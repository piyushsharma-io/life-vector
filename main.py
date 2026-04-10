"""
                LIFE VECTOR
        PERSONAL ASSISTANT SOFTWARE
        
This program demonstrates:
- File Handling: CSV, Text (.txt), and Binary (.dat) files
- Exception Handling: Try-except blocks for error management
- Modules: csv, os, random, time, datetime
"""

import csv
import os
import random
import time
import datetime
import sys

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.csv")   # OS.PATH.JOIN CONNECTS 2 PATHS OR DIRECTORIES WITHOUT THE HASSEL OF WRITING ITS COMPLETE LOCATION AND
TASKS_FILE = os.path.join(DATA_DIR, "tasks.csv")    # IT ALSO HELPS IN ALLOCATING THE RIGHT PATH FOR DIFFERENT OPERATING SYSTEMS LIKE WINDOWS,MAC,LINUX.
MOOD_FILE = os.path.join(DATA_DIR, "mood.csv")
FINANCE_FILE = os.path.join(DATA_DIR, "finance.csv")
NOTES_FILE = os.path.join(DATA_DIR, "notes.txt")
QUOTES_FILE = "quotes.txt"

current_user = None

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')    #CLEARS THE SCREEN AFTER CHECKING THE OPERATING SYTEM IN WHICH THE PROGRAM IS RUNNING, CLS-WINDOWS & CLEAR-MAC,LINUX

def pause():
    """Pause and wait for user input"""
    input("\nPress Enter to continue...")

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {title}")         #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
    print("=" * 60)

def print_menu(title, options):
    """Print a formatted menu"""
    print_header(title)
    i = 1
    for option in options:
        print(f"  [{i}] {option}")      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        i = i + 1
    print("=" * 60)

def initialize_data_files():
    """Create data directory and initialize CSV files with headers if they don't exist"""
    try:
        if not os.path.exists(DATA_DIR):                    #CHECKS IF THE DIEECTORY EXISTS OR NOT. IF NOT THEN IT IS CREATED.
            os.makedirs(DATA_DIR)                           #THIS CREATES MULTIPLE DIRECTORIED UNDER THE MAIN DIRECTORY DATA_DIR='data'
            print(f"Created data directory: {DATA_DIR}")    #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
        if not os.path.exists(USERS_FILE):                  #CHECKS IF THE FILE EXISTS OR NOT. IF NOT THEN IT IS CREATED.
            with open(USERS_FILE, 'w', newline='') as f:    #OPENING A FILE IN WRITE MODE WILL ALSO CREATE A NEW FILE IF IT DOESN'T EXIST
                writer = csv.writer(f)
                writer.writerow(['username', 'password', 'created_date'])
            print("Initialized users.csv")
        
        if not os.path.exists(TASKS_FILE):                  #CHECKS IF THE FILE EXISTS OR NOT. IF NOT THEN IT IS CREATED.
            with open(TASKS_FILE, 'w', newline='') as f:    #OPENING A FILE IN WRITE MODE WILL ALSO CREATE A NEW FILE IF IT DOESN'T EXIST
                writer = csv.writer(f)
                writer.writerow(['username', 'task_name', 'due_date', 'status', 'category'])
            print("Initialized tasks.csv")
        
        if not os.path.exists(MOOD_FILE):                   #CHECKS IF THE FILE EXISTS OR NOT. IF NOT THEN IT IS CREATED.
            with open(MOOD_FILE, 'w', newline='') as f:     #OPENING A FILE IN WRITE MODE WILL ALSO CREATE A NEW FILE IF IT DOESN'T EXIST
                writer = csv.writer(f)
                writer.writerow(['username', 'date', 'mood'])
            print("Initialized mood.csv")
        
        if not os.path.exists(FINANCE_FILE):                #CHECKS IF THE FILE EXISTS OR NOT. IF NOT THEN IT IS CREATED.
            with open(FINANCE_FILE, 'w', newline='') as f:      #OPENING A FILE IN WRITE MODE WILL ALSO CREATE A NEW FILE IF IT DOESN'T EXIST
                writer = csv.writer(f)
                writer.writerow(['username', 'amount', 'category', 'date', 'type', 'description'])
            print("Initialized finance.csv")
        
        if not os.path.exists(NOTES_FILE):                  #CHECKS IF THE FILE EXISTS OR NOT. IF NOT THEN IT IS CREATED.
            with open(NOTES_FILE, 'w') as f:                #OPENING A FILE IN WRITE MODE WILL ALSO CREATE A NEW FILE IF IT DOESN'T EXIST
                f.write("")
            print("Initialized notes.txt")
            
    except OSError as e:
        print(f"Error creating data files: {e}")
    except Exception as e:
        print(f"Unexpected error during initialization: {e}")

def load_quotes():
    """Load motivational quotes from quotes.txt file"""
    quotes = {
        'Happy': [],
        'Sad': [],
        'Stressed': [],
        'Tired': [],
        'Excited': [],
        'Anxious': []
    }
    
    try:
        if os.path.exists(QUOTES_FILE):         #HERE IT CHECKS  IF THE FILE IS THERE,--> IT HASN'T BEEN DELETED AND IT EXISTS.
            with open(QUOTES_FILE, 'r') as f:
                current_mood = None
                for line in f:
                    line = line.strip()
                    if line.startswith('[') and line.endswith(']'):
                        current_mood = line[1:-1]
                        if current_mood not in quotes:
                            quotes[current_mood] = []
                    elif line and current_mood:
                        quotes[current_mood].append(line)
    except FileNotFoundError:
        print("Quotes file not found. Using default quotes.")
    except Exception as e:
        print(f"Error loading quotes: {e}")         #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
    
    return quotes

def get_random_quote(mood):
    """Get a random quote based on mood"""
    quotes = load_quotes()
    if mood in quotes and quotes[mood]:
        return random.choice(quotes[mood])                           #RANDOM MODULE RETURNS A RANDOM QUOTE BASED ON THE MOOD.
    return "Every day is a new opportunity to grow and learn!"

def register_user():
    """Register a new user"""
    print_header("USER REGISTRATION")
    
    try:
        username = input("Enter username: ").strip()        #STRIP() REMOVESS SPACES WHICH IS BETTER FOR STORING USERNAMES AND PASSWORDS.
        if not username:
            print("Username cannot be empty!")
            return False
        
        with open(USERS_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                if row[0].lower() == username.lower():
                    print("Username already exists! Please choose another.")
                    return False
        
        password = input("Enter password: ").strip()
        if len(password) < 4:
            print("Password must be at least 4 characters!")
            return False
        
        created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")        #TIME FORMAT--> YEAR-MONTH-DAY HOUR:MINUTES:SECONDS
        
        with open(USERS_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, password, created_date])
        
        print(f"\nRegistration successful! Welcome, {username}!")   #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        time.sleep(1)                                               #CREATES A TIME LAG FOR THE NEXT CODE TO BE EXECUTED.
        return True
        
    except FileNotFoundError:
        print("Error: User database not found. Please restart the program.")
        return False
    except Exception as e:
        print(f"Error during registration: {e}")    #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        return False

def login_user():
    """Login an existing user"""
    global current_user
    print_header("USER LOGIN")
    
    try:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        with open(USERS_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)                                    #SKIP HEADER i.e. THE NAME OR HEADINGS
            for row in reader:
                if row[0] == username and row[1] == password:
                    current_user = username
                    print(f"\nLogin successful! Welcome back, {username}!") #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                    time.sleep(1)
                    return True
        
        print("Invalid username or password!")
        return False
        
    except FileNotFoundError:
        print("Error: User database not found. Please restart the program.")
        return False
    except Exception as e:
        print(f"Error during login: {e}")   #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        return False

def ask_mood():
    """Ask user for their current mood and store it"""
    print_header("HOW ARE YOU FEELING TODAY?")
    moods = ['Happy', 'Sad', 'Stressed', 'Tired', 'Excited', 'Anxious']
    
    i = 1
    for mood in moods:
        print(f"  [{i}] {mood}")    #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        i = i + 1
    
    try:
        choice = int(input("\nSelect your mood (1-6): "))
        if 1 <= choice <= 6:
            selected_mood = moods[choice - 1]
            
            today = datetime.date.today().strftime("%Y-%m-%d")
            with open(MOOD_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([current_user, today, selected_mood])
            
            quote = get_random_quote(selected_mood)
            print(f"\n╔{'═' * 58}╗")                        #   "╔,╗" SYMBOLS USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)
            print(f"║  Your mood: {selected_mood:<45}║")    #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            print(f"╠{'═' * 58}╣")                          #   "║" SYMBOL USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)
            print(f"║  Quote for you:{'':>42}║")            #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            
            words = quote.split()
            line = ""
            for word in words:
                if len(line) + len(word) + 1 <= 54:
                    line += word + " "
                else:
                    print(f"║  {line:<55}║")    #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                    line = word + " "
            if line:
                print(f"║  {line:<56}║")    #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            print(f"╚{'═' * 58}╝")
            
            time.sleep(3)
            return selected_mood
        else:
            print("Invalid choice. Setting mood as 'Happy'")
            return 'Happy'
    except ValueError:
        print("Invalid input. Setting mood as 'Happy'")
        return 'Happy'
    except Exception as e:
        print(f"Error recording mood: {e}") #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        return 'Happy'

def show_dashboard():
    """Display the main dashboard with summary information"""
    clear_screen()
    print("\n" + "╔" + "═" * 58 + "╗")
    print(f"║{'LIFE VECTOR DASHBOARD':^58}║")           #   "║" SYMBOL USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)
    print(f"║{'Welcome, ' + str(current_user):^58}║")   #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
    print("╠" + "═" * 58 + "╣")
    
    today = datetime.date.today()
    print(f"║  Date: {today.strftime('%A, %B %d, %Y'):<50}║")   #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
    print("╠" + "═" * 58 + "╣")
    
    try:
        pending_daily = 0
        pending_weekly = 0
        upcoming_deadlines = []
        
        with open(TASKS_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)                                    # SKIP HEADER
            for row in reader:
                # row: 0=username, 1=task_name, 2=due_date, 3=status, 4=category
                if row[0] == current_user and row[3].lower() == 'pending':
                    if row[4].lower() == 'daily':
                        pending_daily += 1
                    else:
                        pending_weekly += 1
                    
                    try:
                        due_date = datetime.datetime.strptime(row[2], "%Y-%m-%d").date()
                        days_left = (due_date - today).days
                        if 0 <= days_left <= 3:
                            upcoming_deadlines.append((row[1], days_left))
                    except ValueError:
                        pass
        
        print(f"║  TASKS SUMMARY:{'':>42}║")        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"║    Pending Daily Tasks: {pending_daily:<33}║")        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"║    Pending Weekly Tasks: {pending_weekly:<32}║")      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
        if upcoming_deadlines:
            print(f"║  UPCOMING DEADLINES (within 3 days):{'':>21}║")  #   "║" SYMBOL USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)
            for task, days in upcoming_deadlines[:3]:
                if days == 0:
                    deadline_text = "DUE TODAY!"
                elif days == 1:
                    deadline_text = "Due tomorrow"
                else:
                    deadline_text = f"Due in {days} days"       #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                task_display = task[:30] + "..." if len(task) > 30 else task
                print(f"║    - {task_display}: {deadline_text:<20}║")       #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
    except FileNotFoundError:
        print(f"║  Tasks: No data available{'':>32}║")  #   "║" SYMBOL USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)
    except Exception as e:
        print(f"║  Tasks: Error loading data{'':>30}║") #   "║" SYMBOL USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)
    
    print("╠" + "═" * 58 + "╣")
    
    try:
        total_income = 0
        total_expense = 0
        
        with open(FINANCE_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                # row: 0=username, 1=amount, 2=category, 3=date, 4=type, 5=description
                if row[0] == current_user:
                    amount = float(row[1])              #FLOAT STORES THE AMOUNT IN DECIMAL VALUES
                    if row[4].lower() == 'income':
                        total_income += amount
                    else:
                        total_expense += amount
        
        balance = total_income - total_expense
        
        print(f"║  FINANCE SUMMARY:{'':>40}║")                          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"║    Total Income:  Rs. {total_income:<35.2f}║")        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"║    Total Expense: Rs. {total_expense:<35.2f}║")       #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"║    Balance:       Rs. {balance:<35.2f}║")             #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
        if balance < 0:
            print(f"║  ⚠ WARNING: You are overspending!{'':>23}║")     #   "⚠" SYMBOL USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)
        elif balance < 500:
            print(f"║  ⚠ ALERT: Low balance!{'':>35}║")                #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            
    except FileNotFoundError:
        print(f"║  Finance: No data available{'':>29}║")
    except Exception as e:
        print(f"║  Finance: Error loading data{'':>28}║")
    
    print("╚" + "═" * 58 + "╝")         #   "╚,╝" SYMBOL USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)

def task_management():
    """Task Management System"""
    while True:
        clear_screen()
        print_menu("TASK MANAGEMENT", [
            "View All Tasks",
            "Add New Task",
            "Mark Task Complete",
            "Delete Task",
            "View Daily Tasks",
            "View Weekly Tasks",
            "Back to Main Menu"
        ])
        
        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                view_tasks('daily')
            elif choice == 6:
                view_tasks('weekly')
            elif choice == 7:
                break
            else:
                print("Invalid choice!")
            
            pause()
            
        except ValueError:
            print("Please enter a valid number!")
            pause()
        except Exception as e:
            print(f"Error: {e}")
            pause()

def view_tasks(category=None):
    """View tasks with optional category filter"""
    print_header("YOUR TASKS")
    
    try:
        tasks = []
        with open(TASKS_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                # row: 0=username, 1=task_name, 2=due_date, 3=status, 4=category
                if row[0] == current_user:
                    if category is None or row[4].lower() == category.lower():
                        task = {'username': row[0], 'task_name': row[1], 'due_date': row[2], 'status': row[3], 'category': row[4]}
                        tasks.append(task)
        
        if not tasks:
            print("No tasks found!")
            return
        
        today = datetime.date.today()           #RETURNS THE CURRENT TIME AND DATE
        print(f"\n{'No.':<5}{'Task Name':<25}{'Due Date':<12}{'Status':<12}{'Category':<10}{'Days Left':<10}")  #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print("-" * 74)
        
        i = 1
        for task in tasks:
            try:
                due_date = datetime.datetime.strptime(task['due_date'], "%Y-%m-%d").date()
                days_left = (due_date - today).days
                if days_left < 0:
                    days_text = "OVERDUE"
                elif days_left == 0:
                    days_text = "TODAY!"
                else:
                    days_text = str(days_left)
            except ValueError:
                days_text = "N/A"
            
            task_name = task['task_name'][:22] + "..." if len(task['task_name']) > 25 else task['task_name']
            print(f"{i:<5}{task_name:<25}{task['due_date']:<12}{task['status']:<12}{task['category']:<10}{days_text:<10}")      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            i = i + 1
            
    except FileNotFoundError:
        print("No tasks file found!")
    except Exception as e:
        print(f"Error viewing tasks: {e}")      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def add_task():
    """Add a new task"""
    print_header("ADD NEW TASK")
    
    try:
        task_name = input("Enter task name: ").strip()
        if not task_name:
            print("Task name cannot be empty!")
            return
        
        while True:
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD")
        
        print("\nCategory:")
        print("  [1] Daily")
        print("  [2] Weekly")
        cat_choice = input("Select category (1/2): ").strip()
        category = "daily" if cat_choice == "1" else "weekly"
        
        with open(TASKS_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([current_user, task_name, due_date, 'pending', category])
        
        print(f"\nTask '{task_name}' added successfully!")      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
    except Exception as e:
        print(f"Error adding task: {e}")        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def mark_task_complete():
    """Mark a task as complete"""
    view_tasks()
    
    try:
        tasks = []
        with open(TASKS_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                task = {'username': row[0], 'task_name': row[1], 'due_date': row[2], 'status': row[3], 'category': row[4]}
                tasks.append(task)
        
        user_tasks = [t for t in tasks if t['username'] == current_user and t['status'].lower() == 'pending']
        if not user_tasks:
            print("No pending tasks to mark complete!")
            return
        
        task_num = int(input("\nEnter task number to mark complete: ")) - 1
        if task_num < 0 or task_num >= len([t for t in tasks if t['username'] == current_user]):
            print("Invalid task number!")
            return
        
        user_task_count = 0
        for task in tasks:
            if task['username'] == current_user:
                if user_task_count == task_num:
                    task['status'] = 'completed'
                    print(f"Task '{task['task_name']}' marked as complete!")        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                    break
                user_task_count += 1
        
        with open(TASKS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['username', 'task_name', 'due_date', 'status', 'category'])
            for task in tasks:
                writer.writerow([task['username'], task['task_name'], task['due_date'], task['status'], task['category']])
            
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"Error: {e}")

def delete_task():
    """Delete a task"""
    view_tasks()
    
    try:
        tasks = []
        with open(TASKS_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                task = {'username': row[0], 'task_name': row[1], 'due_date': row[2], 'status': row[3], 'category': row[4]}
                tasks.append(task)
        
        user_tasks = [t for t in tasks if t['username'] == current_user]
        if not user_tasks:
            print("No tasks to delete!")
            return
        
        task_num = int(input("\nEnter task number to delete: ")) - 1
        if task_num < 0 or task_num >= len(user_tasks):
            print("Invalid task number!")
            return
        
        task_to_delete = user_tasks[task_num]
        confirm = input(f"Are you sure you want to delete '{task_to_delete['task_name']}'? (y/n): ").lower()
        
        if confirm in ['y','Y','yes','YES']:
            tasks = [t for t in tasks if not (t['username'] == current_user and 
                     t['task_name'] == task_to_delete['task_name'] and 
                     t['due_date'] == task_to_delete['due_date'])]
            
            with open(TASKS_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'task_name', 'due_date', 'status', 'category'])
                for task in tasks:
                    writer.writerow([task['username'], task['task_name'], task['due_date'], task['status'], task['category']])
            
            print("Task deleted successfully!")
        else:
            print("Deletion cancelled.")
            
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"Error deleting task: {e}")      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def notes_management():
    """Notes Management System using TEXT files"""
    while True:
        clear_screen()
        print_menu("NOTES MANAGEMENT", [
            "View All Notes",
            "Create New Note",
            "Edit Note",
            "Delete Note",
            "Back to Main Menu"
        ])
        
        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                view_notes()
            elif choice == 2:
                create_note()
            elif choice == 3:
                edit_note()
            elif choice == 4:
                delete_note()
            elif choice == 5:
                break
            else:
                print("Invalid choice!")
            
            pause()
            
        except ValueError:
            print("Please enter a valid number!")
            pause()
        except Exception as e:
            print(f"Error: {e}")        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            pause()

def parse_notes():
    """Parse notes from the text file for storing"""
    notes = []
    
    try:
        with open(NOTES_FILE, 'r') as f:
            content = f.read()
            
        if not content.strip():
            return notes
        
        note_blocks = content.split("---NOTE---")
        for block in note_blocks:
            if block.strip():
                lines = block.strip().split('\n')
                if len(lines) >= 4:
                    note = {
                        'username': lines[0].replace('User: ', '').strip(),
                        'title': lines[1].replace('Title: ', '').strip(),
                        'date': lines[2].replace('Date: ', '').strip(),
                        'content': '\n'.join(lines[3:]).replace('Content: ', '', 1).strip()
                    }
                    notes.append(note)
                    
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error parsing notes: {e}")      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
    
    return notes

def save_notes(notes):
    """Save notes to the text file"""
    try:
        with open(NOTES_FILE, 'w') as f:
            for note in notes:
                f.write("---NOTE---\n")                         #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                f.write(f"User: {note['username']}\n")          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                f.write(f"Title: {note['title']}\n")            #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                f.write(f"Date: {note['date']}\n")              #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                f.write(f"Content: {note['content']}\n\n")      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
    except Exception as e:
        print(f"Error saving notes: {e}")                       #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def view_notes():
    """View all notes for current user"""
    print_header("YOUR NOTES")
    
    notes = parse_notes()
    user_notes = [n for n in notes if n['username'] == current_user]
    
    if not user_notes:
        print("No notes found!")
        return
    
    i = 1
    for note in user_notes:
        print(f"\n[{i}] {note['title']}")           #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"    Date: {note['date']}")          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"    Content: {note['content'][:50]}..." if len(note['content']) > 50 else f"    Content: {note['content']}")
        print("-" * 40)
        i = i + 1

def create_note():
    """Create a new note"""
    print_header("CREATE NEW NOTE")
    
    try:
        title = input("Enter note title: ").strip()
        if not title:
            print("Title cannot be empty!")
            return
        
        print("Enter note content (press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        
        content = '\n'.join(lines)
        if not content:
            print("Content cannot be empty!")
            return
        
        notes = parse_notes()
        new_note = {
            'username': current_user,
            'title': title,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'content': content
        }
        notes.append(new_note)
        save_notes(notes)
        
        print(f"\nNote '{title}' created successfully!")        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
    except Exception as e:
        print(f"Error creating note: {e}")                      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def edit_note():
    """Edit an existing note"""
    view_notes()
    
    try:
        notes = parse_notes()
        user_notes = [n for n in notes if n['username'] == current_user]
        
        if not user_notes:
            print("No notes to edit!")
            return
        
        note_num = int(input("\nEnter note number to edit: ")) - 1
        if note_num < 0 or note_num >= len(user_notes):
            print("Invalid note number!")
            return
        
        old_note = user_notes[note_num]
        
        print(f"\nEditing: {old_note['title']}")            #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        new_title = input(f"New title (press Enter to keep '{old_note['title']}'): ").strip()           #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print("New content (press Enter twice to finish, or just Enter to keep current):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        new_content = '\n'.join(lines)
        
        for note in notes:
            if (note['username'] == current_user and 
                note['title'] == old_note['title'] and 
                note['date'] == old_note['date']):
                if new_title:
                    note['title'] = new_title
                if new_content:
                    note['content'] = new_content
                note['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        save_notes(notes)
        print("Note updated successfully!")
        
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"Error editing note: {e}")               #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def delete_note():
    """Delete a note"""
    view_notes()
    
    try:
        notes = parse_notes()
        user_notes = [n for n in notes if n['username'] == current_user]
        
        if not user_notes:
            print("No notes to delete!")
            return
        
        note_num = int(input("\nEnter note number to delete: ")) - 1
        if note_num < 0 or note_num >= len(user_notes):
            print("Invalid note number!")
            return
        
        note_to_delete = user_notes[note_num]
        confirm = input(f"Are you sure you want to delete '{note_to_delete['title']}'? (y/n): ").lower()            #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
        if confirm in ['y','Y','yes','YES']:
            notes = [n for n in notes if not (n['username'] == current_user and 
                     n['title'] == note_to_delete['title'] and 
                     n['date'] == note_to_delete['date'])]
            save_notes(notes)
            print("Note deleted successfully!")
        else:
            print("Deletion cancelled.")
            
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"Error deleting note: {e}")          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def mood_tracking():
    """Mood Tracking System"""
    while True:
        clear_screen()
        print_menu("MOOD TRACKING", [
            "View Mood History",
            "Log Current Mood",
            "View Mood Statistics",
            "Back to Main Menu"
        ])
        
        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                view_mood_history()
            elif choice == 2:
                ask_mood()
            elif choice == 3:
                view_mood_stats()
            elif choice == 4:
                break
            else:
                print("Invalid choice!")
            
            pause()
            
        except ValueError:
            print("Please enter a valid number!")
            pause()
        except Exception as e:
            print(f"Error: {e}")            #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            pause()

def view_mood_history():
    """View mood history for current user"""
    print_header("MOOD HISTORY")
    
    try:
        moods = []
        with open(MOOD_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                # row: 0=username, 1=date, 2=mood
                if row[0] == current_user:
                    mood_entry = {'username': row[0], 'date': row[1], 'mood': row[2]}
                    moods.append(mood_entry)
        
        if not moods:
            print("No mood entries found!")
            return
        
        print(f"\n{'Date':<15}{'Mood':<15}")            #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print("-" * 30)
        
        for mood in moods[-10:]:
            print(f"{mood['date']:<15}{mood['mood']:<15}")          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            
        print(f"\nShowing last {min(10, len(moods))} entries out of {len(moods)} total.")           #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
    except FileNotFoundError:
        print("No mood data found!")
    except Exception as e:
        print(f"Error viewing mood history: {e}")           #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def view_mood_stats():
    """View mood statistics"""
    print_header("MOOD STATISTICS")
    
    try:
        mood_counts = {}
        with open(MOOD_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                # row: 0=username, 1=date, 2=mood
                if row[0] == current_user:
                    mood = row[2]
                    mood_counts[mood] = mood_counts.get(mood, 0) + 1
        
        if not mood_counts:
            print("No mood data found!")
            return
        
        total = sum(mood_counts.values())
        print(f"\nTotal entries: {total}")          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print("\nMood Distribution:")
        print("-" * 40)
        
        for mood, count in sorted(mood_counts.items(), key=lambda x: x[1], reverse=True):   #LAMBDA IS AN ANONAMOUS FUNC. USED FOR A MINUTE TASK FOE WHICH A SEPARATE FUNCTION DEFINATION IS NOT REQUIRED.
            percentage = (count / total) * 100
            bar = "█" * int(percentage / 5)                              #BAR COPIED FROM WEB ART GENERATOR(websource- https://www.asciiart.eu)
            print(f"{mood:<12} {count:>4} ({percentage:>5.1f}%) {bar}") #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
        most_common = max(mood_counts, key=lambda x: mood_counts[x])
        print(f"\nMost common mood: {most_common}")                     #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
    except FileNotFoundError:
        print("No mood data found!")
    except Exception as e:
        print(f"Error viewing mood stats: {e}")             #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def financial_tracker():
    """Financial Tracker System"""
    while True:
        clear_screen()
        print_menu("FINANCIAL TRACKER", [
            "View Financial Summary",
            "Add Income",
            "Add Expense",
            "View All Transactions",
            "Category-wise Report",
            "Back to Main Menu"
        ])
        
        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                view_finance_summary()
            elif choice == 2:
                add_finance_entry('income')
            elif choice == 3:
                add_finance_entry('expense')
            elif choice == 4:
                view_all_transactions()
            elif choice == 5:
                category_wise_report()
            elif choice == 6:
                break
            else:
                print("Invalid choice!")
            
            pause()
            
        except ValueError:
            print("Please enter a valid number!")
            pause()
        except Exception as e:
            print(f"Error: {e}")            #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            pause()

def view_finance_summary():
    """View financial summary"""
    print_header("FINANCIAL SUMMARY")
    
    try:
        total_income = 0
        total_expense = 0
        
        with open(FINANCE_FILE, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)    # skip header
            for row in reader:
                # row: 0=username, 1=amount, 2=category, 3=date, 4=type, 5=description
                if row[0] == current_user:
                    amount = float(row[1])
                    if row[4].lower() == 'income':
                        total_income += amount
                    else:
                        total_expense += amount
        
        balance = total_income - total_expense
        
        print(f"\n╔{'═' * 40}╗")                                    #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"║  Total Income:  Rs. {total_income:>18.2f} ║")     #   "║" SYMBOL USED FROM WEB VIA ONLINE ASCII ART GENERATOR(websource- https://www.asciiart.eu)
        print(f"║  Total Expense: Rs. {total_expense:>18.2f} ║")    #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"╠{'═' * 40}╣")                                      #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"║  Balance:       Rs. {balance:>18.2f} ║")          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print(f"╚{'═' * 40}╝")
        
                #GENERAL MEGGASES FOR USERS FINANCIAL REPORT

        if balance < 0:
            print("\n⚠ WARNING: You are OVERSPENDING!")        #THESE SYMBOLS ARE ADDED THROUGH WINDOWS+(.) KEY. THEY CAN ALSO BE COPIED FROM THE WEB.
            print("  Your expenses exceed your income!")
        elif balance < 500:
            print("\n⚠ ALERT: Your balance is running low!")    #THESE SYMBOLS ARE ADDED THROUGH WINDOWS+(.) KEY. THEY CAN ALSO BE COPIED FROM THE WEB.
        elif balance > 5000:
            print("\n✓ Great! You're saving well!")                #THESE SYMBOLS ARE ADDED THROUGH WINDOWS+(.) KEY. THEY CAN ALSO BE COPIED FROM THE WEB.
            
    except FileNotFoundError:
        print("No financial data found!")
    except Exception as e:
        print(f"Error viewing summary: {e}")                        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def add_finance_entry(entry_type):
    """Add income or expense entry"""
    print_header(f"ADD {entry_type.upper()}")                       #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
    
    categories = ['Food', 'Study', 'Travel', 'Entertainment', 'Shopping', 'Bills', 'Salary', 'Gift', 'Other']
    
    try:
        while True:
            try:
                amount = float(input("Enter amount (Rs.): "))
                if amount <= 0:
                    print("Amount must be positive!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        
        print("\nCategories:")
        i = 1
        for cat in categories:
            print(f"  [{i}] {cat}")                 #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            i = i + 1
        
        cat_choice = int(input("Select category (1-9): "))
        if 1 <= cat_choice <= 9:
            category = categories[cat_choice - 1]
        else:
            category = "Other"
        
        description = input("Enter description (optional): ").strip()
        if not description:
            description = f"{entry_type.capitalize()} - {category}"         #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
        today = datetime.date.today().strftime("%Y-%m-%d")
        
        with open(FINANCE_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([current_user, amount, category, today, entry_type, description])
        
        print(f"\n{entry_type.capitalize()} of Rs. {amount:.2f} added successfully!")           #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        
    except ValueError:
        print("Invalid input!")
    except Exception as e:
        print(f"Error adding entry: {e}")           #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def view_all_transactions():
    """View all transactions"""
    print_header("ALL TRANSACTIONS")
    
    try:
        transactions = []
        with open(FINANCE_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['username'] == current_user:
                    transactions.append(row)
        
        if not transactions:
            print("No transactions found!")
            return
        
        print(f"\n{'No.':<5}{'Date':<12}{'Type':<10}{'Amount':<12}{'Category':<12}{'Description':<20}")     #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print("-" * 71)
        
        for i, trans in enumerate(transactions, 1): 
            desc = trans['description'][:17] + "..." if len(trans['description']) > 20 else trans['description']
            type_symbol = "+" if trans['type'].lower() == 'income' else "-"
            print(f"{i:<5}{trans['date']:<12}{trans['type']:<10}{type_symbol}Rs.{float(trans['amount']):<8.2f}{trans['category']:<12}{desc:<20}")
            
    except FileNotFoundError:
        print("No financial data found!")
    except Exception as e:
        print(f"Error viewing transactions: {e}")       #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def category_wise_report():
    """Show category-wise spending report"""
    print_header("CATEGORY-WISE REPORT")
    
    try:
        category_totals = {}
        
        with open(FINANCE_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['username'] == current_user and row['type'].lower() == 'expense':
                    category = row['category']
                    amount = float(row['amount'])
                    category_totals[category] = category_totals.get(category, 0) + amount
        
        if not category_totals:
            print("No expense data found!")
            return
        
        total_expense = sum(category_totals.values())
        
        print(f"\nTotal Expenses: Rs. {total_expense:.2f}")         #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
        print("\nCategory-wise Breakdown:")
        print("-" * 50)
        
        for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):      #LAMBDA IS AN ANONAMOUS FUNC. USED FOR A MINUTE TASK FOE WHICH A SEPARATE FUNCTION DEFINATION IS NOT REQUIRED.
            percentage = (amount / total_expense) * 100
            bar = "█" * int(percentage / 5)                             #BAR COPIED FROM WEB ART GENERATOR(websource- https://www.asciiart.eu)
            print(f"{category:<15} Rs.{amount:>10.2f} ({percentage:>5.1f}%) {bar}")         #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            
    except FileNotFoundError:
        print("No financial data found!")
    except Exception as e:
        print(f"Error generating report: {e}")          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.

def main_menu():
    """Main menu after login"""
    global current_user
    
    while True:
        show_dashboard()
        
        print("\n" + "=" * 60)
        print("  MAIN MENU")
        print("=" * 60)
        print("  [1] Task Management")
        print("  [2] Notes")
        print("  [3] Mood Tracking")
        print("  [4] Financial Tracker")
        print("  [5] Logout")
        print("  [6] Exit Program")
        print("=" * 60)
        
        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                task_management()
            elif choice == 2:
                notes_management()
            elif choice == 3:
                mood_tracking()
            elif choice == 4:
                financial_tracker()
            elif choice == 5:
                print(f"\nGoodbye, {current_user}! See you soon!")          #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
                current_user = None
                time.sleep(1)
                break
            elif choice == 6:
                print("\nThank you for using LIFE VECTOR!")
                print("Goodbye!")
                time.sleep(1)
                sys.exit(0)
            else:
                print("Invalid choice!")
                pause()
                
        except ValueError:
            print("Please enter a valid number!")
            pause()
        except Exception as e:
            print(f"Error: {e}")            #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            pause()

def welcome_screen():
    """Display welcome screen and login menu"""
    while True:
        clear_screen()
        print("\n") #ASCII ART CREATED FROM ONLINE ASCII-ART-GENERATOR (websource- https://www.asciiart.eu/text-to-ascii-art  "ANSI SHADOW FONT")
        print("╔════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                                        ║")
        print("║   ██╗     ██╗███████╗███████╗    ██╗   ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗    ║")
        print("║   ██║     ██║██╔════╝██╔════╝    ██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗   ║")
        print("║   ██║     ██║█████╗  █████╗      ██║   ██║█████╗  ██║        ██║   ██║   ██║██████╔╝   ║")
        print("║   ██║     ██║██╔══╝  ██╔══╝      ╚██╗ ██╔╝██╔══╝  ██║        ██║   ██║   ██║██╔══██╗   ║")
        print("║   ███████╗██║██║     ███████╗     ╚████╔╝ ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║   ║")
        print("║   ╚══════╝╚═╝╚═╝     ╚══════╝      ╚═══╝  ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ║")
        print("║                                                                                        ║")
        print("║                              Your Personal Life Assistant                              ║")
        print("║                               (CREATOR--> PIYUSH SHARMA)                               ║")
        print("║                                                                                        ║")
        print("╚════════════════════════════════════════════════════════════════════════════════════════╝")
        print("\n")
        print("  [1] Login")
        print("  [2] Register")
        print("  [3] Exit")
        print("\n" + "=" * 60)
        
        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                if login_user():
                    ask_mood()
                    main_menu()
            elif choice == 2:
                register_user()
                pause()
            elif choice == 3:
                print("\nThank you for using LIFE VECTOR!")
                print("Goodbye!")
                time.sleep(1)
                break
            else:
                print("Invalid choice!")
                pause()
                
        except ValueError:
            print("Please enter a valid number!")
            pause()
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")        #THIS IS A F-STRING USED TO FORMAT THE STRING WITH VARIABLES AND SHORTEN THE CODE LINES.
            pause()

def main():
    """Main function to start the program"""
    print("\nInitializing LIFE VECTOR...")
    initialize_data_files()
    time.sleep(1)
    welcome_screen()

if __name__ == "__main__":
    main()


from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date.date()}\nStatus: {self.status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"No task found with title: {title}")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"Task {i}:\n{task}")

    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if task.status == "Incomplete"]
        if not incomplete_tasks:
            print("No incomplete tasks.")
        else:
            for i, task in enumerate(incomplete_tasks, 1):
                print(f"Incomplete Task {i}:\n{task}")


# Main CLI Program
def main():
    todo_list = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)

        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)

        elif choice == "3":
            todo_list.list_all_tasks()

        elif choice == "4":
            todo_list.list_incomplete_tasks()

        elif choice == "5":
            print("Exiting ToDo List. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")

# Test the application by running the main program
if __name__ == "__main__":
    main()






from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content
        print("Post updated successfully.")

    def __str__(self):
        return (f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Content:\n{self.content}\n")

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for i, post in enumerate(self.posts, 1):
                print(f"\nPost {i}:\n{post}")

    def posts_by_author(self, author):
        filtered = [post for post in self.posts if post.author.lower() == author.lower()]
        if not filtered:
            print(f"No posts found by author: {author}")
        else:
            for post in filtered:
                print(post)

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' deleted.")
                return
        print(f"No post found with title: {title}")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                new_title = input("Enter new title: ")
                new_content = input("Enter new content: ")
                post.edit(new_title, new_content)
                return
        print(f"No post found with title: {title}")

    def display_latest_posts(self, count=3):
        if not self.posts:
            print("No posts available.")
        else:
            sorted_posts = sorted(self.posts, key=lambda p: p.created_at, reverse=True)
            for i, post in enumerate(sorted_posts[:count], 1):
                print(f"\nLatest Post {i}:\n{post}")

# Main CLI Program
def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(Post(title, content, author))

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.posts_by_author(author)

        elif choice == "4":
            title = input("Enter title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            blog.display_latest_posts()

        elif choice == "7":
            print("Exiting Blog System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Test the application
if __name__ == "__main__":
    main()












class Account:
    def __init__(self, acc_number, holder_name, balance=0.0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient funds (Overdraft not allowed).")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"${amount:.2f} transferred to Account {target_account.acc_number}.")
        else:
            print("Transfer failed: insufficient funds.")

    def display_details(self):
        print(f"Account Number: {self.acc_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}\n")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc_number, holder_name, balance=0.0):
        if acc_number in self.accounts:
            print("Account with this number already exists.")
        else:
            self.accounts[acc_number] = Account(acc_number, holder_name, balance)
            print("Account created successfully.")

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def check_balance(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit_money(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_money(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer_money(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver:
            sender.transfer(receiver, amount)
        else:
            print("One or both accounts not found.")

    def show_account_details(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            account.display_details()
        else:
            print("Account not found.")


# Main CLI Program
def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            acc_number = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            try:
                balance = float(input("Enter initial deposit: "))
            except ValueError:
                balance = 0.0
            bank.add_account(acc_number, name, balance)

        elif choice == "2":
            acc_number = input("Enter account number: ")
            bank.check_balance(acc_number)

        elif choice == "3":
            acc_number = input("Enter account number: ")
            try:
                amount = float(input("Enter deposit amount: "))
                bank.deposit_money(acc_number, amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "4":
            acc_number = input("Enter account number: ")
            try:
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw_money(acc_number, amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "5":
            from_acc = input("Enter sender's account number: ")
            to_acc = input("Enter receiver's account number: ")
            try:
                amount = float(input("Enter transfer amount: "))
                bank.transfer_money(from_acc, to_acc, amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "6":
            acc_number = input("Enter account number: ")
            bank.show_account_details(acc_number)

        elif choice == "7":
            print("Exiting Banking System. Goodbye!")
            break

        else:
            print("Invalid option. Choose between 1 and 7.")

# Run the CLI
if __name__ == "__main__":
    main()

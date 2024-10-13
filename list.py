def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Feedback")
    print("5. Exit")
    

# Function to view tasks
def view_tasks(to_do_list):
    if not to_do_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task(to_do_list):
    task = input("\nEnter the task you want to add: ")
    to_do_list.append(task)
    print(f"'{task}' has been added to your list.")

# Function to remove a task
def remove_task(to_do_list):
    if not to_do_list:
        print("\nYour to-do list is empty! No task to remove.")
        return
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1 <= task_number <= len(to_do_list):
            removed_task = to_do_list.pop(task_number - 1)
            print(f"'{removed_task}' has been removed from your list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the To-Do list
def run_to_do_list():
    to_do_list = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            view_tasks(to_do_list)
        elif choice == '2':
            add_task(to_do_list)
        elif choice == '3':
            remove_task(to_do_list)
        elif choice =='4':
            feedback= (input("Your Feedback:"))
            print("\n Thanks for your Feedback")
        elif choice == '5':
            print("\nExiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid option, please choose a valid number.")

# Run the to-do list application
if __name__ == "__main__":
    print("\nHello!\n This is a programme developed to help you maintain your TO-DO List.\n Hope you find it helpful.")
    print("\nFeatures of the To-Do List:")
    print("\nView To-Do List: Displays the current tasks.")
    print("Add a Task: Allows you to input and add tasks to the list.")
    print("Remove a Task: Removes a task based on its position.")
    print("Exit: Terminates the program.")
    run_to_do_list()

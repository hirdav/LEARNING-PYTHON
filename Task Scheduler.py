# from collections import deque

# # Initialize an empty list to hold all tasks (task_id, priority)
# tasks = []

# # Function to add a task to the system
# def add_task(task_id, priority):
#     tasks.append((task_id, priority))

# # Function to process the next task (highest priority first)
# def process_task():
#     if not tasks:
#         print("No tasks to process.")
#         return
    
#     # Sort tasks based on priority (higher first) and maintain FIFO for same priority
#     tasks.sort(key=lambda x: x[1], reverse=True)
    
#     # Process the highest priority task (which is now at index 0)
#     task_to_process = tasks.pop(0)
#     print(f"Processing task {task_to_process[0]} with priority {task_to_process[1]}")

# # Function to display current tasks
# def display_tasks():
#     if not tasks:
#         print("No tasks available.")
#         return
    
#     print("Current tasks (task_id, priority):")
#     for task in tasks:
#         print(f"Task {task[0]}, Priority {task[1]}")

# # Example usage
# add_task(1, 2)  # Add task with id 1 and priority 2
# add_task(2, 1)  # Add task with id 2 and priority 1
# add_task(3, 3)  # Add task with id 3 and priority 3
# add_task(4, 2)  # Add task with id 4 and priority 2

# display_tasks()   # Display all tasks

# # Process tasks based on priority
# process_task()  # Expected: Task 3 (priority 3)
# process_task()  # Expected: Task 1 (priority 2)
# process_task()  # Expected: Task 4 (priority 2)
# process_task()  # Expected: Task 2 (priority 1)

# # Display tasks after processing
# display_tasks()  # Expected: No tasks available


Task_1='adding'
Task_2='multi'
Task_3='subst'

Priority_1=1
Priority_2=2
Priority_3=3



Task=[(Task_1,Priority_1),(Task_2,Priority_2),(Task_3,Priority_3)]


print(Task)

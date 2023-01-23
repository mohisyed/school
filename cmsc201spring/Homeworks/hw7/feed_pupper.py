"""
File:    feed_pupper.py
Author:  Mohiuddin Syed
Date:    2/24/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Ask the user a set of questions about if they have any task to complete.
    program just checks if they have finished them.

"""
number_task = int(input("How many tasks do you have? "))       # this is the counter variable pretty much everything comes from this
all_task = []       # all the task will be entered in this list
no_task = []        # for the last display

for i in range(number_task):   # loop to get the tasks
    task_entry = input("Enter next task: ")
    all_task.append(task_entry)

print("Here are your tasks: ")
for i in range(number_task):    # Display the tasks
    print(i, " {}".format(all_task[i]))

for i in range(len(all_task)):    # loop for asking if you have finished the tasks
    task_completion = input("Have you completed {}: ".format(all_task[i]))
    if task_completion == "no":
        no_task.append(all_task[i])

for i in range(len(no_task)):       # Display the no list
    print("you still need to {}".format(no_task[i]))

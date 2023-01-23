"""
File:         hw3_part1.py
Author:       Mohiuddin Syed
Date:         9/25/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Ask the user for how many tasks do they have. After that system asks user to input
              whether or not they finished the tasks or not.
"""
if __name__ == "__main__":

    user_task = []
    no_task = []
    numberoftasks = int(input("How many tasks do you have? "))

    for i in range(numberoftasks):           # loop used to append the amount of items the user inputs
        x = input("Enter next task: ")
        user_task.append(x)

    if numberoftasks == 0 :                  # if zero program prints and stops running
        print("Thats either negative or postive")
    else:
        print("Here are your tasks:")
        for i in range(len(user_task)):      # loop prints the user tasks
            print(user_task[i])

    for i in range(len(user_task)):          # loop checks whether if they finished they're work
        complete_task = input("Have you finished {} (ENTER yes or no): ".format(user_task[i]))
        if complete_task == "no":            # complete_task == no appends the task the no_task list
            no_task.append(user_task[i])

    for i in range(len(no_task)):            # loop prints out the tasks that haven't been complete
        print("a remaining task is {}".format(no_task[i]))


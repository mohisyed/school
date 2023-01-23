"""
File:         hw3_part5.py
Author:       Mohiuddin Syed
Date:         9/26/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Ask the user for an angle. Depending on the angle they input the system will
            tell them what path of enlightment there angle lands on
"""
if __name__ == "__main__":

    answer = ["Right Resolve", "Right View", "Right Samadhi", "Right Mindfulness", "Right Effort", "Right Livelihood", "Right Conduct", "Right Speed"]
    user_input = int(input("enter an angle to determine the point on the Eightfold Path: "))

    x = (int(user_input % 45))       # modulo divides the user input by 45

    if x != 0:
        print("You have not reached enlightenment yet, try an angle divisible by 45")
    else:
        x = int((user_input % 360)/45)                     # divides the user input futher by modulo division by 360 then integer divison by 45
        print("You have selected is {}".format(answer[x]))





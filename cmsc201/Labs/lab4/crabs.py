"""
File:         crabs.py
Author:       Mohiuddin Syed
Date:         10/1/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Ask the user for crab weight, whether they like their crabs heavy or light,
              then the ideal weight. The splits the from the ideal weight.
"""

if __name__ == "__main__":
    end = "STOP"
    crab_weight = []
    overcrab_weight = []
    under_weight = []
    user_input = (input("Enter Crab weight,     (STOP to end) "))

    while user_input != end:
        crab_weight.append(int(user_input))
        user_input = (input("Enter Crab weight,     (STOP to end) "))

    while user_input == end:
        hvy_ligt_crabs = input("Do you want to keep light or heavy crabs? ")
        if hvy_ligt_crabs != "light" and "heavy":
            print("Must enter light or heavy")
        crab_weight_divider = int(input("What weight determines whether a crab is light or heavy? "))
        for i in range(len(crab_weight)):
            if crab_weight_divider > crab_weight[i]:
                overcrab_weight.append(crab_weight[i])
            elif crab_weight_divider < crab_weight[i]:
                under_weight.append(crab_weight[i])
        if hvy_ligt_crabs == "light":
            print("You are keeping the crabs with weights {}".format(under_weight))
            print("You are not keeping the crabs with weights {}".format(overcrab_weight))
        elif hvy_ligt_crabs == "heavy":
            print("You are keeping the crabs with weights {}".format(overcrab_weight))
            print("You are not keeping the crabs with weights {}".format(under_weight))



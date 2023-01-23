def taxi_cab(input_string):
    total_string = "urdl"
    fake_string = ""
    total_string_dict = ["u", "r", "d", "l"]
    counter = 0
    """
    for i in range(len(input_string)):
        if input_string[i] == total_string[0]:
            fake_string = input_string[i]
            counter += 1
        elif input_string[i] == total_string[1]:
            fake_string = input_string[i]
            counter += 1
        elif input_string[i] == total_string[2]:
            fake_string = input_string[i]
            counter += 1
        elif input_string[i] == total_string[3]:
            fake_string = input_string[i]
            counter += 1
        if fake_string == total_string:
            print(counter)
        """
    # return counter
    print(len(input_string))
    for i in range(len(input_string) - 1):
        if input_string[i] in ["u", "r", "d", "l"]:
            if (input_string[i] == "u" and input_string[i+1] == "d") or (input_string[i] == 'd' and input_string[i + 1] == "u"):
                counter = counter
                fake_string += input_string[i]
                print("doesn't move")
            elif (input_string[i] == "r" and input_string[i + 1] == "l") or (input_string[i] == "l" and input_string[i + 1] == "r"):
                counter = counter
                fake_string += input_string[i]
                print("doesn't move")
            else:
                counter += 1
                fake_string += input_string[i]


    if total_string in fake_string:
        counter = 0


    return print(counter, fake_string)


if __name__ == '__main__':
   taxi_cab("urdl")
   taxi_cab("uuuuu")
   taxi_cab("urdlurdlurdlurdlurdl")

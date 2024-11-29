
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("Please choose right or left? ").lower()

if answer == "left":
    answer = input("You come to a river, round it or swin accross? Type walk or swin: ").lower()

    if answer == "walk":
        print("You walk for miles, run out of water and die")
    
    elif answer == "swin":
        print("You swan accross the river, and be eaten by aligator")
    
    else:
        print("Not a valid option")

elif answer == "right":
    answer = input("You come a bridge, it's very old, you want to cross it or head back (cross/back)? ").lower()

    if answer == "cross":
        print("Several tables are broken, you fell and die")
    
    elif answer == "back":
        print("You go back to main road, you can choose again")
    
    else:
        print("Not a valid option")

    

else:
    print("Not a vali option")

print("Thank you for trying", name)



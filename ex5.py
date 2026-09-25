colorlist = ["blue", "green", "white", "grey", "red", "yellow"]
color = input("What is your favorite color: ")
if color in colorlist:
    index = colorlist.index(color)
    print(f" Your favourite color is index {index} in the list.")
else:
    print("Sorry, i could not find your color.")

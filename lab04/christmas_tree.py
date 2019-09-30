# Programming exercise 2: Draw a Christmas Tree


def main():

    # Tree width question and restriction on 3 being the smallest value
    tree_width = int(input("How wide would you like the Christmas tree to be?\n"))
    while ((tree_width < 3) or ((tree_width % 2) == 0)):
        tree_width = int(input("Please enter an odd number that is atleast 3 or greater:\n"))

    # Defining other variables for constructing the tree:
    midpoint = tree_width // 2
    BLANKS = " "
    GROUND = "_"
    slant = (midpoint-1)
    tree_expanse = 1

    # Print Tree
    print("Here is your Christmas tree!\n")
    print(midpoint*BLANKS + "*" + midpoint*BLANKS)
    while slant > 0:
        print(slant*BLANKS + "/" + tree_expanse*BLANKS + "\\" + slant*BLANKS)
        slant -= 1
        tree_expanse += 2
    print(slant*BLANKS + "/" + tree_expanse*GROUND + "\\" + slant*BLANKS)

main()

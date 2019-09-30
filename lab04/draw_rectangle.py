# Programming exercise 1: Draw a rectangle


def main():

    # Program startup questtionare for symbol, width and height
    symbol_rec = input("What character should I make the rectangle in?\n")

    width_rec = int(input("What is the width of the rectangle?\n"))
    while width_rec < 2:
        width_rec = int(input("The width seems too low. Try another value:\n"))
    height_rec = int(input("What is the height of the rectangle?\n"))
    while height_rec < 2:
        height_rec = int(input("The height seems too low. Try another value:\n"))

    blanks = (width_rec - 2)

    # For loop for printing rectangle of the required spec
    print("\nHere is required rectangle:\n")
    for i in range(height_rec):
        if i == 0 or i == (height_rec-1):
            print(symbol_rec * width_rec)
        else:
            print(symbol_rec + blanks * " " + symbol_rec)

main()

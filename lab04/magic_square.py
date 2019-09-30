# Programming exercise 3: Identify magic square


def main():

    magic_row1 = input("Enter a magic number:\n")
    magic_row2 = input()
    magic_row3 = input()

    magic_sq = True
    dup_check = False

    # Duplicates check: first within same row then check within other rows
    if (magic_row1[0] is magic_row1[1]) or (magic_row1[1] is magic_row1[2]) or (magic_row1[0] is magic_row1[2]) is True:
        dup_check = True
    if (magic_row2[0] is magic_row2[1]) or (magic_row2[1] is magic_row2[2]) or (magic_row2[0] is magic_row2[2]) is True:
        dup_check = True
    if (magic_row2[0] is magic_row2[1]) or (magic_row2[1] is magic_row2[2]) or (magic_row2[0] is magic_row2[2]) is True:
        dup_check = True
    for i in [0, 2]:
        if magic_row1[i] in (magic_row2 or magic_row3):
            dup_check = True
        elif magic_row2[i] in (magic_row1 or magic_row3):
            dup_check = True
        elif magic_row3[i] in (magic_row1 or magic_row2):
            dup_check = True

    # Sum Totals check for rows, columns and diagonals in order
    if int(magic_row1[0]) + int(magic_row1[1]) + int(magic_row1[2]) != 15:
        magic_sq = False
    elif int(magic_row2[0]) + int(magic_row2[1]) + int(magic_row2[2]) != 15:
        magic_sq = False
    elif int(magic_row3[0]) + int(magic_row3[1]) + int(magic_row3[2]) != 15:
        magic_sq = False
    elif int(magic_row1[0]) + int(magic_row2[0]) + int(magic_row3[0]) != 15:
        magic_sq = False
    elif int(magic_row1[1]) + int(magic_row2[1]) + int(magic_row3[1]) != 15:
        magic_sq = False
    elif int(magic_row1[2]) + int(magic_row2[2]) + int(magic_row3[2]) != 15:
        magic_sq = False
    elif int(magic_row1[0]) + int(magic_row2[1]) + int(magic_row3[2]) != 15:
        magic_sq = False
    elif int(magic_row3[0]) + int(magic_row2[1]) + int(magic_row1[2]) != 15:
        magic_sq = False

    # Print relevant conclusions
    if dup_check is True:
        print("Duplicate numbers present \n")
    if (magic_sq is True) and (dup_check is False):
        print("This is a magic square!")
    else:
        print("Not a magic square!")

main()

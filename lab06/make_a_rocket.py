import sys


def main():
    try:
        width = int(sys.argv[1])
        block_count = int(sys.argv[2])

        if len(sys.argv) == 4:
            if sys.argv[3].lower() == "striped":
                striped = True
            else:
                print("Please try again!")
                return
        else:
            striped = False
    except ValueError:
        print("Invalid input")
        return

    cone_section(width)
    fuselage_section(width, block_count, striped)
    tail_section(width)


def cone_section(width):

    CONE_CHAR = "*"
    cone_width = 0
    if width % 2 == 0:
        cone_width = 2
    else:
        cone_width = 1
    while cone_width <= width:
        print((cone_width*CONE_CHAR).center(width))
        cone_width += 2


def fuselage_section(width, block_count, striped):
    FUSELAGE_CHAR = "x"
    FUSELAGE_STRIPE = "_"

    if striped is False:
        while block_count > 0:
            for i in range(width):
                print(width*FUSELAGE_CHAR)
                i -= 1
            block_count -= 1
    elif striped is True:
        if width % 2 == 0:
            while block_count > 0:
                for i in range(width//2):
                    print(width*FUSELAGE_STRIPE)
                    i -= 1
                for j in range(width//2):
                    print(width*FUSELAGE_CHAR)
                    j -= 1
                block_count -= 1
        elif width % 2 != 0:
            while block_count > 0:
                for i in range(width//2):
                    print(width*FUSELAGE_STRIPE)
                    i -= 1
                for j in range(width//2 + 1):
                    print(width*FUSELAGE_CHAR)
                    j -= 1
                block_count -= 1


def tail_section(width):
    TAIL_CHAR = "*"
    tailtip_width = (width // 2)
    if tailtip_width % 2 == 0 and width % 2 != 0:
        tailtip_width += 1
    elif tailtip_width % 2 != 0 and width % 2 == 0:
        tailtip_width += 1
    while tailtip_width <= width:
        print((tailtip_width*TAIL_CHAR).center(width))
        tailtip_width += 2
    print(((tailtip_width-2) * TAIL_CHAR).center(width))


main()

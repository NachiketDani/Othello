# Print cube program: prepared by Nachiket Dani


def main():
    correct_input = False

    while correct_input is False:
        cube_size = int(input("Input cube size (multiple of 2): "))
        if cube_size % 2 != 0 or cube_size < 2 or cube_size == 0:
            print("Invalid input!")
        else:
            correct_input = True
    cube_elements(cube_size)


def cube_elements(cube_size):
    CORNER_CROSS = "+"
    HORIZONTAL_EDGE = "-"
    BLANKS = " "
    VERTICAL_EDGE = "|"
    SIDE_HORIZONTAL_EDGE = "/"

    horizontals = 2 * cube_size
    side_horizontals = int(cube_size/2)
    blank_count_left = side_horizontals + 1
    blank_count_right = 0
    vertical_count = 0

    print(BLANKS * (blank_count_left) + CORNER_CROSS +
          (HORIZONTAL_EDGE * horizontals) + CORNER_CROSS)
    blank_count_left -= 1

    for i in range(side_horizontals):
        print(BLANKS * blank_count_left + SIDE_HORIZONTAL_EDGE +
              BLANKS * horizontals + SIDE_HORIZONTAL_EDGE +
              BLANKS * blank_count_right + VERTICAL_EDGE)
        blank_count_left -= 1
        blank_count_right += 1
        vertical_count += 1

    print(BLANKS * (blank_count_left) + CORNER_CROSS +
          HORIZONTAL_EDGE * horizontals + CORNER_CROSS +
          BLANKS * (blank_count_right) + VERTICAL_EDGE)
    vertical_count += 1

    for i in range(cube_size - vertical_count):
        print(VERTICAL_EDGE + BLANKS * horizontals + VERTICAL_EDGE
              + BLANKS * blank_count_right + VERTICAL_EDGE)

    print(VERTICAL_EDGE + BLANKS * horizontals + VERTICAL_EDGE +
          BLANKS * blank_count_right + CORNER_CROSS)

    for i in range(side_horizontals):
        print(VERTICAL_EDGE + BLANKS * horizontals + VERTICAL_EDGE
              + BLANKS * blank_count_right + SIDE_HORIZONTAL_EDGE)
        blank_count_right -= 1

    print(CORNER_CROSS +
          HORIZONTAL_EDGE * horizontals + CORNER_CROSS)


main()

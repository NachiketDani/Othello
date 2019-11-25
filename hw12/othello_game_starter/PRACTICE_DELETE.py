direction_list = [[7] * 3 for j in range(3)]
direction_list2 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
for row in direction_list:
    for column in direction_list:
        for items in direction_list2:
            direction_list[row][column] = direction_list[row - items[0]][column - items[1]] - 1

print(direction_list)

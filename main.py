import random


def main():
    """
    @Version 1.0.0
    print randomly Generated Axis With Grid Lines
    """
    cols = [str(i) for i in random.sample(list(range(0, 10)), 10)]
    rows = [str(i) for i in random.sample(list(range(0, 10)), 10)]
    grid_spots = []
    name_set = set()
    # Collect Grid Spot fill ins
    while len(grid_spots) < 100:
        print('Number of Boxes Remaining: '+str(100 - len(grid_spots)))
        person_name = input("Enter your Name (Format: FIRST LAST): ")
        num_blocks = int(input("Enter Number of Blocks: "))
        if num_blocks > 100 - len(grid_spots) or num_blocks <= 0:
            print(100 - len(grid_spots))
            print('You Entered too high of a value please redo entry (max = '+str(100-len(grid_spots))+')')
            continue
        if person_name in name_set:
            same_pers = input("Name found in entries :: Are you the same person (y/n): ")
            if same_pers != 'y':
                print("Same Name sorry you cant enter")
                continue
        else:
            name_set.add(person_name)
        name_list = [person_name]
        grid_spots.extend([person_name]*num_blocks)

    # Get largest first / last name
    box_width = get_largest_first_last(name_set)
    user_blocks = [str(i) for i in random.sample(grid_spots, 100)]
    col_label = '  | '+' | '.join( str(x).center(box_width) for x in cols)+' |'
    row_separator = create_between_rows_for_size(11, box_width)
    print(col_label)
    for i in range(0, 10):
        row_str = create_num_row_with_entries(rows[i], 11, user_blocks, i, box_width)
        print(row_separator)
        print(row_str)
    print(row_separator)


def create_number_row(row, num_cols):
    """
    Creates a column string for given column and number of rows
    :param row: row number as string
    :param num_cols: number of | to repeat for table
    :return: String to print for row
    """
    ret = row
    for x in range(num_cols):
        if x == 0:
            ret += ' |'
        else:
            ret += '   |'
    return ret


def create_num_row_with_entries(row, num_cols, user_spots, col_num, col_width):
    """
    Based on {create_number_rows} extended to inject peoples initials
    :param row: number assigned to row
    :param num_cols: number of | to repeat for table
    :param user_spots: entered users to inject into row
    :param col_num: column number in table
    :param col_width: center the string to this many characters
    :return: String to print for row
    """
    ret = row
    for x in range(num_cols):
        if x == 0:
            ret += ' |'
        else:
            ret += ' '+str(user_spots[(col_num-1)*10+x]).center(col_width)+' |'
    return ret


def create_between_row(num_cols):
    """
    Creates the seperator bewtween Rows
    :param num_cols: number of columns to separate
    :return: string for separator row
    """
    ret = ''
    for x in range(num_cols):
        if x == 0:
            ret += '--+'
        else:
            ret += '---+'
    return ret


def create_between_rows_for_size(num_cols, col_width):
    """
    Creates the seperator bewtween Rows
    :param num_cols: number of columns to separate
    :param col_width: number of dashes for names
    :return: string for separator row
    """
    ret = ''
    for x in range(num_cols):
        if x == 0:
            ret += '--+'
        else:
            ret += '-'+'-'*col_width+'-+'
    return ret


def get_largest_first_last(name_set):
    """
    Gets largest first or last name size for width of columns to print
    :param name_set:
    :return: int representing largest first or last name
    """
    size = max(len(x) for x in name_set)
    return size


if __name__ == '__main__':
    main()

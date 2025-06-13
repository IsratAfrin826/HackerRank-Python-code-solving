def print_door_mat(n, m):
    # Top part
    for i in range(n // 2):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(m, '-'))

    # Middle line
    print('WELCOME'.center(m, '-'))

    # Bottom part
    for i in range(n // 2 - 1, -1, -1):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(m, '-'))


# Input
if __name__ == '__main__':
    n, m = map(int, input().split())
    print_door_mat(n, m)
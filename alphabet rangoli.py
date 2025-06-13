import string

def print_rangoli(size):
    alpha = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    lines = []

    for i in range(size):
        # Generate left side: from outer to inner
        left = alpha[size-1:i:-1]
        # Add center and right side
        row = '-'.join(left + alpha[i:size])
        # Center the line based on full width
        lines.append(row.center(4 * size - 3, '-'))

    # Print the top half + middle + bottom half (reversed top)
    print('\n'.join(lines[::-1] + lines[1:]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
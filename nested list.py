if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])  # Store name-score pair

    # Get all unique scores, sort them, and find the second lowest
    scores = sorted(set(score for name, score in students))
    second_lowest = scores[1]

    # Collect names of students with the second lowest score
    second_lowest_names = [name for name, score in students if score == second_lowest]

    # Sort names alphabetically and print
    for name in sorted(second_lowest_names):
        print(name)

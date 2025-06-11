if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Remove duplicates
    unique_scores = set(arr)

    # Remove the highest score
    unique_scores.remove(max(unique_scores))

    # Find the next highest (runner-up)
    runner_up = max(unique_scores)

    print(runner_up)
def is_eligible_for_puzzle_hunt(N):
    return 6 <= N <= 8

# Input
N = int(input().strip())

# Output
if is_eligible_for_puzzle_hunt(N):
    print("Yes")
else:
    print("No")

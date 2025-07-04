A, B, C = map(int, input().split())
N = int(input())

max_score = 0

for _ in range(N):
    team_score = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        member_score = A * a + B * b + C * c
        team_score += member_score
    if team_score > max_score:
        max_score = team_score

print(max_score)
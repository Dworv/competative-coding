my_team = int(input())
finished = int(input())

scores = [None] + [0] * 4
games_left = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

for _ in range(finished):
    t1, t2, s1, s2 = (int(x) for x in input().split())
    if s1 > s2:
        scores[t1] += 3
    elif s2 > s1:
        scores[t2] += 3
    else:
        scores[t1] += 1
        scores[t2] += 1
    games_left.remove((t1, t2))

def possible_wins(games_left, scores):
    if len(games_left) > 0:
        wins = 0
        game = games_left.pop()
        # win
        win_scores = scores[:]
        win_scores[game[0]] += 3
        wins += possible_wins(games_left[:], win_scores)
        # tie
        tie_scores = scores[:]
        tie_scores[game[0]] += 1
        tie_scores[game[1]] += 1
        wins += possible_wins(games_left[:], tie_scores)
        # lose
        lose_scores = scores[:]
        lose_scores[game[1]] += 3
        wins += possible_wins(games_left[:], win_scores)
        return wins
    else:
        for i, score in enumerate(scores[1:]):
            if i + 1 != my_team and score >= scores[my_team]:
                return 0
        return 1

print(possible_wins(games_left, scores))
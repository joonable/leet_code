from heapq import heapify, heappop
from collections import defaultdict

def solution(genres, plays):
    total_plays = []
    genre_plays = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_plays[genre].append((-play, i))

    for genre, play_list in genre_plays.items():
        total = 0
        for play, i in play_list:
            total += play
        total_plays.append((total, genre))
        heapify(genre_plays[genre])
    heapify(total_plays)

    answer = []
    while total_plays:
        _, genre = heappop(total_plays)
        for i in range(2):
            if not genre_plays[genre]:
                break
            _, idx = heappop(genre_plays[genre])
            answer.append(idx)
    return answer
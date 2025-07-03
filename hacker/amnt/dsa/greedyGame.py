import heapq

def greedy_coin_game(piles):
    # Max heap (invert values for Python's min-heap)
    max_heap = [-pile for pile in piles]
    heapq.heapify(max_heap)

    a_score = 0
    b_score = 0
    turn = 0

    while max_heap:
        max_pile = -heapq.heappop(max_heap)  # Take the largest pile
        if turn % 2 == 0:
            a_score += max_pile
        else:
            b_score += max_pile
        turn += 1

    return a_score, b_score

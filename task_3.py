import heapq


def min_cost_to_connect_cables(cables):

    if len(cables) <= 1:
        return 0

    heapq.heapify(cables)
    
    total_cost = 0

    while len(cables) > 1:

        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost

if __name__ == "__main__":
    cables = [4, 2, 1]
    print(f"Початкові довжини кабелів: {cables}")
    
    min_cost = min_cost_to_connect_cables(cables)
    print(f"Мінімальні загальні витрати на з'єднання: {min_cost}")
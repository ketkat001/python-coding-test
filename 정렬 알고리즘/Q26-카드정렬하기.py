import heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))
result = 0

while cards:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    temp = a + b
    result += temp
    heapq.heappush(cards, temp)
print(result)

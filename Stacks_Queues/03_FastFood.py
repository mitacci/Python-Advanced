from collections import deque

total_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    curr_order = orders[0]

    if curr_order > total_food:
        break
    total_food -= curr_order
    orders.popleft()

if orders:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')
else:
    print('Orders complete')

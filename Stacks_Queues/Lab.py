# 01. Reverse Strings
string = input()
stack = []
for char in string:
    stack.append(char)

result = ''

while len(stack):
    result += stack.pop()

print(result)
# 02. Matching Parentheses
expression = input()

parrenthesis_indeces = []

for index, char in enumerate(expression):
    if char == '(':
        parrenthesis_indeces.append(index)
    elif char == ')':
        closing_index = index
        opening_index = parrenthesis_indeces.pop()
        print(expression[opening_index:closing_index + 1])

# 03. Supermarket
from collections import deque
queue = deque()

while True:
    command = input()
    if command == 'End':
        print(f'{len(queue)} people remaining.')
        break
    elif command == 'Paid':
        while queue:
            print(queue.pop())
    else:
        queue.appendleft(command)
# 04. Water Dispenser
from collections import deque

water_quantity = int(input())

people_queue = deque()

while True:
    command = input()
    if command == 'Start':
        break
    people_queue.appendleft(command)

while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill'):
        params = command.split(' ')
        liters_to_add = int(params[1])
        water_quantity += liters_to_add
    else:
        name = people_queue.pop()
        water_wanted = int(command)
        if water_wanted <= water_quantity:
            print(f'{name} got water')
            water_quantity -= water_wanted
        else:
            print(f'{name} must wait')
print(f'{water_quantity} liters left')

# 05. Hot Potato
from collections import deque

potatoes = input().split(' ')
potatoes_queue = deque()
for p in potatoes:
    potatoes_queue.appendleft(p)

step = int(input())

while potatoes_queue:
    for _ in range(step - 1):
        potatoes_queue.appendleft(potatoes_queue.pop())
    potato_to_remove = potatoes_queue.pop()

    if potatoes_queue:
        print(f'Removed {potato_to_remove}')
    else:
        print(f'Last is {potato_to_remove}')

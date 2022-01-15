# 01. Multiplication Function
def multiply(*args):
    if not args:
        return None
    product = 1
    for x in args:
        product *= x
    return product


# 02. Person Info
def get_info(name, age, town):
    return f'This is {name} from {town} and he is {age} years old'


# 03. Cheese Show
#TODO later
def sorting_cheeses(**kwargs):
    x = kwargs

    def eq(lst):
        res = False
        if len(lst) > 0:
            res = all(el == lst[0] for el in lst)
        return res

    return {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}


# 04. Character Combination
from itertools import permutations


def text_permutation(string):
    return list(permutations(string))


text = input()
[print("".join(el)) for el in text_permutation(text)]

# 05. Operate
from functools import reduce


def operate(operator, *args):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    product = reduce(operations.get(operator), args)

    return product


# 06. Chairs
from itertools import combinations


def chair_combinations(names, n_chairs):
    return combinations(names, n_chairs)


names = input().split(", ")
n = int(input())  # num of chairs
[print(*el, sep=", ") for el in chair_combinations(names, n)]


# 07. Expressions

def recur_expression(nums, current_sum=0, result=""):
    if not nums:
        return result, current_sum

    result_plus = recur_expression(nums[1:], current_sum + nums[0], f"{result}+{nums[0]}")
    result_minus = recur_expression(nums[1:], current_sum - nums[0], f"{result}-{nums[0]}")
    return result_plus + result_minus


def print_result(result):
    formatted_result = "\n".join(f'{result[i]}={result[i + 1]}' for i in range(0, len(result), 2))
    print(formatted_result)


nums = list(map(int, input().split(", ")))
result = recur_expression(nums)
print_result(result)

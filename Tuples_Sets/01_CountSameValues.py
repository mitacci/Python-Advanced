nums = (float(x) for x in input().split())
occ = {}

for num in nums:
    if num not in occ:
        occ[num] = 0
    occ[num] += 1
    
for k, v in occ.items():
    print(f"{k} - {v} times")

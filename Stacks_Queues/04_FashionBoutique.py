clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_racks = 1
curr_rack = rack_capacity

while clothes:
    curr_piece = clothes[-1]

    if curr_piece <= curr_rack:
        clothes.pop()
        curr_rack -= curr_piece
    else:
        used_racks += 1
        curr_rack = rack_capacity

print(used_racks)

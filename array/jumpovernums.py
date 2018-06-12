def jump_over_numbers(list):
    # Write your solution here
    idx = 0
    count = 0
    while idx < len(list):
        current = list[idx]
        if current == 0:
            return -1
        idx = idx + current
        count += 1
    return count

print jump_over_numbers([3,4,1,2,5,6,9,0,1,2,3,1])
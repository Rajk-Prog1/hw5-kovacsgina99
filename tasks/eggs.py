def eggs_solution(breaks): # sárkányos feladat logikája mentén
    low_floor = 0
    high_floor = 99

    while (low_floor + 1) <= high_floor:
        middle_floor = low_floor + high_floor // 2
        if breaks(middle_floor):
            high_floor = middle_floor - 1
        else:
            low_floor = middle_floor + 1
    
    return high_floor

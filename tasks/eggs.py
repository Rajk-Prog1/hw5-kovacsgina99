def eggs_solution(breaks): 
    low_floor = 0
    high_floor = 100

    while (low_floor + 10) <= high_floor: # 10-esével megyünk végig az emeleteken
        if breaks(low_floor + 10): # megvizsgáljuk, hogy afölött az emelet fölött vagyunk-e, ahol összetört az első tojás
            break # összetörik a tojás + megtörik a ciklus
        else:
            low_floor = low_floor + 10 # ha még nem tört össze, akkor feljebb visszük azt az emeletet, ameddig vizsgálunk
    while (low_floor + 1) <= high_floor: # egyesével nézzük meg az emeleteket:
        if breaks(low_floor + 1): # legmagasabb emelet, ahol még nem törik össze
            break # összetörik a tojás + megtörik a ciklus
        else: 
            low_floor = low_floor + 1

    return low_floor # legmagasabb szint, ahol még nem törik össze

    
        

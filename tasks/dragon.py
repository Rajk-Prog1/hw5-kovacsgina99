def dragon_solution(is_dead, number_of_cows):
    fat_alive_cow_index = 0
    thin_alive_cow_index = number_of_cows - 1
    
    while (fat_alive_cow_index + 1) <= thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index + thin_alive_cow_index) // 2)
        if is_dead(middle_cow):
            thin_alive_cow_index = middle_cow - 1
        else:
            fat_alive_cow_index = middle_cow + 1 
    
    return thin_alive_cow_index
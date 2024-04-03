def dragon_solution(is_dead, number_of_cows):
    fat_alive_cow_index = 0 # élő tehenek listájának az eleje
    thin_alive_cow_index = number_of_cows - 1 # élő tehenek listájának az utolsó eleme
    
    while (fat_alive_cow_index + 1) <= thin_alive_cow_index: # bináris keresés
        middle_cow = int((fat_alive_cow_index + thin_alive_cow_index) // 2) # a középső tehenet megkeressük
        if is_dead(middle_cow): # megnézzük, hogy a középső tehén halott-e
            thin_alive_cow_index = middle_cow - 1 # ha igen, akkor a vékonyabb tehenek oldalán folytatjuk a keresést
        else:
            fat_alive_cow_index = middle_cow + 1 # ha nem, akkor a ducibb tehenek oldalán folytatjuk a keresést
    
    return thin_alive_cow_index # visszaadja a legducibb élő tehenet 
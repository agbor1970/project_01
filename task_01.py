# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый 
#трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

my_list = list(my_favorite_songs.split(', '))
print(my_list[0], my_list[-1], my_list[1], my_list[-2])

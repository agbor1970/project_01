# Задача 3
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
import random 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

songs_sum  = 0

for num in range(3):
    a = random.randint(0, 8)
    songs_sum += int(my_favorite_songs[a][1] // 1 * 60) + int(round(my_favorite_songs[a][1] % 1 * 100, 0))

celoe = songs_sum // 60
ostatok = songs_sum % 60
if ostatok < 10:
    ostatok = str('0' + str(ostatok))
strin = str(celoe) + '.' + str(ostatok)
print('Три песни звучат ' + strin + ' минут')

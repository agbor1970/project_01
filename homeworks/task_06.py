# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


import random


my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
keys = list(my_favorite_songs.keys())
songs_sum = 0.0
for i in range(3):
    a = random.randint(0, len(keys)-1)
    songs_sum += int(round(float(my_favorite_songs.get(keys[a])) // 1 * 60, 0)) + int(round(float(my_favorite_songs.get(keys[a])) % 1 * 100, 0))
celoe = songs_sum // 60
ostatok = songs_sum % 60
if ostatok < 10:
    ostatok = str('0' + str(ostatok))
strin = str(celoe)[:-2] + '.' + str(ostatok)[:-2]

print (f'Три песни звучат {strin} минут.')
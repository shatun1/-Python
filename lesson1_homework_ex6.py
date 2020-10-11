a = 5
b = 9
day_number = 0
while a < b:
    if a < b:
        day_number += 1
    if day_number > 1:
        a = (a / 100 * 10) + a
    print(f'{day_number}-ый день - {a:.3f} километров')
    print(f'Ответ: на {day_number}-ый день спортсмен достиг результата не менее {b} километров')

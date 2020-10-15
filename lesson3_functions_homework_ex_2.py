def info(name, surname, year, town, email, phone_number):
    print(f'Имя - {name}, фамилия - {surname}, год рождения - {year}, город проживания - {town}, '
          f'электронная почта - {email}, номер телефона - {phone_number} ')


info(name=input("Введите имя :"), surname=input('Ведите фамилию :'), year=input('Введите год рождения :'),
     town=input('Введите город проживания :'), email=input('Введите вашу электронную почту'),
     phone_number=input('Введите ваш номер телефона'))

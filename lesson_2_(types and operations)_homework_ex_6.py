goods_number = int(input('Введите количество видов товара'))
n = 0
list_1 = []
list_1_2 = []
analys = []
while n < goods_number:
    n += 1
    list_1 = dict({'name': input('Введите имя товара :'), "цена": int(input("Введите цену товара :")),
                  "количество": int(input('Введите количество товара :')),
                  'единица измерения товара': input('Введите единицу измерения товара')})
    list_1_2.append((n, list_1))


    analys = dict({'имена': list_1.get('name'), 'цены': list_1.get('цена'),
                 'количества': list_1.get('количество'),
                 'единицы измерения товаров': list_1.get('единица измерения товара')})


    print(list_1)
    print(analys)
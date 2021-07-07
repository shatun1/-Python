goods = []
list_items = {'имя': '', 'цена': '', 'количество': '', 'единица измерения товара': ''}
analytics = {'имя': [], 'цена': [], 'количество': [], 'единица измерения товара': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', Для продолжения нажмите : 'Enter', для просмотра аналитики нажмите : 'F'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'F':
        print(f'\n Аналитика \n')
        for key, value in analytics.items():
            print(f'{key}: {value}')
    for f in list_items.keys():
        feature_ = input(f'Input feature "{f}"')
        list_items[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(list_items[f])
    goods.append((num, list_items))
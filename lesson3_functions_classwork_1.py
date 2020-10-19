# def my_sum(arg_1, arg_2):
#     return arg_1 + arg_2
#
#
# print(my_sum(10, 30))
# print(my_sum('Nik', 'ita'))
# def first_func(arg1_2):
#     def second_func(arg_2):
#         return arg1_2 + arg_2
#     return second_func
#
#
# func_3 = first_func(20123)
# print(func_3(23142))

# def calc():
#     try:
#         r_val = float(input('Введите числовое значение высоты : '))
#         h_val = float(input('Ведите числовое значение радиуса : '))
#     except ValueError:
#         return
#
#     s_side = 2 * 3.14 * r_val * h_val
#     s_circle = 3.14 * r_val ** 2
#     s_full = s_side + 2 * s_circle
#     return s_side, s_full
#
#
# v_side, v_full = calc()
# print(f'Площадь боковой поы-сти = {v_side}, полная площадь = {v_full}')


# def second_func(var_2, var_1, var_3):
#     print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_3}")
#
#
# second_func(var_1=10, var_2=20, var_3=30)


def second_func_1(var_2, var_1, var_3):
    print(f'var_2 - {var_2}, var_1 - {var_1}, var_3 - {var_3}')


second_func_1(var_1=10, var_2=20, var_3=30)
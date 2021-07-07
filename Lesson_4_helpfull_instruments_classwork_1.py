from sys import argv

script_name, work_in_hours, rate_per_hour, prize, currency = argv
work_in_hours,rate_per_hour, prize = int(work_in_hours), int(rate_per_hour), int(prize)
salary = int(work_in_hours * rate_per_hour) + prize
print(f'Ваша зарплата сотавляет : {salary} {currency}')

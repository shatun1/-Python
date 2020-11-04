import json
new_file = open('my_file_7.txt', 'r+', encoding='utf-8')
middle_profit_dict = {}
firm_profit = {}
firm_list = []
profit_list = []
for line in new_file:
    line = line.split()
    profit = int(line[2]) - int(line[3])
    if int(line[2]) > int(line[3]):
        profit_list.append(profit)
    firm_name = line[0]
    firm_profit.update({firm_name: profit})
middle_profit = sum(profit_list) / len(profit_list)
middle_profit_dict.update({'Middle Profit': middle_profit})
firm_list.append(middle_profit_dict)
firm_list.append(firm_profit)
j_son_list = json.dumps(firm_list)
print(j_son_list)
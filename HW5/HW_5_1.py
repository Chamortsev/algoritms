#  1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
#  (т.е. 4 отдельных числа) для каждого предприятия..
#  Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
#  чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

a = int(input('Введите количество предприятий: '))
result = []
all_middle = 0
for i in range(a):
    info = {}
    name = input(f'Введите наименование предприятия № {i+1}: ')
    profit = [i for i in input(f'Введите прибыть за 4 квартала по предприятию {name} (Формат ввода 1 2 3 4): ').split()]
    middle = (int(profit[0])+int(profit[1])+int(profit[2])+int(profit[3]))/4
    # print(middle)
    info["id"] = i+1
    info["name"] = name
    info["middle"] = middle
    # print(info)
    result.append(info)
for i in result:
    print(f'Среднее по компании {i["name"]} за 4 квартала {i["middle"]}')
    all_middle = all_middle + i["middle"]
all_middle = all_middle / a
print(f'Среднее по всем компаниям составляет {all_middle}')
res_min = []
res_max = []
for i in result:
    if all_middle > i["middle"]:
        res_min.append(i["name"])
    else:
        res_max.append(i["name"])
print(f'Предприятия у которых прибыль меньше среднего: ')
for i in res_min:
    print(i)

print(f'Предприятия у которых прибыль больше среднего: ')
for i in res_max:
    print(i)

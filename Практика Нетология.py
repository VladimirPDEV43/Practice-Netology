
# 1
# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя.
# Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

geo_tag = set()# Cоздаем пустое множество

for i in ids.values(): # возвращаем значения из словаря
       geo_tag = geo_tag.union(set(i)) # записываем в множество уникальные значения и объединяем в одно множество


print(geo_tag)





# 2
# Дана переменная, в которой хранится список поисковых запросов пользователя.
# Вам необходимо написать программу,
# которая выведет на экран распределение количества слов в запросах в требуемом виде.
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

list1 = []

for i in queries:
    list1.append(len(i.split())) # разделяем основную строку по разделителю и возвращаем список строк

a = 0
count = 1
while count <= max(list1): # пока count не = макс значению
    for j in range(len(list1)):
        if count == list1[j]: # если count = элементу из списка, то +1
            a += 1
    if a > 0:
        print('Поисковых запросов, содержащих', count, 'слов(а):', round(a*100/len(list1), 2))
    count += 1
    a = 0






# 3
# Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам.
# Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: ((revenue / cost) - 1) * 100

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

new_results = {}

for i, j in results.items(): # возвращает пары «ключ — объект» из results.
    new_results.update({i: {'revenue': j['revenue'], 'cost': j['cost'],
                             'ROI': round((j['revenue'] / j['cost'] - 1) * 100, 2)}})# обновить несколько пар

print(new_results)




# 4
# Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж.
# Напишите программу, которая возвращает название канала с максимальным объемом продаж.

stats = {
    'facebook': 55,
    'yandex': 115,
    'vk': 120,
    'google': 99,
    'email': 42,
    'ok': 98,
}

for i, j in stats.items():
    if j == max(stats.values()):
        print(f"Максимальный объем продаж на рекламном канале: {i} - {j}")

print(f"Максимальный объем продаж на рекламном канале: {max(iter(stats), key=lambda k: stats[k])}")



# 5
# Дан список произвольной длины.
# Необходимо написать код, который на основе исходного списка составит словарь такого уровня вложенности,
# какова длина исходного списка.

my_list1 = ['2018-01-01', 'yandex', 'cpc', 100]
my_list2 = ['a', 'b', 'c', 'd', 'e', 'f']

def func(list_):
    it = reversed(list_)
    d = next(it)
    for n in it:
        d = {n: d}
    return d


print(func(my_list1))
print(func(my_list2))




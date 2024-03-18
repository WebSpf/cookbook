from pprint import pp
cook_book = {}
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    name_dish = ''
    for some in file:
        some = some.strip()
        if some.isdigit():
            continue
        elif some and '|' not in some:
            cook_book[some] = []
            name_dish = some
        elif some and '|' in some:
            ingredient_name, quantity, measure = some.split(" | ")
            cook_book.get(name_dish).append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})

pp(cook_book)
print()


def get_shop_list_by_dishes(dishes_list, person_count):
    shop_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
                else:
                    shop_list[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 'quantity':
                                                                (ingredient['quantity'] * person_count)})
        else:
            pp('Такого блюда нет в книге')
    return shop_list


pp(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


with open('1.txt', 'r', encoding='utf-8') as file:
    line_1 = {}
    count = 0
    for line in file.readlines():
        count += 1
        line_1['1.txt'] = count

with open('1.txt', 'r', encoding='utf-8') as file:
    text_1 = file.read()

with open('2.txt', 'r', encoding='utf-8') as file:
    line_2 = {}
    count = 0
    for line in file.readlines():
        count += 1
        line_2['2.txt'] = count

with open('2.txt', 'r', encoding='utf-8') as file:
    text_2 = file.read()

with open('3.txt', 'r', encoding='utf-8') as file:
    line_3 = {}
    count = 0
    for line in file.readlines():
        count += 1
        line_3['3.txt'] = count
        
with open('3.txt', 'r', encoding='utf-8') as file:
    text_3 = file.read()

with open('resulting-file.txt', 'a', encoding='utf-8') as file_result:
    some_list = sorted(list(line_1.items()) + list(line_2.items()) + list(line_3.items()), key=lambda x: x[1])
    file_result.write(f'{some_list[0][0]}\n {some_list[0][1]}\n {text_2}\n {some_list[1][0]}\n {some_list[1][1]}\n {text_1}\n'
                          f'{some_list[2][0]}\n {some_list[2][1]}\n {text_3}\n')                                           
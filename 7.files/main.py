def nice_print(*args, tab=0, quot=False):
    for val in args:
        if isinstance(val, dict):
            nice_print('\t' * tab, '{', tab=tab)
            if val:
                tab += 1
                for el in val:
                    if isinstance(val[el], list):
                        nice_print('\n\t' * tab)
                    nice_print(el, quot=True)
                    nice_print(': ')
                    nice_print(val[el], quot=True)
                    nice_print(',')
                nice_print('\b')
                if isinstance(val[el], list):
                    nice_print('\n')
                tab -= 1
            nice_print('}', tab=tab)
        elif isinstance(val, list):
            nice_print('\t' * tab, '[\n', tab=tab)
            tab += 1
            for el in val[:-1]:
                nice_print('\t' * tab, el, ',\n', tab=tab)
            nice_print('\t' * tab, val[-1], '\n', tab=tab)
            nice_print('\t' * tab, ']')
        elif isinstance(val, str):
            if quot:
                print("'", sep="", end="")
            print(val, sep="", end="")
            if quot:
                print("'", sep="", end="")
        else:
            print(val, sep='', end="")


def read_dish(file):
    dish_name = file.readline()
    if not dish_name:
        return
    while dish_name == '\n':
        dish_name = file.readline()
        if not dish_name:
            return
    dish_name = dish_name.strip()
    ingredient_count = int(file.readline().strip())
    res = {dish_name: []}
    i = 0
    while i < ingredient_count:
        ingredient_name, quantity, measure = file.readline().split('|')
        res[dish_name].append({'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity),
                               'measure': measure.strip()})
        i += 1
    return res


cook_book = {}

with open('file.txt', 'r') as file:
    dish = read_dish(file)
    while dish:
        cook_book.update(dish)
        dish = read_dish(file)
    file.close()

nice_print('cook_book = ', cook_book)

import pprint


def create_cook_book():
    with open('recipes.txt', 'rt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish = line.strip()
            ingredients_count = int(f.readline())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_info = f.readline().strip().split(' | ')
                ingredient_name, quantity, measure = ingredient_info
                ingredients.append({'ingredient_name': ingredient_name,
                                    'quantity': quantity,
                                    'measure': measure})
            f.readline()
            cook_book.update({dish: ingredients})
    return cook_book


pprint.pprint(create_cook_book())
print()


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = \
                    {'measure': ingredient['measure'], 'quantity': 0}
            shop_list[ingredient['ingredient_name']]['quantity'] = \
            shop_list[ingredient['ingredient_name']]['quantity'] + \
            (int(ingredient['quantity'])) * person_count
    return shop_list


pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

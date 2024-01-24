with open('recipes.txt', 'r') as f:
    data = f.read().split('\n\n')
    cook_book = {}
    for food in data:
        key = food.split('\n')[0]
        values = food.split('\n')[2:]
        ingridients = []
        for value in values:
            value = value.split('|')
            ingridient = {}
            ingridient['ingredient_name'] = value[0]
            ingridient['quantity'] = value[1]
            ingridient['measure'] = value[2]
            ingridients.append(ingridient)

            cook_book[key] = ingridients
    
    def get_shop_list_by_dishes(dishes, person_count):
        cook_dishes = {}
        for dish in dishes:
            for ingredient in cook_book[dish]:
                dish_cook = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                if dish_cook not in cook_dishes:
                    cook_dishes[dish_cook] = {
                        "measure": measure,
                        "quantity": quantity
                    }
                else:
                    cook_dishes[dish_cook]['quantity'] += quantity
        return cook_dishes

print(cook_book)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
f.close
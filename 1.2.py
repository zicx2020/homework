def cook_list () :
     cook_book = {}
     with open('Книга_рецептов.txt') as f :
       for line in f :
           dish_name = line
           counter = int(f.readline())
           list_of_ingridient = []
           for i in range(counter):
               temp_dict= {}
               ingridient = f.readline()
               ingr = ingridient.split("|")
               keys = ['ingredient_name' , 'quantity' , 'measure']
               temp_dict[keys[0]] = ingr[0]
               temp_dict[keys[1]] = ingr[1]
               temp_dict[keys[2]] = ingr[2]
               list_of_ingridient.append(temp_dict)
               cook_book[dish_name] = list_of_ingridient
     return cook_book
cook_list()


def get_shop_list_by_dishes(dishes, person_count) :
    cook_book = {'Омлет\n': [{'ingredient_name': 'Яйцо ', 'quantity': ' 2 ', 'measure': ' шт\n'}, {'ingredient_name': 'Молоко ', 'quantity': ' 100 ', 'measure': ' мл\n'}, {'ingredient_name': 'Помидор ', 'quantity': ' 2 ', 'measure': ' шт\n'}], 'Утка по-пекински\n': [{'ingredient_name': 'Утка ', 'quantity': ' 1 ', 'measure': ' шт\n'}, {'ingredient_name': 'Вода ', 'quantity': ' 2 ', 'measure': ' л\n'}, {'ingredient_name': 'Мед ', 'quantity': ' 3 ', 'measure': ' ст.л\n'}, {'ingredient_name': 'Соевый соус ', 'quantity': ' 60 ', 'measure': ' мл\n'}], 'Запеченный картофель\n': [{'ingredient_name': 'Картофель ', 'quantity': ' 1 ', 'measure': ' кг\n'}, {'ingredient_name': 'Чеснок ', 'quantity': ' 3 ', 'measure': ' зубч\n'}, {'ingredient_name': 'Сыр гауда ', 'quantity': ' 100 ', 'measure': ' г\n'}], 'Фахитос\n': [{'ingredient_name': 'Говядина ', 'quantity': ' 500 ', 'measure': ' г\n'}, {'ingredient_name': 'Перец сладкий ', 'quantity': ' 1 ', 'measure': ' шт\n'}, {'ingredient_name': 'Лаваш ', 'quantity': ' 2 ', 'measure': ' шт\n'}, {'ingredient_name': 'Винный уксус ', 'quantity': ' 1 ', 'measure': ' ст.л\n'}, {'ingredient_name': 'Помидор ', 'quantity': ' 2 ', 'measure': ' шт.\n'}]}
    ingridients = {}
    ingr = []
    keys = []
    value = []
    for key , values in cook_book.items() :
       if key.split('\n')[0] == dishes[0] :
           x = cook_book[key]
           for v in x :
             ingr.append(v)
       elif key.split('\n')[0] == dishes[1] :
           x = cook_book[key]
           for v in x:
               ingr.append(v)
    for  ins in ingr :
      valuee = {}
      x = str(ins.get('ingredient_name'))
      keys.append(x)
      a = ins.get('measure')
      z = ins.get('quantity')
      valuee['measure'] = a
      valuee['quantity'] = int(z) * person_count
      value.append(valuee)
    x = 0

    for k in keys:
        ingridients[k] = value[x]
        x = x + 1

    print(ingridients)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4)


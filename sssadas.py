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
    cook_book = cook_list()
    spisok = []
    for key,values in cook_book.items() :
      for din in dishes :
        if key.split('\n')[0] == din :
            spisok.append(values)
    for s in spisok :
        for a in s :
            a['quantity'] =int(a['quantity']) * person_count
    print(spisok)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4)

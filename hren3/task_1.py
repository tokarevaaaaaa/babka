# TODO Напишите функцию для поиска индекса товара

def count (product, items_list):
    i = 0
    lenght = len (items_list)
    while (i < lenght):
        if (items_list[i] == product):
            return i
        i+=1
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = count (find_item, items_list)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

'''Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
[1, 2, 3, 1, 2] -> [1, 2]'''

my_list = [1, 2, 3, 1, 2]
for i in set(my_list):
    if my_list.count(i) == 1:
        my_list.remove(i)

print(list(set(my_list)))
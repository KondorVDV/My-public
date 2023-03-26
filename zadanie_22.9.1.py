def sort_increase(c):  # определяем функцию сортировки списка по возрастанию

    for i in range(len(c)):
        for j in range(len(c) - i - 1):
            if c[j] > c[j + 1]:
                c[j], c[j + 1] = c[j + 1], c[j]

    return (c)


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] < element <= array[middle + 1]:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


a = input('Введите последовательность чисел через пробел: ')

print('*********************************************************************************************************')


element = int(input('Введите любое число: '))

print('*********************************************************************************************************')


input('Нажмите "Enter" для преобразования введенной последовательности в список целых чисел:')
a_list = a.split() # преобразовываем последовательность в список
a_list_int = [int(a) for a in a_list] # преобразовываем последовательность в список целых чисел
print(a_list_int)

print('*********************************************************************************************************')


input('Нажмите "Enter" для сортировки списка по возрастанию:')
sort_increase(a_list_int) # вызываем функцию для сортировки по возрастанию
print(a_list_int)

print('*********************************************************************************************************')


input('Нажмите "Enter" для проверки условий задания:')
i = int(binary_search(a_list_int, element, 0, len(a_list_int)))

if a_list_int[i] < element <= a_list_int[i + 1]:
    print('Число',a_list_int[i],' с номером позиции:', i,'меньше введенного числа',element,', а следующее за ним:',
          a_list_int[i + 1], ', больше , либо равно этому числу.')
    print('Условия выполнены!!!')
else:
    print('Введенное число не соответствует заданному условию!!!')



person =int(input("Какое количество билетов вы планируете приобрести?:")) # запрашиваем количество приобретаемых билетов
print('---------------------------------------')
cost = 0 # ввводим переменную стоимости билета каждого поситителя
cost_sum = 0 # вводим переменную общей стоимости билетов

for i in range(1, person + 1):     # вводим цикл для подсчета стоимости билетов в соответствии с возрастом поситителей
    print('Введите возраст',i,'-го поситителя:')
    age_person = int(input())
    if age_person >= 0 and age_person <18:
        cost = 0
    elif age_person >= 18 and age_person < 25:
        cost = 990
    else:
        cost = 1390
    cost_sum = cost + cost_sum # Подсчитываем общую стоимость билетов

    print('Стоимость билета',i,'-го поситителя:',cost,'руб.')
    print('---------------------------------------')

if person > 3:          # подсчитываем цену со скидкой если билетов больше 3-х
    cost_sum = cost_sum - cost_sum/100*10
    print('---------------------------------------')
    print("Общая стоимость билетов с учетом скидки:",round(cost_sum),'руб.')
else:
    print("Общая стоимость билетов:", cost_sum, 'руб.')






# У вас есть данные о загрузке сервера в трёх разных часах: hour1, hour2, hour3. Загрузка измеряется в процентах. Напишите программу, которая:
#
#     Выводит "Стабильная нагрузка", если разница между самой высокой и самой низкой загрузкой не превышает 10%.
#     Выводит "Нестабильная нагрузка" и предупреждение "Отклонение от нормы", если разница между самой высокой и самой низкой загрузкой превышает 10%.
#     Если в какой-то из часов нагрузка превышает 90%, выводит "Перегрузка в часы пик".

hour_1, hour_2, hour_3 = int(input()), int(input()), int(input())

load = max([hour_1, hour_2, hour_3]) - min([hour_1, hour_2, hour_3])
load_90 = max([hour_1, hour_2, hour_3]) > 90

if load <= 10:
    print("Стабильная нагрузка")
elif load > 10 and load_90 is True:
    print("Нестабильная нагрузка\nОтклонение от нормы\nПерегрузка в часы пик")
elif load > 10:
    print("Нестабильная нагрузка\nОтклонение от нормы")
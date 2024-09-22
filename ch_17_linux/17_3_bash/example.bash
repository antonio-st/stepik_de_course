Примеры объявлений переменных:

name="John" 
age=30 
greeting="Hello, $name"



# Типы кавычек

# Одинарные кавычки (' '): Содержимое внутри одинарных кавычек трактуется как буквальный текст, без интерпретации специальных символов и переменных.
# Пример:

single_quote='This is $name' 
echo $single_quote # Выведет: This is $name

# двойные 
double_quote="Hello, $name" 
echo $double_quote # Выведет: Hello, John


# переменные

# локальные

age = 30 
echo "You age = $age"

# глобальные

export global_var="I am global" 
bash -c 'echo $global_var' # Выведет: I am global


# Чтение значений переменных из ввода
#!/bin/bash
echo "You name: "
read user_name
echo "Hello, $user_name from bash"


# Специальные переменные
# 
# Bash имеет ряд встроенных специальных переменных, которые предоставляют информацию о состоянии скрипта или окружения.

    $0 : Имя текущего скрипта.
    $1, $2, ... : Параметры, переданные в скрипт.
    $# : Количество аргументов, переданных в скрипт.
    $@ : Все аргументы, переданные в скрипт.
    $? : Статус завершения последней выполненной команды.
    $$ : PID текущего процесса.
    $! : PID последнего запущенного в фоне процесса.
    
    
#     Арифметические операции
# 
# Для выполнения арифметических операций используется команда let, конструкция $(( )) или команда expr.


a=10 
b=5 

# Использование let 
let sum=a+b 
echo $sum # Выведет: 15 

# Использование $(( )) 
sum=$((a + b)) 
echo $sum # Выведет: 15 

# Использование expr 
sum=$(expr $a + $b) 
echo $sum # Выведет: 15



# Строковые операции


# Конкатенация строк 
str1="Hello" 
str2="World" 
greeting="$str1, $str2!" 
echo $greeting # Выведет: Hello, World! 

# Длина строки 
str="Hello, World!" 
echo ${#str} # Выведет: 13


Пример скрипта с использованием переменных:

#!/bin/bash 
# Объявление переменных 
name="Alice" 
age=25 

# Вывод значений переменных 
echo "Name: $name" 
echo "Age: $age" 

# Арифметическая операция 
year_of_birth=$((2024 - age)) 
echo "Year of birth: $year_of_birth" 

# Чтение значения переменной из ввода 
echo "Enter your favorite color:" 
read color 
echo "Your favorite color is $color" 

# Использование специальной переменной 
echo "Script name: $0"


# Условные операторы в Bash

    -eq: равно
    -ne: не равно
    -lt: меньше
    -le: меньше или равно
    -gt: больше
    -ge: больше или равно
    
    
#     Операторы сравнения для строк

    =: равно
    !=: не равно
    -z: пустая строка
    -n: непустая строка
    
# Логические операторы

    &&: логическое "и"
    ||: логическое "или"



#!/bin/bash
echo "start script $0"
echo "read number-> "
read input_num

if [ $input_num -gt 10 ]; then
        echo "number is greater 10"
else
        echo "number is less than or equal to 10"
fi


#!/bin/bash
echo "start script $0"
echo "read number-> "
read input_num

if [ $input_num -gt 0 ] && [ $input_num -le 20 ]; then
        echo "number is between 0 and 20 inclusive"
elif [ $input_num -lt 0 ]; then
        echo "The value is less than zero"
else
        echo "number is greater than 20"
fi


# case

#!/bin/bash
echo "start script $0"
echo "read color-> "
read input_color

case $input_color in
                "red")
                        echo "Color is red" ;;
                "blue")
                        echo "Color is blue" ;;
                "green")
                        echo "Color is green" ;;
                *)
                        echo "Color is unknown!" ;;
esac 


# Пример использования case для обработки аргументов:

#!/bin/bash

echo "Enter a choice (start/stop/restart):"
read choice

case $choice in
    "start")
        echo "Starting the service..."
        # команды для старта сервиса
        ;;
    "stop")
        echo "Stopping the service..."
        # команды для остановки сервиса
        ;;
    "restart")
        echo "Restarting the service..."
        # команды для перезапуска сервиса
        ;;
    *)
        echo "Invalid choice"
        ;;
esac


# 
# Использование if с командами
# 
# В Bash можно использовать результат выполнения команды в условных операторах.
# 
# Пример:

if ls /some/directory; then
    echo "Directory exists"
else
    echo "Directory does not exist"
fi

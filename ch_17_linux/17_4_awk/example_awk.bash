# AWK — это язык программирования и утилита для обработки текстовых данных в Unix-подобных системах. Он позволяет выполнять сложные операции по обработке строк и файлов на основе шаблонов и условий. Основные области применения AWK включают анализ логов, обработку CSV-файлов, генерацию отчетов и многое другое.
# Основы AWK
# 
# Программа AWK состоит из набора шаблонов и действий. Основная структура выглядит так:
# 
# pattern { action }
# 
#     pattern (шаблон) определяет, какие строки обрабатываются.
#     action (действие) определяет, что делать с этими строками.



echo -e "John 28\nJane 32\nTom 25\nAlice 29" | awk '{ print $1 }'
John
Jane
Tom
Alice

cat name.txt
John 28
Jane 32
Tom 25
Alice 29
Lucy 40


cat name.txt | awk '$2 > 30 { print $0 }'
Jane 32
Lucy 40


# сумма
cat name.txt | awk '{ sum += $2 } END { print sum }'
154

# красивый вывод

cat name.txt | awk '{ printf "%s is %d years old\n", $1, $2 }'
John is 28 years old
Jane is 32 years old
Tom is 25 years old
Alice is 29 years old
Lucy is 40 years old


# подсчет в массиве

cat fruit.txt 
apple
banana
apple
orange
banana
banana


cat fruit.txt | awk '{ count[$1]++ } END  { for (i in count) print i, count[i] }'

banana 3
orange 1
apple 2

# можно запускать со скрипта awk -f script.awk

function sqr(x) {
        return x * x
}

BEGIN {
print "Enter number:"
getline name
printf "Square of %s is %d\n", name, sqr(name)
}

Enter number:
100000
Square of 100000 is 2147483647

# Управляющие структуры

awk -f script2.awk 20000

function sqr(x) {
        return x * x
}

BEGIN {
        if (ARGC != 2){
          print "Передано неверное количество аргументов"
          print "Используйте следующий шаблон:"
          print "awk -f script.awk number"
        }
else{
print "Число", ARGV[1], "в квадрате =", sqr(ARGV[1])
   }
}









ssh remote_username@remote_host

# копировать файл с сервера
$ scp опции пользователь1@хост1:файл пользователь2@хост2:файл
 scp -r /home/sergiy/photos/* root@losst.pro:/root/

ctrl + l # clear
ctrl + f2-f6 # консольный режим

:wq
:wq - название файла
:wq! # записать даже в файл с read only
:q! # выйти без сохранения

# логи
var/log

sudo cat /var/log/syslog | grep ???

# папка с шаблонами для создания дирректории юзера
/etc/skel

# системный лог ОС в опер памяти
sudo dmesg

# папка с пользователем
cat /etc/passwd | grep antonio

# зашифрованные пароли пользователе
sudo cat /etc/shadow

# группы пользователей
cat /etc/group

# сменить юзера
su <user> -> <pass>

# история входа в систему
sudo last

# номера групп где находиться юзер
id

# кто в системе
who
w

# Системный bashrc. Этот файл выполняется для каждого пользователя, 
# каждый раз когда он создает новую терминальную сессию.
cat /etc/bash.bashrc
добавить в файл: 
alias l="/home/antonio/#LEARN/"


Команда xargs объединяет зафиксированный набор заданных в командной строке начальных аргументов с 
аргументами, прочитанными со стандартного ввода, и выполняет 
указанную команду один или несколько раз. 
xargs

# запустить предыдущую команду с sudo
!! 


# работа с содержимым файла по шаблону
sed 
# вывести строчки с 5 по 10
sed '5,10p' /etc/group

# установка времени
sudo date --set "2023-06-08 11:20:00"

============================================================
# Общие команды

# размер папки
du -hs pgdata

# вернуться к процессу ping если остановили с помощью CTRL + Z 
fg ping

# locate, whereis местоположение команды
locate uptime
whereis uptime

# куда установлена программа
whereis hardinfo 


# показывает, что делает команда 
whatis uptime

# найти все команды с упоминанием uptime
man -k uptime

# инфо о процессоре
lscpu

# инфо о процессе
systemctl status docker.service


# инфо о системе , пользователе, ядре и тд(кратко)
uname -a

# тек время , пользователи, время работы системы
uptime

# список процессов в терминале
ps

# сменить дирректорию
cd

# на предыдущую дирректорию
cd -

# файлы, l - длинный формат, a - скрытые , S - по размеру, t - повремени
ls -la 


# где я 
pwd

# корневая дирректория
/ 

# домашняя
~

# текущая дирректория
.

# директория на шаг назад (../..) - 2 шага
..

# просмотреть большой текст
more text_file

# просмотр и поиск в файле , по '/' поиск
less text_file

# создать текстовый файл, если существует обновиться время создания(обновление работает и с папкой)
touch text_file

# копирование на рабочий стол
cp test.txt ~/'Рабочий стол'

# копирование всех файлов в папку Dir_1 / -v показывает процесс копирования
cp *.* Dir_1

# копирование файла по маске (?) в каталог на уровень выше
cp -v test_? ../Dir_1

# удалить все фаайлы в Dir_2
rm Dir_2/*

# копировать все файлы с Dir_1 в новую дирректорию
cp -Rv Dir_1 newdir

# создать дирректории Dir3 в ней Dir3x
mkdir -p Dir3/Dir3x

# создать папку , без -p во вложенной папке папку не создать
mkdir Dir3

# удалить пустую дирректорию
rmdir test/


# удалить непустой каталог
rm -R test_2/
rm -rf test_2/

# переименовать файл
mv newdir newdir_x


# перенести newdir_x в Dir3/
mv newdir_x/ Dir3/

# ссылка на папку /Dir_1
ln -s $(pwd)'/Dir_1' ~/'Рабочий стол'

# дубль файла с автообновлением
ln test.txt test_dubl.txt

# ПОИСК : по имени
find / -name "learn"

# ПОИСК : по расширению
find / -name "*.doc"

# выдает кол-во строчек / слов / размер в байтах
wc test_git.txt 
>>  81  472 5049 test_git.txt

# сортирует числа
sort randnum.txt


# выделяет текст, разделить по разделителю ">", далее взять 3 элемент
cut -d ">" -f 3 filesdelim.txt

1993>USA>linux
1995>South America>RedHat
1996>GB>Solyaris
>> linux
>> RedHat
>> Solyaris

# запустить с последующей сортировкой вывода: | sort
cut -d ">" -f 3 filesdelim.txt | sort

# выведет с 1 по 3 строчки разделенные :
cut -d ":" -f 1-3 /etc/passwd



# поиск по файлам слово linux, -i игнорировать заглавн/строчн.
grep -i linux ./*

# найти .gov в файле linux-history.txt 
grep .gov linux-history.txt


# регулярные выражения

[A-Za-z] 
[A-Z]* любое слово из больших букв
[0-9]* числа подряд
www\.[a-z]*\.com - web адрес

* - любой символ, любое количество;
\+ - как звездочка, только один символ или больше;
\? - нет или один символ;
\{i\} - любой символ в количестве i;
\{i,j\} - любой символ в количестве от i до j;
\{i,\} - любой символ в количестве от i и больше.


# найти или Fedora или Linux
grep -E " Fedora|Linux" linux.txt 


# ПОТОКИ ВВОДА ВЫВОДА ЗАПИСЬ В ФАЙЛ
# сохранит в файл отсортированный список из чисел (-n)
sort -n randnum.txt > new.txt

# добавит имена в конец файла
sort names.txt >>new.txt

# отсортировать и перезаписать файл
sort -n numb_2.txt >> numb_2.txt

# направить поток ошибок в файл
grep antonio /etc/* 2> err.txt

# вывести 1 поток без ошибок
grep antonio /etc/* >good.txt

# вывести все потоки в файл
grep antonio /etc/* &> all.txt^



=========================================================
# ПРАВА ПОЛЬЗОВАТЕЛЕЙ

# зайти под root
sudo su - root


# создание юзера
sudo useradd -m userguest

# задать пароль юзеру
sudo passwd userguest

# удалить пользователя вместе с папкойсв
sudo userdel -r <user> 

# добавить группу
sudo groupadd programer

# удалить группу
sudo groupdel programer

# добавить юзера в группу programer
sudo usermod -aG programer userguest


# добавить юзера в группу sudo
sudo usermod -aG sudo userguest

# удалить юзера из группы
sudo deluser userguest programer

u -user
g - group
o - other
a - ugo (все вместе)
ugo+x - добавить X всем
g-rw - убрать rw у группы
o=rw - установить rw всем остальным


-rw-rw-r-- 1 antonio   programer
-rw группа пользователь, его доступ
-rw - доступ группы к файлу
-r группа other
antonio - владелец файла(owner)
programer - группа имеющая доступ к файлу, их права -rw


# сменить владельца папки
sudo chown userguest Dir_1

# сменить группу пользователей на доступе к файлу
sudo chgrp programer ../err.txt
-rw-rw-r-- 1 antonio   programer   7447 июн  6 11:37 err.txt

# группе other добавить(o+w) права на изменение
chmod o+w test_git.txt 
-rw-rw-rw- 1 antonio   antonio     5049 июн  5 23:06 test_git.txt

# у группы other забрать права на чтение
chmod o-r good.txt
-rw-rw---- 1 antonio   antonio     1244 июн  6 11:43 good.txt


# у группы programer забрали права на запись файла
chmod g-w err.txt
-rw-r--r-- 1 antonio   programer   7447 июн  6 11:37 err.txt


# у юзера забрали права на запись файла
sudo chmod u-w linux.txt
-r--rw-r-- 1 userguest antonio     1701 июн  6 10:00 linux.txt


# защита от затирания файлов в каталоге, даже если на файл нет доступа
sudo chmod o+t Dir_1
drwxr-xr-t 2 userguest antonio     4096 июн  6 21:25 Dir_1
# аналог числами
sudo chmod 1777 Dir_1
# выкл
sudo chmod 1777 Dir_1



=================================================================
# Сеть

# ip адрес, устройства
ifconfig
ip addr show

# 
route -ven
ip route show

# 
ping -c 4 8.8.8.8 

# узлы через которые проходят пакеты
traceroute 77.88.55.242

# ip адрес сайта и хосты
host beeline.ru
dig beeline.ru

# сетевые подключения
netstat

sudo apt install openssh-server


=================================================================
# crone

crontab -e
# каждую минуту будет добавлятьчя в конец файлы потом echo
# вывод каждый день 23:05

# m  h  day month dow

  *  *   *    *    *   echo "Hi, its cron" >> ~/#LEARN/school_de/02_linux/scripts/cron_log.log

05 23 * * * echo "$(date) Hi, its me again" >> ~/#LEARN/school_de/02_linux/scripts/cron_log_2.log

# системные логи cron
sudo cat /var/log/syslog | grep CRON



==============================================================
# АРХИВАЦИЯ

#tar

# создание архива без компрессии f должна быть в конце, v - просмотрт процесса
tar cf mytar_dir_1.tar Dir_1

# посмотреть что в архивее
tar tf mytar_dir_1.tar 

# распаковать архив
tar xf mytar_dir_1.tar 

# tar c компрессией gzip 
tar cvf my_tar_GZIP.gz Dir_1

# распаковать 
tar xf my_tr_GZIP.gz

# tar c компрессией bzip
tar cjf my_tar_BZIP.bz2 Dir_1

# tar c компрессией xz
tar cJf my_tar_XZ.xz Dir_1


# gzip (только один файл)

# упаковать в файл
gzip -v mytar_dir_1.tar

# bzip2

# упаковать файл
bzip2 -v mytar_dir_1.tar

# распаковать файл
bunzip2 -v mytar_dir_1.tar.bz2


# xz

# упаковать файл
xz -v mytar_dir_1.tar


# распаковать файл
unxz -v mytar_dir_1.tar.xz


#zip

# упаковать файл
zip -r my_ZIP.zip Dir_1

# распаковать файл
unzip my_ZIP.zip
=====================================================================

# ПРОЦЕССЫ И ПАМЯТЬ

# диспетчер, ctrl + m, ctrl + p - сортировка
top


# инфо о памяти
free -h

============================================================

# Программы, установки

# скачать файл
wget http://stavexperts.h1n.ru/wp-content/uploads/2018/11/logoSE2.png


sudo apt-get install <package>
sudo apt-get remove <package>

# репозитарии
cat /etc/apt/sources.list

# установка загруженного пакета вручную
sudo dpkg -i <package.deb>

# удаление программы
sudo dpkg -r <название программы(не пакета)>


### cent os / red RedHat

sudo yum install <package>
sudo yum remove <package>

# пакеты называются .rpm
# скачиваем пакет wget

# установка
rpm -i <package.rpm>

# удаление пакета
sudo rpm -e nethack


sudo reboot now
sudo shutdown nowxter


=========================================================
# Написание скриптов
.sh

# начало скрипта
#!/bin/bash



# запуск
./script.sh

# перед запуском установить права на x
# например 
chmod ug=rwx file.sh

или # всем a добавить x 
chmod a+x file.sh

# вывести в переменную значение команды
myos=`uname -a`

# вывод переменной
echo "My operation system is $myos"

# вывод суммы
summa=$((num_1+num_2))

# вывод на одной строке
echo -n "text.."
echo "text_next"

$0 - имя файла
# - переменные переданные при запуске скрипта
$1, $2 


# if
if [ "$1" == "Vasya" ]; then
        echo "Hi, $1"
elif [ "$1" == "Anton" ]; then
        echo "Hi, $1 my owner"
else echo "Hello $1"
fi

# чтение введенного числа в переменную
read -p "Enter something $ " x


# case
echo "================================="
echo "CASE selection...."

case $x in
        1) echo "this one";;
        [2-9]) echo "two-nine";;
        "Petya") echo "Privet $x";;
        *) echo "unknown parameter!"
esac

# WHILE

COUNTER=0
echo "Starting WHILE"
while [ $COUNTER -lt 10 ]; do
        sleep 1
        echo "Current counter is $COUNTER"
        let COUNTER+=1
        #let COUNTER=COUNTER+1
        #COUNTER=$(($COUNTER+1))
done

# for
for myfile in `ls *.txt`; do
        cat $myfile >> myfile
done

# for 2
for x in {1..10}; do
        echo "X = $x"
        echo "X = $x" >> myfile
done

# for 3
for ((i=1; i<=10; i++)); do
        echo "I = $i"
        echo "I = $i" >> myfile
done

# Функции
myFunc()
{
        echo "It text from function"
        echo "Num_1 = $1"
        echo "Num_2 = $2"
        summa=$(($1+$2))
}

myFunc 50 30
echo "Summa = $summa"


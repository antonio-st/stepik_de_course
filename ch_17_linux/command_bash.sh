 # с добавлением в конец
 cat >> ./DE_course/file_num2.txt
 
 # без добавления в конец
 cat >> ./DE_course/file_num2.txt
 
 # ctrl + d выход
 
 # printf похож на echo, но более гибкий, так как позволяет форматировать текст.
 printf "first string\nSecond string\n" >> ./DE_course/new_text_file.txt
 
 # генерация случайных данных(строк)
 seq 1 20 >> DE_course/new_text_file.txt
 
 
 # чтение первых/последних строк в файле
 head -n 12 ./DE_course/new_text_file.txt
 tail -n 10 ./DE_course/new_text_file.txt
 
 # архивация
tar -czvf archive.tar.gz DE_course/
tar -xzvf archive.tar.gz

zip -r arhive.zip DE_course/
unzip arhive.zip

# размер файла / папки
du -h arhive.zip

# свободная RAM
free -h

# аналог диспетчера задач в Windows
ps aux

# процессы
top
# не получается выйти после этой команды? Нажмите комбинацию клавиш ctrl+C и Вы вернетесь в терминал.

# убийство процессов
kill уникальный номер процесса (PID)

# поиск файлов
find /home/akbogdanov -name "*.txt"

# расположение программы
whereis cat
cat: /usr/bin/cat /usr/share/man/man1/cat.1.gz /usr/share/man/man1p/cat.1p.gz

# инфо о домене 
dig ya.ru

ctrl + w # удалить пред слово
ctrl + u # удалить строку





 
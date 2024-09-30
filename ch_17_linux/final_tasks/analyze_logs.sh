: > report.txt
path="report.txt"
echo "Отчет о логе веб-сервера" >> $path 
echo "========================" >> $path  
echo -e "Общее количество запросов: " $(awk 'END{print NR}' access.log) >> $path 
echo -e "Количество уникальных IP адресов: " $(cat access.log | awk -F ' ' '{print $1}' |sort |uniq | awk 'END{print NR}') >> $path 
echo "" >> $path
echo "Количество запросов по методам:" >> $path 
cat access.log | awk -F '"' '{print $2}' | awk -F ' ' '{ count[$1]++ } END { for (word in count) print count[word], word }' >> $path 
echo "" >> $path
echo -e "Самый популярный URL: " $(cat access.log | awk -F ' ' '{print $7}' | awk '{ count[$1]++ } END { for (word in count) print count[word], word }' | sort -r | head -n 1) >> $path 

echo -e "Отчет сохранен в файл, $path"

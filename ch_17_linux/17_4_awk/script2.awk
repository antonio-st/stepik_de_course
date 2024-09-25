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

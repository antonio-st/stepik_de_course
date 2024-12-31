BEGIN {
    if (ARGC != 2) {
        print "Передано неверное количество аргументов"
        print "Используйте следующий шаблон:"
        print "awk -f script.awk number"
        exit 1
    }
    N = ARGV[1]
    i = 1
    while (i <= N) {
        print i
        i++
    }
}

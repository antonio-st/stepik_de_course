{
	for (i = 1; i <= NF; i++) {
	  print "Строка", NR, "слово под номером", i, "это", $1
	}
}
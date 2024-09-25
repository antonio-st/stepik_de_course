function sqr(x) {
	return x * x
}

BEGIN {
print "Enter number:"
getline name
printf "Square of %s is %d\n", name, sqr(name)
}

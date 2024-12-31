process_student() {
    echo "$1" | awk -F', ' '
}

BEGIN {
print process_student("John Doe, 90")
print "end"
}

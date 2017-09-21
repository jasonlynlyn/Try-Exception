try:
	v = int(raw_input("enter a number: "))

	if v>60:
		print "too old!"
	else:
		print "still young!"
except ValueError:
	print "wrong number"

bread = 1
PB = 1
jelly = 4

sandwiches = min(bread / 2, PB, jelly)

print sandwiches

if bread >= 2 and PB >= 1 and jelly >= 1 and bread % 2 == 1 and (PB > sandwiches or jelly > sandwiches):
	print "I can make this many sandwiches:", sandwiches, "but I can also make an open-face sandwich."
elif bread >= 2 and PB >= 1 and jelly >= 1:
	print "I can make this many sandwiches:", sandwiches
elif bread < 2 and PB < 1 and jelly < 1:
	print "I won't be eating a PB&J sandwich today beacuse I am missing all of the ingredients for a PB&J"
elif bread < 2 and PB < 1:
	print "I am missing bread and PB"
elif bread < 2 and jelly < 1:
	print "I am missing bread and jelly"
elif PB < 1 and jelly < 1:
	print "I am missing PB and jelly"
elif bread < 2:
	print "I am missing bread"
elif PB < 1:
	print "I am missing PB"
else:
	print "I am missing jelly"



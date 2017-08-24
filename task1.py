print "Enter a number"
n = input()
if (n % 2 ==1):
    print "Weird"
elif (n % 2 == 0 and 3 <= n <= 6):
    print "Not Weird"
elif (n % 2 == 0 and 7 <= n <= 20):
    print "Weird"
else:
    print "Not Weird"
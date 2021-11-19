file = open('countries.txt.txt', 'r')
a = 1
for line in file:
        print(a, line)
        a += 1
file.close()
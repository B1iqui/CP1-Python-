file = open('shopping.txt', 'a')
for _ in range(5):
    file.write(input())
    file.write('\n')
    
file.close()
file = open('data.txt', 'w')
for _ in range(4):
    file.writelines(input())
    file.write('\n')
    
file.close()
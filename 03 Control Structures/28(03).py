fib1 = fib2 = 1
 
n = 50
 
print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
    
    # В данном случае выводится не только значение искомого элемента (50)
    # ряда Фибоначчи, но и все числа до него включительно.
    # Для этого вывод значения fib2 помещен в цикл.
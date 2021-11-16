def count(l, t):
    counter = 0
    for symbol in text:
        if symbol.lower() == l:
            counter += 1
            
    return counter

letter = input()
text = input()

print(count(letter, text))
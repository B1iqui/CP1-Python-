def is_month(num):
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    return months[num - 1]

n = int(input())

print(is_month(n))
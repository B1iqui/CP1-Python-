def myFunc(l):
  return len(l)

names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

names.sort(key=myFunc)

print('Names:', *names)
print('Longest name:', names[-1])


            
film_titles = ['film1', 'film2', 'film3', 'film4', 'film5']
file = open('films.txt', 'w')
for title in film_titles:
    file.write(title)
    file.write('\n')
    
file.close()
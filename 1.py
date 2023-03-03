filename = input('nazwa pliku: ')
file = open(filename, 'r')

with open('lab1zad1.txt', 'w') as f:
    for i in file:
        f.write(i)
        
file.close()
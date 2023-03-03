filename = input('nazwa pliku: ')
file = open(filename, 'rb')

with open('lab1zad1.png', 'wb') as f:
    for i in file:
        f.write(i)
        
file.close()
n = 100

for i in range(n):
    with open(str(i)+'.flood', 'w') as flood_file:
        for j in range(1000):
            flood_file.write('hello number ' + str(i) + ' line number ' + str(j) + '\n')

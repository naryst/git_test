n = 100

for i in range(n):
    with open(str(i)+'.flood', 'w') as flood_file:
        flood_file.write('hello number' + str(i))

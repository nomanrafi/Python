# To print different patterns using nested loops.

# *
# **
# ***
# ****

row = int(input('Enter number of rows: '))

for i in range(1, row + 1):
    for j in range(0, i):
        print('*', end=' ')
    print('')
# *
# **
# ***
# **
# *

row = int(input('Enter number of rows: '))
for i in range(1, row + 1):
    for j in range(0, i):
        print('*', end=' ')
    print('')

for k in range(row, 0, -1):
    for l in range(0, k - 1):
        print('*', end=' ')
    print('')
    
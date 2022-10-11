def color(code):
    return f'\u001b[{code}m'


def flag():
    for i in range(2):
        print(red + '  ' * 15 + end)

    for i in range(2):
        print(white + '  ' * 15 + end)

    for i in range(2):
        print(blue + '  ' * 15 + end)


def pic():
    for i in range(1):
        print(white + ' ' * 3 + end + ' ' * 7 + white + ' ' * 3 + end + white + ' ' * 3 + end + ' ' * 7 + white + ' ' * 3 + end)
        print(' ' + white + ' ' * 3 + end + ' ' * 5 + white + ' ' * 3 + end + ' ' * 2 + white + ' ' * 3 + end + ' ' * 5 + white + ' ' * 3 + end)
        print(' ' * 3 + white + ' ' * 3 + end + ' ' + white + ' ' * 3 + end + ' ' * 6 + white + ' ' * 3 + end + ' ' + white + ' ' * 3 + end)
        print(' ' * 5 + white + ' ' * 3 + end + ' ' * 10 + white + ' ' * 3 + end)
        print(' ' * 3 + white + ' ' * 3 + end + ' ' + white + ' ' * 3 + end + ' ' * 6 + white + ' ' * 3 + end + ' ' + white + ' ' * 3 + end)
        print(' ' + white + ' ' * 3 + end + ' ' * 5 + white + ' ' * 3 + end + ' ' * 2 + white + ' ' * 3 + end + ' ' * 5 + white + ' ' * 3 + end)
        print(white + ' ' * 3 + end + ' ' * 7 + white + ' ' * 3 + end + white + ' ' * 3 + end + ' ' * 7 + white + ' ' * 3 + end)


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += white + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += blue + '  ' + white
        line += end
        print(line)
    print(white + '0   1 2 3 4 5 6 7 8 9' + end)


def diag():
    for i in range(1):
        print(red + ' ' * int(pr_do_2016) + end + ' ' + str(pr_do_2016) + ' %')
        print(blue + ' ' * int(pr_posle_2016) + end + ' ' + str(pr_posle_2016) + ' %')
        print(' ')
        print(red + ' ' + end + 'Книги до 2016 года' + ' ' + blue + ' ' + end + 'Книги после 2016 года')

red = color(41)
blue = color(44)
white = color(107)
end = color(0)

flag()

print('')

pic()

print('')

array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]


for i in range(10):
    result[i] = 2*i
print(result)

step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

import csv

do_2016 = 0
posle_2016 = 0
count = 0

with open('books.csv', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter =';')
    for row in list(table)[1:]:
        count += 1
        if row[6][6:10] >= '2016':
            do_2016 += 1
        else:
            posle_2016 += 1

pr_do_2016 = round(do_2016 / count * 100)
pr_posle_2016 = round(posle_2016 / count * 100)


print('')
diag()
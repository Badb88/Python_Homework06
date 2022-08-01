# Snimok_ekrana32

print()
def print_operation_table(operation, num_rows, num_columns):
    if operation == '*':
        for i in range(1, num_rows + 1):
            for j in range(i, i * num_columns + 1, i):
                print(j, end='\t')
            print()
    if operation == '+':
        for i in range(1, num_rows + 1):
            for j in range(i, i + num_columns + 1, i):
                print(j, end='\t')
            print()
    if operation == '**':
        for i in range(1, num_rows + 1):
            for j in range(i, i ** num_columns + 1, i):
                print(j, end='\t')
            print()

nr = int(input('Введите количество строк: '))
op = str(input('Введите операцию: '))
nc = int(input('Введите количество столбцов: '))
print_operation_table(op, nr, nc)
# Пам-парам парам-пам парам

print()
def param(s):
    a = s.split()
    count = 0
    cl = []
    check = 'ауоыэяюёиеaeiouy'
    for i in a:
        for j in i:
            for g in check:
                if g in j:
                    count += 1
        if count > 0:
            cl.append(count)
        count = 0
    y = cl[0]
    b = list(filter(lambda x: x == y, cl))
    if len(cl) == len(b):
        return True
    else:
        return False

verse = str(input('Введите вашу версию: '))
if param(verse):
    print("Парам пам-пам")
else:
    print("Пам парам")
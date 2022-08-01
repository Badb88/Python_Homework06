# Все равны, как на подбор

print()
def same_by(characteristic, objects):
    a = []
    for i in objects:
        if characteristic(i) == 0:
            a.append(True)
        else:
            a.append(False)
    y = a[0]
    b = list(filter(lambda x: x == y, a))
    if len(a) == len(b):
        return True
    else:
        return False

values = [0, 2, 4, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
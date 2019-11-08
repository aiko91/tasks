print(
'''
Ведите кольчество людей в класах
''')

class_room1 = int(input('First group: '))
class_room2 = int(input('Second group: '))
class_room3 = int(input('Third group: '))

print('\n')

try:
    if class_room1 % 2 == 0:
        print(int(class_room1 / 2))
    else:
        print(int((class_room1 / 2) + (class_room1 % 2)))

    if class_room2 % 2 == 0:
        print(int(class_room2 / 2))
    else:
        print(int((class_room2 / 2) + (class_room2 % 2)))

    if class_room3 % 2 == 0:
        print(int(class_room3 / 2))
    else:
        print(int((class_room3 / 2) + (class_room3 % 2)))
except ZeroDivisionError:
    print('На ноль делить нельзя!')


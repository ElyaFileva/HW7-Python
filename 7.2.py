string = 'house=дом car=машина men=человек tree=дерево'
list = string.split(' ')

def convert_to_tuple(x):
    return tuple(x.split('='))

tp = tuple(map(convert_to_tuple, list))
print(tp)
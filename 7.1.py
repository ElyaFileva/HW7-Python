string = input('Введите текст: ').lower().split(' ')
vowels = "аеёиоуыэюя"

def sum_vowels(x):
    return sum(x.count(vowel) for vowel in vowels)

result = list(map(sum_vowels, string))
if len(set(result)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')

# Евгений составляет 6-буквенные слова из букв М, У, Ж, Ч, И, Н, А.
# Каждая из букв может встречаться в слове ровно один раз,
# причём первой буквой не может быть Ч, буква Ж должна
# встречаться не менее 1 раза и номер слова должен быть нечётный.
# Сколько различных слов может составить Евгений?


ABC = 'МУЖЧИНА'
counter = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        word = a+b+c+d+e+f
                        if len(set(word)) == 6 and a != 'Ч' and word.count('Ж') >= 1:
                            counter += 1
                            print(counter, word)
print(counter, counter/2)
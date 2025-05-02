# Task 1

import finder

num_s = "2"

def prime_check(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

i = 3
while len(num_s) < 500:
    if prime_check(i):
        num_s += str(i)
    i += 1

def brut_check(num_s):
    count_s = {i:0 for i in range(10, 100)}
    for i in range(1, len(num_s)):
        if (10*int(num_s[i-1]) + int(num_s[i])) in count_s:
            count_s[10*int(num_s[i-1]) + int(num_s[i])] += 1
    return count_s

def hash_check(num_s):
    count_s = {i:0 for i in range(10, 100)}
    for i in count_s.keys():
        count_s[i] = finder.hash_finder(num_s, str(i))
    return count_s


def kmp_check (num_s):
    count_s = {i:0 for i in range(10, 100)}
    for i in count_s.keys():
        count_s[i] = finder.kmp_finder(num_s, str(i))
    return count_s


def shift_check (num_s):
    count_s = {i:0 for i in range(10, 100)}
    for i in count_s.keys():
        count_s[i] = finder.shift_finder(num_s, str(i))
    return count_s

best = kmp_check(num_s)
#if best == shift_check(num_s) == brut_check(num_s) == hash_check(num_s):
    #print("Работает")

print('Чаще всего встречается число', max(best, key=best.get))
print('Количество наиболее часто встречающегося двузначного числа =', max(best.values()))
del best[max(best, key=best.get)]
print('Чуть реже встречается число', max(best, key=best.get))
print('Количество чуть менее часто встречающегося двузначного числа =', max(best.values()))
del best[max(best, key=best.get)]
print('Еще реже встречается число', max(best, key=best.get))
print('Количество еще менее часто встречающегося двузначного числа =', max(best.values()))

# Task 2

import wikipedia
import docx

def remover(text):
    symbols = ['.', ',', ':', '\n', '-', ')', '1', '2',
                    '3', '4', '5', '6', '7', '8', '9', '0',
                    ';', '(', '-', '«', '»', '—', '?', '=' , '=='
                    '  ', '–']
    for i in symbols:
        if i == "  ": text = text.replace(i, ' ')
        elif i == "\n": text = text.replace(i, "\n")
        else: text = text.replace(i, '')
    return text

def text_get(file_name):
    f = docx.Document(file_name)
    text = ""
    for i in f.paragraphs:
        text += i.text
    return text

def plagiat_check(file_name, text):
    k = 0
    start_len = len(text_get(file_name))
    summary = remover(text_get(file_name))
    summary = summary.split()
    text = remover(text)
    checked_words = []
    plagiat = 0
    for i in range(2, len(summary)):
        checking = summary[i-2] + " " + summary[i-1] + " " + summary[i]
        if finder.shift_finder(text, checking):
            for j in range(3):
                if (i-j) not in checked_words:
                    checked_words.append(i-j)
                    plagiat += len(summary[i - j]) + 1
    return (plagiat/start_len)*100

language = "ru"
wikipedia.set_lang(language)
text = wikipedia.page("Жизнь").content

print(plagiat_check("Жизнь.docx", text), "%")

# Time

import time

language = "ru"
wikipedia.set_lang(language)
example1 = wikipedia.page("Жизнь").content
template1 = 'жизнь'


t0 = time.perf_counter()
finder.brute_finder(example1, template1)
t1 = time.perf_counter()
print('%.4f sec brute' % (t1-t0))


t0 = time.perf_counter()
finder.hash_finder(example1, template1)
t1 = time.perf_counter()
print('%.4f sec hash' % (t1-t0))


t0 = time.perf_counter()
finder.shift_finder(example1, template1)
t1 = time.perf_counter()
print('%.4f sec shift' % (t1-t0))

t0 = time.perf_counter()
finder.kmp_finder(example1, template1)
t1 = time.perf_counter()
print('%.4f sec kmp' % (t1-t0))

print(finder.brute_finder(example1, template1), 'naive result')
print(finder.hash_finder(example1, template1), 'karp result')
print(finder.shift_finder(example1, template1), 'mur result')
print(finder.kmp_finder(example1, template1), 'knut result')

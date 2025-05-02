def brute_finder(string, word):
    count = 0
    for i in range(len(word), len(string)+1):
        if string[i-len(word):i:] == word:
            count += 1
    return count

def hash_calcutor(alphabet: list , word: str):
    hash = 0 
    i = len(word)
    while i > 0:
        hash += alphabet.index(word[-i])*(len(alphabet))**(i-1)
        i -= 1
    return hash

def hash_finder(string, word):
    count = 0
    alphabet = list(set(string))
    word_hash = hash_calcutor(alphabet, word)
    for i in range(len(word), len(string)+1):
        if word_hash == hash_calcutor(alphabet, string[i-len(word):i:]):
            if word == string[i-len(word):i:]:
                count += 1
    return count
        
def shift_table(word):
    shift_table = {}
    k = 1
    for i in word[-2::-1]:
        if i not in shift_table:
            shift_table[i] = k
        k += 1
    if word[-1] not in shift_table:
        shift_table[word[-1]] = len(word)
    return shift_table

def shift_finder(string, word):
    table = shift_table(word)
    count,i = 0, 0
    while i + len(word) <= len(string):
        j = len(word)
        while j > 0:
            if string[i + j-1] != word[j-1]:
                if string[i+len(word)-1] in table:
                    i += table[string[i+len(word)-1]]
                else:
                    i += len(word)
                break
            j -= 1
        if j == 0:
            count += 1
            i += 1
    return count
    
def kmp_table(word):
    table = [0]*len(word)
    for i in range(1, len(word)):
        for j in range(0, i):
            if word[0:j+1] == word[i-j:i+1]:
                table[i] = j + 1
    return table

def kmp_finder(string, word):
    table = kmp_table(word)
    i,j,count = 0, 0, 0
    while i < len(string):
        if word[j] == string[i]:
            j += 1
            if j == len(word):
                j = 0
                count += 1
                if len(word) == 1:
                    i += 1
            else:
                i += 1
        else:
            if j == 0:
                i += 1
            else:
                j = table[j-1]
    return count









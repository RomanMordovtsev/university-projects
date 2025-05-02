import wikipedia 
import docx

def remover(text):
    symbols = ['.', ',', ':', '\n', '-', ')', '1', '2',
                    '3', '4', '5', '6', '7', '8', '9', '0',
                    ';', '(', '-', '«', '»', '—', '?', '=' , '==',
                    '  ', '–'] 
    for i in symbols:
        if i == "  ": text = text.replace(i, ' ')
        elif i == "\n": text = text.replace(i, "\n")
        else: text = text.replace(i, ' ')
    return text

def text_get(file_name):
    f = docx.Document(file_name)
    text = ""
    for i in f.paragraphs:
        text += i.text
    return text 

language = "ru"
wikipedia.set_lang(language)
text = remover(wikipedia.page("Жизнь").content).split()
alphabet = list(set(text))
summary = remover(text_get("Жизнь.docx"))
summary_len = len(summary)
summary = summary.split()
checked_i = []
plagiat_len = 0
hash_s = {summary[i-2] +  summary[i-1] + summary[i]: hash(summary[i-2] +  summary[i-1] +  summary[i]) for i in range(2, len(summary))}
for i in range(2, len(text)):
    if hash(text[i-2] +  text[i-1] + text[i]) in hash_s.values():
        for j in range(0, 3):
            if (i - j ) not in checked_i:
                plagiat_len += len(text[i-j])
                checked_i.append(i-j)
print((plagiat_len/summary_len)*100, " %")
        
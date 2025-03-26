"""
Напишіть python скрипт, який зчитує вміст файлу з розширенням .txt 
та повертає кількість слів і речень у цьому файлі. 
Символи, які закінчуються файл: . ! ? ...
Символи-розділювачі: пробіл , : ;
"""

def count_words_and_sentences(filePath):
    with open(filePath, 'r') as file:
        text = file.read()
    
    sentencesEndings = ['.', '!', '?']
    wordsDelimiters = [' ', ',', ':', ';']
    sentencesCount = 0
    wordsCount = 0
    inWord = False
    i = 0
    
    while i < len(text):
        char = text[i]
        
        # Слова
        if char not in wordsDelimiters:
            if not inWord:
                wordsCount += 1
                inWord = True
        else:
            inWord = False
        
        # Речення
        if char in sentencesEndings:
            if i + 2 < len(text) and text[i:i+3] == '...':
                i += 2
            sentencesCount += 1
        
        i += 1
    
    # Якщо останній символ не є кінцем речення, але є слова, рахуємо додаткове речення
    if len(text) > 0 and text[-1] not in sentencesEndings and wordsCount > 0:
        sentencesCount += 1
    
    return wordsCount, sentencesCount
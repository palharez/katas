def filter_duplicates(words):
    duplicates = []

    for word, quantity in words.items():

        if quantity > 1:
            duplicates.append(word)
    
    return duplicates

def duplicate_count(text):
    print(text)
    words = {}
    
    for word in text:
        parsed_word = word.lower()

        if not words.get(parsed_word):
            words[parsed_word] = 0
        
        words[parsed_word] += 1
    
    duplicates = filter_duplicates(words)
    
    return len(duplicates)
     

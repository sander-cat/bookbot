def count_words(text):
    book_words=text.split()

    return len(book_words)

def count_characters(text):
    lowercase=text.lower()
    letter_count={}
    for letter in lowercase:
        if letter not in letter_count:
            letter_count[letter]=1
        else:
            letter_count[letter]+=1
    
    return letter_count

def sort(items):
    return items["quantity"]

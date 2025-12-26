import sys

def get_book_text(path_to_file):
    
    with open(path_to_file) as f:
        file_contents=f.read()

    return file_contents


from stats import count_words, count_characters, sort


def main():

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book=get_book_text(sys.argv[1])
    
    num_words=count_words(book)
    num_letters=count_characters(book)

    letters_list=[]
    for letter in num_letters:
        count={}
        count["letter"]=letter
        count["quantity"]=num_letters[letter]
        letters_list.append(count)
    letters_list.sort(reverse=True, key=sort)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in letters_list:
        print(f"{dict["letter"]}: {dict["quantity"]}")
    print("============= END ===============")


main()
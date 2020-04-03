# Word in book counter

f = open("C:\\Users\\micha\\Desktop\\WithFireAndSword.txt", "r")
book = f.read()


def word_counter(word):
    counter = 0
    text_as_list = list(book.lower().split(' '))
    for word_from_book in text_as_list:
        if word.lower() in word_from_book.lower():
            counter += 1
    print(counter)


user_input = input("Type a word to check how many times it shows up in "
                   "\"With Fire and Sword\" by Henryk Sienkiewicz\n"
                   "(English edition, translation by:\tJeremiah Curtin)\n")

word_counter(user_input)

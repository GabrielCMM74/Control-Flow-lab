# exercise-02 Length of Phrase

word = None
while word != "quit":
    word = input('Please enter a word or phrase: ').lower()
    print(f'The user entered {word} and its {len(word)} letters long ')
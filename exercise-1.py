# exercise-01 Vowel or Consonant

letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
print(f'The user entered {letter}')

if letter in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
    print(f'{letter} is a vowel')

elif letter == 'y':
    print(f'{letter} is sometimes a vowel')

else: 
    print(f'{letter} is a consonant')


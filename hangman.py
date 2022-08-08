import random
CONTINUE = 1
ALREADY_GUESSED = 2
WON = 5
LOST = 6

def get_random_word(path='/usr/share/dict/words'):
    good_words = []
    with open(path) as words:
        for word in words:
            word = word.strip()
            if len(word) < 6:
                continue
            if not word.isalpha():
                continue
            if word[0].isupper():
                continue
            good_words.append(word)
    return random.choice(good_words)

def mask_word(secret_word, guessed_letters):
    masked_word = ''
    for char in secret_word:
        if char in guessed_letters:
            masked_word += char
        else:
            masked_word += '-'
    return masked_word
def get_status(secret_word, guessed_letters, turns_left):
    return  f"""{mask_word(secret_word, guessed_letters)}
    Guessed Letters: {" ".join(guessed_letters)}
    Turns Left: {turns_left}"""

def process_turn(secret_word, current_guess, guessed_letters, turns_left):
    if current_guess in guessed_letters:
        return turns_left, ALREADY_GUESSED,
    if secret_word == mask_word(secret_word, guessed_letters + [current_guess]):
        return turns_left, WON
    if turns_left == 1:
        return turns_left, LOST
    if current_guess not in secret_word:
        guessed_letters.append(current_guess)
        turns_left-= 1
        return turns_left, CONTINUE
    else:
        guessed_letters.append(current_guess)             
        return turns_left, CONTINUE

def main():
    secret_word = get_random_word()
    turns_left = 7
    guessed_letters = []
    print(secret_word)
    while True:
        print(get_status(secret_word, guessed_letters, turns_left))
        current_guess = input("Guess a letter:")
        turns_left, result = process_turn(secret_word, current_guess, guessed_letters, turns_left)
        if result == WON:
            print(f"You WON, the word was {secret_word}")
            break
        if result == LOST:
            print(f"You LOST, the word was {secret_word}")
            break
if __name__ == "__main__":
    main()
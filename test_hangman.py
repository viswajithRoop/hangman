import hangman
import random
random.seed(10)

def test_get_random_word_min_length_6():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'cat', 'car', 'dog', "hen"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "ambulances"

def test_get_random_word_no_non_alphanum():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['elephants', "hospital's", "policeman's"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "elephants"

def test_get_random_word_no_proper_noun():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['firehouse', "Abraham", "Mercury"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "firehouse"


def test_get_random_word():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'hospitalized', 'car', 'Abraham', "mercury's"]:
            f.write(i+"\n")
    words = set()
    for _ in range(10):
        word = hangman.get_random_word(my_dict)
        words.add(word)
    assert words == {"hospitalized", 'ambulances'}

def test_mask_word_no_guesses():
    for i in ["monkey", "space", "elephant", "water"]:
        assert hangman.mask_word(i, []) == len(i)* "-"

def test_mask_word_invalid_guesses():
    for i in ["monkey", "space", "elephant", "water"]:
        assert hangman.mask_word(i, ["z", "q"]) == len(i) * "-"

def test_mask_word_single_guesses():
    assert hangman.mask_word('elephant', ['l',]) == '-l------'
    assert hangman.mask_word('monkey', ['o',]) == '-o----'

def test_mask_word_multiple_guesses():
    assert hangman.mask_word('elephant', ['e', 'l',]) == 'ele-----'
    assert hangman.mask_word('kayak', ['k', 'y', 'a',]) == 'kayak'

def test_get_status():
    secret_word = "police"
    guessed_letters = ["o", "j"]
    turns_left = 5
    assert hangman.get_status(secret_word, guessed_letters, turns_left) == f"""{hangman.mask_word(secret_word, guessed_letters)}
    Guessed Letters: {" ".join(guessed_letters)}
    Turns Left: {turns_left}"""

def test_process_turn_already_guessed():
    current_guess = "o"
    secret_word = "police"
    guessed_letters = ["o", "p"]
    turns_left = 5
    assert hangman.process_turn(secret_word, current_guess, guessed_letters, turns_left ) == (turns_left, hangman.ALREADY_GUESSED)

def test_process_turn_wrong_guess():
    current_guess = "b"
    secret = 'police'
    guessed_letters = ["o", "j"]
    turns_left = 5
    assert hangman.process_turn(secret, current_guess, guessed_letters, turns_left) == (turns_left -1, hangman.CONTINUE)

def test_process_turn_right_guess():
    current_guess = "l"
    secret_word = "police"
    guessed_letters = ["p", "h", "i"]
    turns_left = 5
    assert hangman.process_turn(secret_word, current_guess, guessed_letters, turns_left) == (turns_left, hangman.CONTINUE)

def test_process_turn_win():
    current_guess = "e"
    secret_word = "police"
    guessed_letters = ["o","l","k","p","c","i"]
    turns_left = 5
    assert hangman.process_turn(secret_word, current_guess, guessed_letters, turns_left) == (turns_left, hangman.WON)

def test_process_turn_lost():
    current_guess = "k"
    secret_word = "police"
    guessed_letters = ["e","u","h","g","f","r"]
    turns_left = 1
    assert hangman.process_turn(secret_word, current_guess, guessed_letters, turns_left) == (turns_left, hangman.LOST)

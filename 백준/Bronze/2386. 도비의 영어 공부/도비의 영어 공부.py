while True:
    letter_and_sentence = input()
    if letter_and_sentence == "#":
        break

    letter, sentence = letter_and_sentence.split(" ", 1)
    print(letter, sentence.lower().count(letter))

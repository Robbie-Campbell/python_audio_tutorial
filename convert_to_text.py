from play import recognise_speech
import speech_recognition as sr
import random
import time

if __name__ == "__main__":
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    word = random.choice(WORDS)

    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
        print('Guess {}. Speak!'.format(i + 1))
        guess = recognise_speech(recognizer, microphone)
        for j in range(PROMPT_LIMIT):
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")
            if guess["error"]:
                print("ERROR: {}".format(guess["error"]))
                break
        print("You said: {}".format(guess["transcription"]))
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        if guess_is_correct:
            print("Correct! You win!".format(word))
            break
        elif user_has_more_attempts:
            print("Incorrect. Try again.\n")
        else:
            print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
            break

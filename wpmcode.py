import time
import random

def get_random_text():
    sample_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is the art of telling another human being what one wants the computer to do.",
        "To be or not to be, that is the question."
    ]
    return random.choice(sample_texts)

def typing_speed_test():
    text_to_type = get_random_text()
    print("Type the following:")
    print(text_to_type)

    input("Press Enter when you are ready to start typing...")

    start_time = time.time()
    user_input = input("Start typing: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    correct_characters = sum(1 for expected, actual in zip(text_to_type, user_input) if expected == actual)
    words_per_minute = (correct_characters / 5) / (elapsed_time / 60)

    print(f"\nYour typing speed: {round(words_per_minute, 2)} WPM")

if __name__ == "__main__":
    typing_speed_test()


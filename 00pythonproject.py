import random
import time

# Improved Dice faces for D6 with bolder dots
dice_faces = [
    """
     +-------+
     |       |
     |   ●   |
     |       |
     +-------+
    """,
    """
     +-------+
     | ●     |
     |       |
     |     ● |
     +-------+
    """,
    """
     +-------+
     | ●     |
     |   ●   |
     |     ● |
     +-------+
    """,
    """
     +-------+
     | ●   ● |
     |       |
     | ●   ● |
     +-------+
    """,
    """
     +-------+
     | ●   ● |
     |   ●   |
     | ●   ● |
     +-------+
    """,
    """
     +-------+
     | ●   ● |
     | ●   ● |
     | ●   ● |
     +-------+
    """
]

# Themed messages based on rolls
themed_messages = {
    1: "Oh no! You rolled a 1... Better luck next time!",
    2: "A 2! Not quite what you wanted, but there's always the next roll.",
    3: "You got a 3! Just average, but you can do better!",
    4: "Nice! A 4! You're getting there!",
    5: "Great roll! A 5! You're on a roll!",
    6: "Jackpot! You rolled a 6! Fantastic!",
}

def roll_dice():
    return random.choice(dice_faces)

def rolling_animation():
    for _ in range(3):
        print("Rolling", end='...', flush=True)
        time.sleep(0.5)
    print()

def welcome_message():
    print("""
    ============================================
            🎲 Welcome to the YO Dice Roller! 🎲
    ============================================
    """)

def main():
    welcome_message()

    ready = input("Are you ready to roll? (y/n): ").strip().lower()
    if ready != 'y':
        print("Okay, maybe next time! Take care!")
        return

    roll_count = 0
    roll_history = []
    face_count = [0] * 6  # For D6, to count occurrences of each face

    roll = "y"
    while roll.lower() == "y":
        rolling_animation()
        chosen_die_picture = roll_dice()
        roll_value = dice_faces.index(chosen_die_picture) + 1

        print("\nResult:")
        print(chosen_die_picture)
        print(f"You rolled a {roll_value}!")
        print(themed_messages[roll_value])  # Display themed message

        roll_count += 1
        roll_history.append(chosen_die_picture)

        # Count the rolled face for statistics
        face_count[roll_value - 1] += 1

        roll = input("Press 'y' to roll again (or any other key to quit): ").strip()

    print(f"\nYou rolled the dice {roll_count} times.")
    print("Roll history:")
    for idx, result in enumerate(roll_history, start=1):
        print(f"Roll {idx}:")
        print(result)

    print("\nStatistics:")
    for i, count in enumerate(face_count):
        print(f"Face {i + 1}: {count} times")

    print("Thanks for playing! Hope you had fun!")

if __name__ == "__main__":
    main()
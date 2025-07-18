# YO Dice Roller

## Overview
The **YO Dice Roller** is a fun and interactive Python command-line application that simulates rolling a six-sided die (D6). The program displays ASCII art representations of dice faces, provides themed messages based on the roll result, and tracks roll history and statistics. It's a beginner-friendly project designed to bring a playful dice-rolling experience to the terminal.

## Features
- **ASCII Dice Art**: Visual representation of a D6 with bold dot patterns for each face (1 to 6).
- **Themed Messages**: Unique, encouraging messages for each roll result to enhance the user experience.
- **Roll Animation**: A simple "Rolling..." animation to build excitement before revealing the result.
- **Roll History**: Tracks and displays all rolls made during a session.
- **Statistics**: Summarizes how many times each face (1-6) was rolled.
- **User-Friendly Interface**: Simple prompts to roll again or quit, with a welcoming message at the start.

## Requirements
- Python 3.x
- Standard Python libraries: `random`, `time`

No additional dependencies are required, as the project uses only Python's built-in libraries.

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/yo-dice-roller.git
   ```
2. Navigate to the project directory:
   ```bash
   cd yo-dice-roller
   ```

## Usage
1. Run the Python script:
   ```bash
   python 00pythonproject.py
   ```
2. Follow the on-screen prompts:
   - Enter `y` to start rolling the die.
   - After each roll, view the ASCII art, roll value, and a themed message.
   - Press `y` to roll again or any other key to quit.
3. When done, the program displays your roll history and statistics.

## Example Output
```
============================================
        🎲 Welcome to the YO Dice Roller! 🎲
============================================
Are you ready to roll? (y/n): y
Rolling...
Result:
     +-------+
     | ●   ● |
     |       |
     | ●   ● |
     +-------+
You rolled a 4!
Nice! A 4! You're getting there!
Press 'y' to roll again (or any other key to quit): n

You rolled the dice 1 times.
Roll history:
Roll 1:
     +-------+
     | ●   ● |
     |       |
     | ●   ● |
     +-------+

Statistics:
Face 1: 0 times
Face 2: 0 times
Face 3: 0 times
Face 4: 1 times
Face 5: 0 times
Face 6: 0 times
Thanks for playing! Hope you had fun!
```

## Code Structure
- **File**: `00pythonproject.py`
- **Key Components**:
  - `dice_faces`: List of ASCII art strings for each die face (1-6).
  - `themed_messages`: Dictionary with motivational messages for each roll value.
  - `roll_dice()`: Randomly selects a die face.
  - `rolling_animation()`: Displays a "Rolling..." animation.
  - `welcome_message()`: Prints a welcome banner.
  - `main()`: Core game loop handling user input, roll logic, history, and statistics.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows Python PEP 8 style guidelines.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built as a fun first Python project.
- Inspired by classic dice-rolling games and ASCII art.
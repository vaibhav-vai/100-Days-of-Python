# 100 Days of Python
My journey through the "100 Days of Code - Python Bootcamp" by Angela Yu.

## Projects
- **Day 01: Band Name Generator**  
  - Description: A simple Python script that generates a band name using user inputs (city and pet name).  
  - File: [band_name_generator.py](Day01-BandNameGenerator/band_name_generator.py)
  - Sample Output:  
    Input: City = "Delhi", Pet = "Tommy"  
    Output: "Delhi Tommy"
- **Day 02: Tip Calculator**  
  - Description: A Python script to calculate the total bill with tip and split it among people.  
  - File: [tip_calculator.py](Day02_TipCalculator/tip_calculator.py)  
  - Sample Output:  
    Input: Bill = $100, Tip = 10%, People = 4  
    Output: "Each person should pay: $27.50"
- **Day 03: Treasure Island**
  - **Description**: A text-based adventure game where the player makes choices to find the treasure using nested if-else statements.
  - **File**: [treasure_island.py](Day03_TreasureIsland/treasure_island.py)
  - **Sample Output**:
    - Input: The player chooses "left" or "right", "swim" or "wait", etc.
    - Output: "You found the treasure! You Win!" or "Game Over."
- **Day 04: Rock Paper Scissors**
  - **Description**: A text-based game where the player competes against the computer in a classic Rock Paper Scissors match using random selection and conditionals.
  - **File**: [rock_paper_scissors.py](Day04_RockPaperScissors/rock_paper_scissors.py)
  - **Sample Output**:
    - Input: Player chooses "Rock"
    - Output: "Computer chose Scissors. You Win!" or "Computer chose Paper. You Lose!"
- **Day 5: Password Generator**
  - **Description**: A program that generates a random password using loops and basic randomization techniques.
  - **File**: [password_generator.py](Day05_PasswordGenerator/password_generator.py)
  - **Sample Output**:
    - Input: User specifies the desired length, count of letters, symbols and numbers in their password (e.g., 8 characters)
    - Output: "Your password is: s2t#u1v*"
- **Day 6: Escaping the Maze (Reeborg’s World)**
  - **Description**: A program that helps Reeborg, a virtual robot, escape a maze in Reeborg’s World using loops and conditional logic to navigate obstacles.
  - **File**: [escaping_the_maze.py](Day06_EscapingTheMaze/escaping_the_maze.py)
  - **Sample Output**:
    - Input: The maze layout is provided in Reeborg’s World (e.g., Maze 1)
    - Output: Reeborg successfully reaches the goal or gets stuck (visualized in Reeborg’s World) 
- **Day 7: Hangman**
  - **Description**: A text-based game where the player guesses letters to uncover a randomly chosen word, with a limited number of lives, using lists and loops.
  - **File**: [hangman.py](Day07_Hangman/hangman.py)
  - **Sample Output**:
    - Input: Player guesses a letter (e.g., "a")
    - Output: "Current word: _a___  Lives: 6" or "You lose! The word was: apple"
- **Day 8: Caesar Cipher**
  - **Description**: A program that encrypts or decrypts a message by shifting letters in the alphabet by a specified number, using functions and loops.
  - **File**: [caesar_cipher.py](Day08_CaesarCipher/caeser_cipher.py)
  - **Sample Output**:
    - **Input**: User chooses to "encode" or "decode", enters a message (e.g., "hello"), and a shift number (e.g., 3)
    - **Output**: "The encoded text is: "khoor" or "The decoded text is: hello"
- **Day 9: Blind Auction**
  - **Description**: A program that simulates a blind auction where multiple bidders place secret bids, and the highest bidder wins, using dictionaries and loops.
  - **File**: [blind_auction.py](Day09_BlindAuction/blind_auction.py)
  - **Sample Output**:
    - **Input**: Users enter their name and bid amount (e.g., "Alice: 100", "Bob: 150"), and indicate if there are more bidders
    - **Output**: "The winner is Bob with a bid of $150!"
- **Day 10: Calculator**
  - **Description**: A program that performs basic arithmetic operations (addition, subtraction, multiplication, division) and allows the user to continue calculating with the result, using functions and loops.
  - **File**: [calculator.py](Day10_Calculator/calculator.py)
  - **Sample Output**:
    - **Input**: User enters two numbers (e.g., 5 and 3), chooses an operation (e.g., "+"), and decides whether to continue (e.g., "y" or "n")
    - **Output**: "5 + 3 = 8" and "Continue with 8? (y/n)"
- **Day 11: Blackjack**
  - **Description**: A text-based game simulating Blackjack, where the player competes against the dealer to get a hand value closest to 21 without going over, using lists, loops, and conditionals.
  - **File**: [blackjack.py](Day11_Blackjack/blackjack.py)
  - **Sample Output**:
    - **Input**: Player chooses to "hit" or "stand" (e.g., "hit")
    - **Output**: "Your cards: [10, 5], total: 15  Dealer's first card: 7" or "You went over 21! You lose."
- **Day 12: Guess the Number**
  - **Description**: A text-based game where the player tries to guess a randomly chosen number, receiving hints like "Too high" or "Too low", using loops, conditionals, and randomization.
  - **File**: [guess_the_number.py](Day12_GuessTheNumber/guess_the_number.py)
  - **Sample Output**:
    - **Input**: Player guesses a number (e.g., "50")
    - **Output**: "Too high! Guess again." or "You got it! The number was 42."
- **Day 13: Debugging**
  - **Description**: A learning module on debugging techniques to identify and fix errors in code, covering problem description, bug reproduction, line-by-line evaluation, using print statements, debuggers, and final tips, with exercises on Odd or Even, Leap Year, and FizzBuzz.
  - **File**: N/A (Conceptual learning and exercises)
- **Day 14: Higher Lower**
  - **Description**: A game where the player guesses which of two randomly selected options has a higher value (e.g., social media followers), using data from a file, loops, and conditionals.
  - **File**: [higher_lower.py](Day14_HigherLower/higher_lower.py)
  - **Sample Output**:
    - **Input**: Player chooses "A" or "B" (e.g., "A")
    - **Output**: "Compare A: Cristiano Ronaldo vs B: Lionel Messi. Is A higher or lower? You chose A. Correct!" or "Wrong! B had more followers."
- **Day 15: Coffee Machine**
  - **Description**: A program that simulates a coffee machine, managing resources (water, milk, coffee), processing orders, and handling payments using dictionaries, loops, and conditionals.
  - **File**: [coffee_machine.py](Day15_CoffeeMachine/coffee_machine.py)
  - **Sample Output**:
    - **Input**: User selects "espresso", inserts "1.5" in coins
    - **Output**: "Please insert coins. Here is your espresso. Enjoy!" or "Sorry, not enough resources."
- **Day 16: OOP Coffee Maker**
  - **Description**: A program that enhances the coffee machine with object-oriented programming (OOP), using classes and objects to manage resources, orders, and payments.
  - **File**: [main.py](Day16_OOPCoffeeMachine/main.py)
  - **Sample Output**:
    - **Input**: User selects "latte", inserts "2.5" in coins
    - **Output**: "Please insert coins. Latte prepared. Enjoy!" or "Insufficient resources for latte."
- **Day 17: Quiz App**
  - **Description**: A program that creates a quiz application where users answer questions and track their score using lists, loops, dictionaries and OOP concepts.
  - **File**: quiz.py
  - **Sample Output**:
    - **Input**: User answers a question (e.g., "True" for "Is the sky blue?")
    - **Output**: "Correct! Score: 1" or "Wrong. Score: 0. Next question..."

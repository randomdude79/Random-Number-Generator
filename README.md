# Random Number Generator with Feedback function in Python
This code defines a simple Python program that generates a random number within a user-defined range. It also includes functionality for providing feedback and exiting the program. Here's a breakdown of how it works:

Function Definitions:

`exit()`: This function imports the sys module and calls its `exit()` function, which terminates the program.
`is_an_integer(s)`: This function checks if a given string `s` represents an integer by attempting to convert it to an integer using a `try-except` block.
`get_int(prompt)`: This function prompts the user to input an integer. It handles special cases like when the user inputs "-0" (which is not a valid integer), `Exit` or `exit` (to exit the program), and `Feedback` or `feedback` (to provide feedback). It also writes feedback to a file named `feedback.txt`.
`random_gen()`: This function generates random numbers based on user input. It prompts the user to input two numbers defining a range and the number of random integers to generate within that range. It then generates random integers and prints them.

Main Program:

The main program consists of an infinite loop (`while True:`) that repeatedly calls the `random_gen()` function.
How to Use:

Run the Python script containing this code.
The program will prompt you to input two numbers defining the range within which you want to generate random numbers.
It will then prompt you to input the number of random integers you want to generate within that range.
After providing inputs, the program will generate and display the random numbers.
You can also input `Exit` or `exit` at any time to terminate the program.
Additionally, you can input `Feedback` or `feedback` to provide feedback, which will be saved to a file named `feedback.txt`.
Functionality:

The program ensures that the input numbers are integers and handles invalid inputs gracefully.
It provides a feedback mechanism for users to share their thoughts about the program.
It generates random numbers within the specified range and displays them to the user.
It handles edge cases like when the user inputs the same number for both ends of the range or special numbers like 69 and 420.
Overall, this program serves as a simple tool for generating random numbers with user-defined ranges, while also allowing for feedback from users.
### [Credits](Credits.md)
###[Code](main.py.md)

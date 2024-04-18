# Random Number Generator
![logo](logo.png)
This code defines a simple Python program that generates a random number within a user-defined range. It also includes functionality for providing feedback and exiting the program. Here's a breakdown of how it works:

Function Definitions:

`detect_profanity()`: This function will detect profanity in the feedback or email input.
`clear()`: This function uses the `os.system('clear')` command to clear the console screen. It is used to provide a clean interface when running the program.  
`animate(key)`: This function creates a simple animation effect using `sys.stdout.write()` and `time.sleep()`. The key parameter determines the intensity of the animation.  
`exit()`: This function uses `sys.exit()` to exit the program cleanly.  
`is_an_integer(s)`: This function checks if a given string `s` can be converted to an integer. It returns `True` if conversion is successful, otherwise `False`.  
`get_int(prompt)`: This function repeatedly asks the user for input until they enter a valid integer. It handles special commands like `/clear` to clear the console and `/exit` to exit the program.  

Main Function `random_gen()`:  

This function is the core of the random number generation process. It first prompts the user to choose two numbers to define a range, and optionally, a seed value for the random number generator.  
Based on the user's input, it generates a specified amount of random numbers within the defined range using `random.randint()`.  
It then offers the option to calculate and display the average of all generated numbers using `statistics.mean()`.  

Usage:  

To use the program, run it in a Python environment.  
Follow the prompts to choose the range of numbers, specify a seed (if desired), and select the amount of random numbers to generate.  
The program provides options to clear the console, exit the program, and provide feedback.  
After generating random numbers, it offers the option to calculate and display the average of all generated numbers.  

### [Credits](Credits.md)
### [Updates](UpdateLog.md)
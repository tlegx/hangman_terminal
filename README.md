# hangman_terminal
A small hangman game created in Python for fun
## How it works
Randomly select a file from the [database](https://github.com/tlegx/hangman_terminal/tree/master/database) folder, then read the file and randomly select a line, after that take that line to play as the secret word (if it's too hard to understand, please see [main.py](https://github.com/tlegx/hangman_terminal/blob/master/main.py), thank you!)
## How to use
**Make sure you have installed the *Python interpreter* before continuing**

Navigate to the directory you've downloaded this and simply type 
```
python main.py
```
in the Command Prompt or a terminal. Choose the "New game" option and show off your guessing skills. I've provided 2 sample files in the [database](https://github.com/tlegx/hangman_terminal/tree/master/database) folder for you to start off.
### Add new words to the database
If you want more words because you've cycled through it all, or just want to challenge yourself with long and complicated words, then please follow the guide below:
- ***Step 1:*** Navigate to the *database* folder.
- ***Step 2:*** Add your text file, with the filename being the subject of the words in that text file.
### Warning on adding new words
- Please add words that are based off the English alphabet, otherwise Python will not be able to recognize the words you given.
- Add one word ***per*** line.
- Don't add spaces to the word. You can still play it but it will rather be confusing.
## Bug fixes and contributions
I am constantly adding new features and fixing to this app. If you found a bug, please don't hesitate to create an [issue](https://github.com/tlegx/hangman_terminal/issues), or if you know the fix, feel free to contribute to this repository.
## Screenshots
![Welcome screen](https://github.com/tlegx/hangman_terminal/blob/master/demo/Screenshot%202021-06-11%20214409.png) ![Level screen](https://github.com/tlegx/hangman_terminal/blob/master/demo/Screenshot%202021-06-11%20214449.png)
![Playing](https://github.com/tlegx/hangman_terminal/blob/master/demo/Screenshot%202021-06-11%20214506.png) ![Correct guess](https://github.com/tlegx/hangman_terminal/blob/master/demo/Screenshot%202021-06-11%20214600.png)
![Wrong guess](https://github.com/tlegx/hangman_terminal/blob/master/demo/Screenshot%202021-06-11%20214616.png) ![Player won](https://github.com/tlegx/hangman_terminal/blob/master/demo/Screenshot%202021-06-11%20214636.png)
![Credits screen](https://github.com/tlegx/hangman_terminal/blob/master/demo/Screenshot%202021-06-11%20214651.png)
## License
hangman_terminal is licensed under GNU General Public License v3.0

Copyright (C) 2021 tlegx

For more information, please see [LICENSE](https://github.com/tlegx/hangman_terminal/blob/master/LICENSE)

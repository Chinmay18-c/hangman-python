# 🕹️ Hangman Game (Python)

Welcome to the classic **Hangman** game — now enhanced with a 500-word vocabulary and colorful terminal output using `colorama`!  
Test your vocabulary and guessing skills in this fun, beginner-friendly Python project.

---

## 🎯 Features
- ✅ 500-word mixed-difficulty word list
- ✅ Colorful terminal output (`colorama`)
- ✅ ASCII art hangman stages
- ✅ Repeated guess detection
- ✅ Modular, function-based design
- ✅ GitHub-ready with clean file structure

---

## 🛠️ Requirements

- Python 3.x  
- `colorama` module

Install with:
```bash
pip install colorama
```

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/your-username/hangman-python.git
cd hangman-python
```

2. Run the game:
```bash
python main.py
```

---

## 🧩 Project Structure
```
hangman-python/
├── main.py           # Core game logic
├── words.py          # 500-word list
├── hangman_art.py    # ASCII logo + hangman stages
├── README.md         # Project readme
└── requirements.txt  # Optional
```

---

## 🎨 ASCII Logo
```plaintext
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
```

---

## ☠️ Hangman Stages

Each wrong guess draws part of the hangman. You lose at 6 wrong guesses.

```plaintext
Stage 0:
  +---+
  |   |
      |
      |
      |
      |
=========

Stage 1:
  +---+
  |   |
  O   |
      |
      |
      |
=========

Stage 2:
  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Stage 3:
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

Stage 4:
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Stage 5:
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Stage 6 (Game Over):
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

---

## ✅ Sample Game Output
```plaintext
_ _ _ _ _ _

******************** 6/6 LIVES LEFT ********************
Guess a letter: a

Word to guess: _ a _ _ _ _

✅ You guessed correctly!

Guess a letter: z

❌ You guessed 'z', that's not in the word. You lose a life.
```

---

## 🙏 Credits
- 🧠 **Instructor**: Dr. Angela Yu (Original project inspiration)
- 🎨 **Art & Structure**: Adapted and enhanced from her Python Bootcamp
- 💻 **Developer**: [Your Name](https://github.com/your-username)
- 🎨 **Color Support**: `colorama` Python package

---

## 📜 License
This project is licensed under the MIT License.  
Use it, modify it, share it — enjoy learning Python!

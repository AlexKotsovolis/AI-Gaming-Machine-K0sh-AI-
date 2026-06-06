# K0sh AI - Semantic Chat & Gaming Machine! 🤖🎮

> **K0sh AI:** A casual, NLP-powered conversational chatbot and number-guessing game, and rock-paper-scissors game, built with `SentenceTransformers`, `Tkinter` as well as `JSON` and `Threading` (soon)

An interactive desktop application that merges semantic AI conversation with a classic number-guessing game. Powered by a local natural language processing (NLP) model and packaged inside a clean, dark-themed GUI, K0sh understands user intent regardless of spelling, slang, or language variations (including Greek and Greeklish!).

---

## ✨ Features

* **Semantic AI Conversations:** Utilizes Sentence-BERT (`all-MiniLM-L6-v2`) to accurately calculate cosine similarity and map user inputs to response pairs—meaning it handles typos, variations, and multilingual slang gracefully.
* **Dual Mode Engine:** * *Chat Mode:* Crack jokes, ask how K0sh is doing, or learn how to play.
  * *Game Mode:* Type `INT` to initialize a randomly generated 0-100 number-guessing challenge with randomized AI feedback hints.
* **Multilingual Support:** Pre-mapped to recognize and respond to English, Greek, and phonetic Greeklish phrases.
* **Sleek Dark GUI:** Built entirely with Python's standard `tkinter` package featuring a retro, hacker-friendly dark palette and intuitive layout.

---

## 🛠️ Tech Stack & Requirements

* **Python 3.8+**
* **Sentence-Transformers** (Semantic search engine)
* **PyTorch** (Underlying tensor computations)
* **Tkinter** (Built-in Python GUI library)
---

## LICENSE

K0sh AI is licensed under the **K0sh AI Personal Use License v1.0**.

### What you may do

* Use the software for personal, non-commercial purposes.
* Modify the software for personal, non-commercial purposes.

### What you may NOT do

* Commercialize, sell, or monetize the software.
* Distribute, redistribute, publish, or share the software or modified versions.
* Incorporate the software into distributed or commercial projects.
* Remove copyright notices or author attribution.

For full terms, see the LICENSE file included in this repository.

© 2026 Alex Kotsovolis. All rights reserved.

---

## Screenshot!

-> From VER. 0.3 & 0.2

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ef45107b-a5a5-48ac-98d4-dd4567e09a21" />


-> From VER. 0.4: 

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/6fe7a8c8-7c8e-4e24-954d-babfdfa0c392" />




---
## UPDATE LOG
---
## What is the update log?
---

The update log is basically a file here in github, where I will be updating the text of the file, whenever a new version of K0sh or even of minor fixes/updates are posted. So, starting from now, 03/06/2026 i am releasing this log.

---

## Version 0.1 (RELEASE)

---

  --> Released K0sh AI.
  
  --> Simple "Guess the number" and "Chat".
  
  --> Simple GUI.
  
  --> Kinda boring... :(

---
## Version 0.2: (REWORK)
---

  --> Reworked chat messages!
  
  --> Cool UI and design!  (Feel free to make suggestions if you want!)
  
  --> NOTICE: Hey everyone! I have decided (from now on) to keep every version here in github, if anyone would like to use previous versions (with of course more coming soon). I think it is really cool, so next update, you can choose which version you like the most!
  
---
## Version: 0.3 : "One.. More.. Game!"
--- 

  --> Introducing... Rock-Paper-Scissors!    (NEW GAME MODE)

  --> Really simple, maybe buggy.

  --> New messages.

  --> Next update is gonna be FIRE

  --> Kept old version's code, as promised.

---
## Version: 0.4: "Wait.. I know you!" (what even are these names really)
---

  --> Introducing our new feature... LOG-IN / PLAYER DATA!

  --> New Point system!

  --> New messages.

  --> I have a headache...

  --> New GUI, more professional-like and some gaming vibes! (It is going to change anytime soon, the GUI will never stay the same!)

  --> Kept old version's code, as promised.

  --> How it works: Make a new account (with a json which is already being made in the code), play, leave, rejoin, say your name and K0sh is going to know you know!
---
## Version 0.4.1 : "Threading"
---

  --> Added threading, for a better experience.

  --> Lagging? Not anymore! Threading is here.

  --> Really small update, before version 0.5. 
  
---
# Next Version: 0.5 "Another One."
- New game mode, will take some time.
---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/k0sh-ai.git](https://github.com/YOUR_USERNAME/k0sh-ai.git)
cd k0sh-ai
2. Install Dependencies
Make sure you have your virtual environment activated, then install the NLP framework:

Bash
pip install sentence-transformers torch
3. Run the Application
Bash
python main.py
Note: On your first startup, the application will take a brief moment to download the lightweight all-MiniLM-L6-v2 model locally.

🎮 How to Play
Launch the app and chat with K0sh to warm up.

When you are ready, type INT into the chat box to initialize the game loop.

K0sh will lock in a hidden number between 0 and 100.

Submit your numeric guesses. K0sh will guide you with dynamic alerts (Higher!, Lower!) until you strike the winning match!

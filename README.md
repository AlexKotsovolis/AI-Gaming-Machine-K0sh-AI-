# K0sh AI - Semantic Chat & Number Guessing Game 🤖🎮

> **K0sh AI:** A casual, NLP-powered conversational chatbot and number-guessing game built with `SentenceTransformers` and `Tkinter`.

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

## Screenshot!

<img width="598" height="726" alt="image" src="https://github.com/user-attachments/assets/9f77bd00-7ad9-4e8f-b736-1f4d057820c4" />

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

---
#UPDATE LOG
---
#What is the update log?
---

The update log is basically a file here in github, where I will be updating the text of the file, whenever a new version of K0sh or even of minor fixes/updates are posted. So, starting from now, 03/06/2026 i am releasing this log.

---

#VERSION 0.1 (RELEASE)

---

  --> Released K0sh AI.
  --> Simple "Guess the number" and "Chat".
  --> Simple GUI.
  --> Kinda boring... :(

---

# What's coming in the next version(s):

  >New GUI
  >New Games


Next Version: 0.2 (REWORK) --> Coming Soon!
---

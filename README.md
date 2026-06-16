````markdown
# 🤖 K0sh AI
### Semantic Chat & Gaming Machine

<p align="center">
  <a href="https://deepwiki.com/AlexKotsovolis/AI-Gaming-Machine-K0sh-AI-">
    <img src="https://devin.ai/assets/askdeepwiki.png" alt="Ask DeepWiki">
  </a>
</p>

<p align="center">
  <strong>A modern desktop AI chatbot and gaming platform powered by local NLP.</strong>
</p>

<p align="center">
  🧠 Semantic AI • 🌍 Multilingual • 🎮 Gaming • ⚡ Local Processing
</p>

---

## 🚀 Overview

K0sh AI is a Python-powered desktop chatbot that combines **semantic artificial intelligence**, **multilingual conversations**, and **built-in gaming experiences** inside a sleek cyberpunk-inspired interface.

Unlike traditional keyword-based chatbots, K0sh AI uses **Sentence-BERT embeddings** and **cosine similarity matching** to understand user intent, making conversations feel more natural and forgiving of typos, slang, and language variations.

Whether you want to chat, compete in games, unlock achievements, or simply explore a local AI assistant, K0sh AI delivers a unique experience entirely on your desktop.

---

## 🖼️ Showcase

<img width="1024" height="506" alt="image" src="https://github.com/user-attachments/assets/6cb327cd-2d87-4973-a716-a66c2c0a3c70" />

<img width="1024" height="506" alt="image" src="https://github.com/user-attachments/assets/4a0b7fdc-54ae-439f-8fd0-16471000cd4f" />

---

# ✨ Features

## 🧠 Semantic AI Conversations

Powered by:

```python
paraphrase-multilingual-MiniLM-L12-v2
````

K0sh AI understands:

* Typographical errors
* Informal language
* Slang
* Multilingual input
* Similar sentence meanings

Using Sentence-BERT embeddings and cosine similarity matching.

---

## 🎮 Built-In Game Modes

| Command | Game                     |
| ------- | ------------------------ |
| `GTN`   | Guess The Number         |
| `RPS`   | Rock-Paper-Scissors      |
| `BLC`   | Blackjack (Dice Edition) |

Earn points, unlock achievements, and compete against K0sh.

---

## 🌍 Multilingual Support

K0sh AI recognizes:

* 🇬🇧 English
* 🇬🇷 Greek
* 🔤 Greeklish

Language detection happens automatically.

---

## 👤 Player Profiles

Features:

* Login system
* Persistent player data
* Point tracking
* Achievement tracking
* Secure JSON storage

---

## 💬 Typewriter Responses

Enjoy smooth character-by-character rendering for a more immersive conversation experience.

---

## 📜 Chat History

Every conversation can be stored and reviewed using the dedicated history viewer.

---

## 🖥️ Modern Cyberpunk Interface

Built with Tkinter and inspired by retro terminal aesthetics.

Features:

* Dark theme
* Neon accents
* Responsive layout
* Dedicated game windows
* Achievement notifications

---

## ⚡ Multithreaded Architecture

K0sh AI uses threading to keep the UI responsive while processing user requests.

---

# 🛠️ Requirements

| Requirement | Version           |
| ----------- | ----------------- |
| Python      | 3.8+              |
| Internet    | First launch only |

> The internet connection is only required for downloading the NLP model during first startup.

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/AlexKotsovolis/AI-Gaming-Machine-K0sh-AI-.git
cd AI-Gaming-Machine-K0sh-AI-
```

## 2️⃣ Install Dependencies

```bash
pip install sentence-transformers torch pillow langdetect
```

## 3️⃣ Launch K0sh AI

Navigate to the latest version folder:

```text
CODE_VERSIONS/
└── CODE (VER. 0.6.1)
```

Run:

```bash
python your_script_name.py
```

---

## 📥 First Startup

The following model will automatically download:

```text
paraphrase-multilingual-MiniLM-L12-v2
```

This only happens once.

---

# 🎮 How To Play

### Step 1

Launch K0sh AI.

### Step 2

Enter your username.

### Step 3

Start chatting or launch a game.

### Available Commands

| Command | Description         |
| ------- | ------------------- |
| GTN     | Guess The Number    |
| RPS     | Rock-Paper-Scissors |
| BLC     | Blackjack           |

---

# 📸 Preview (VER. 0.6 - 0.6.2)

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/3ddd5bed-6f2f-419f-a2f2-5be1f0898317" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/20fa9bc7-72a0-4365-81e9-f1cde2a79075" />

---

# 🔧 Built With

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Core application logic    |
| Tkinter               | Desktop GUI               |
| Sentence-Transformers | Semantic NLP              |
| PyTorch               | Tensor computations       |
| Threading             | Responsive interface      |
| JSON                  | Persistent player storage |

---

# 🔒 License

This project is licensed under the:

## K0sh AI Personal Use License v1.0

### ✅ You May

* Use the software
* Modify the software
* Learn from the code
* Create personal versions

### ❌ You May NOT

* Sell the software
* Commercialize the software
* Redistribute the software
* Publish modified versions

For complete details, see:

```text
LICENCE
```

© 2026 Alex Kotsovolis. All Rights Reserved.

---

# 📋 Update Log

<details>
<summary><strong>Version History</strong></summary>

### 🚀 Version 0.1 (RELEASE)

Released K0sh AI. Simple "Guess the Number" and Chat functionality.

### 🔨 Version 0.2 (REWORK)

Reworked chat messages and UI. Repository version tracking introduced.

### 🎮 Version 0.3 ("One.. More.. Game!")

Added Rock-Paper-Scissors (RPS).

### 👤 Version 0.4 ("Wait.. I know you!")

Added Login System and Persistent Player Data.

### ⚡ Version 0.4.1 ("Threading")

Introduced multithreading.

### 🃏 Version 0.5 ("Another One.")

New GUI and Blackjack mode.

### ✨ Version 0.5.1 ("Enhanced GUI")

Added typewriter animation and bug fixes.

### 🌍 Version 0.5.2 ("Multilingual")

Introduced multilingual support.

### 🛠️ Version 0.5.3 ("QOL Fixes!")

Improved chatbot communication and fixed response bugs.

### 📜 Version 0.6 ("???")

Added chat history window and improved gameplay systems.

### 🔧 Version 0.6.1 ("QOL")

Security improvements, better Blackjack balancing, and new player states.

### 🏆 Version 0.6.2

Added:

* Loading Screen
* Achievement System
* UI Improvements
* Bug Fixes

More updates coming soon...

</details>

---

# 🗺️ Roadmap

### Planned Features

* [ ] More AI conversation data
* [ ] New achievements
* [ ] Additional game modes
* [ ] Better player statistics
* [ ] Save slots
* [ ] Improved NLP responses
* [ ] More animations
* [ ] Expanded multilingual support

---

# 🐱 The Inspiration

This program's inspiration comes from the real K0sh.

<img width="3060" height="4080" alt="The real K0sh" src="https://github.com/user-attachments/assets/feccb714-3670-4985-a1ac-b2e2b642ddc0" />

<img width="2556" height="3408" alt="Another photo of K0sh" src="https://github.com/user-attachments/assets/9d706290-6f8c-4cc3-8d93-a89b14c81363" />

---

# 👨‍💻 Author

## Alex Kotsovolis

GitHub:

* https://github.com/AlexKotsovolis

Discord:

* @myboialex3

---

# ⭐ Support The Project

If you enjoy K0sh AI and want to support future development:

⭐ Star the repository

🐛 Report bugs

💡 Suggest new features

📢 Share the project

Every star helps the project grow.

---

<p align="center">
  Built with ❤️, Python, and a little bit of chaos.
</p>
```

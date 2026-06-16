# 🤖 K0sh AI — Semantic Chat & Gaming Machine
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/AlexKotsovolis/AI-Gaming-Machine-K0sh-AI-)

<img width="1024" height="506" alt="image" src="https://github.com/user-attachments/assets/6cb327cd-2d87-4973-a716-a66c2c0a3c70" />
<img width="1024" height="506" alt="image" src="https://github.com/user-attachments/assets/4a0b7fdc-54ae-439f-8fd0-16471000cd4f" />

A modern desktop AI chatbot and gaming platform powered by local NLP, built entirely with Python.

**Semantic. Multilingual. Fun.**

---

## ✨ Features

- 🧠 **Semantic AI Conversations** — Powered by Sentence-BERT (`paraphrase-multilingual-MiniLM-L12-v2`) using cosine similarity to understand typos, slang, and language variations.
- 🎮 **Three Game Modes** — Guess the Number (GTN), Rock-Paper-Scissors (RPS), and Blackjack (BLC).
- 🌍 **Multilingual Support** — Recognizes and responds in English, Greek, and phonetic Greeklish.
- 👤 **Player Profiles** — Login system with persistent score tracking via JSON.
- 💬 **Typewriter Animations** — Smooth character-by-character response rendering.
- 📜 **Chat History** — In-app history window with session logging.
- 🖥️ **Sleek Dark GUI** — Retro cyberpunk-inspired interface built with Tkinter.
- ⚡ **Multithreaded Architecture** — Non-blocking responses for smooth performance.

---

## 🛠️ Requirements

- Python 3.8+
- Internet connection (first run only, to download the model)

---

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AlexKotsovolis/AI-Gaming-Machine-K0sh-AI-.git
    cd AI-Gaming-Machine-K0sh-AI-
    ```

2.  **Install dependencies:**
    ```bash
    pip install sentence-transformers torch pillow langdetect
    ```

3.  **Run the application:**
    Navigate to the latest version directory (e.g., `CODE_VERSIONS/CODE (VER. 0.6.1)`) and run the Python script.

> **Note:** On first startup, the app will download the `paraphrase-multilingual-MiniLM-L12-v2` model locally. This may take a moment.

---

## 🎮 How to Play

1.  Launch the app and enter your name when prompted.
2.  Chat with K0sh freely, or jump straight into a game.
3.  Type one of the game commands to start:

| Command | Game                 |
| :------ | :------------------- |
| `GTN`   | Guess the Number     |
| `RPS`   | Rock-Paper-Scissors  |
| `BLC`   | Blackjack (dice)     |

---

## 📸 Preview (VER. 0.6 - 0.6.2)
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/3ddd5bed-6f2f-419f-a2f2-5be1f0898317" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/20fa9bc7-72a0-4365-81e9-f1cde2a79075" />

---

## 🔧 Built With

| Technology            | Purpose                     |
| :-------------------- | :-------------------------- |
| Python                | Core application logic      |
| Tkinter               | Desktop GUI                 |
| Sentence-Transformers | Semantic NLP engine         |
| PyTorch               | Tensor computations         |
| Threading             | Non-blocking UI             |
| JSON                  | Player data persistence     |

---

## 🔒 License

This project is licensed under the **K0sh AI Personal Use License v1.0**.

-   **You may:** Use and modify the software for personal, non-commercial purposes.
-   **You may NOT:** Commercialize, sell, distribute, redistribute, or publish the software or its modified versions.

For full terms, see the `LICENCE` file.

© 2026 Alex Kotsovolis. All rights reserved.

---

## 📋 Update Log

### Version 0.1 (RELEASE)
Released K0sh AI. Simple "Guess the number" and "Chat". Simple GUI.

### Version 0.2 (REWORK)
Reworked chat messages and UI. All versions are now kept in the repository.

### Version 0.3 ("One.. More.. Game!")
Introduced Rock-Paper-Scissors (RPS) game mode. New messages added.

### Version 0.4 ("Wait.. I know you!")
Introduced a Log-in / Player Data system with persistent points. Reworked GUI.

### Version 0.4.1 ("Threading")
Added threading for a smoother, non-blocking experience.

### Version 0.5 ("Another One.")
Changed the GUI. Added "Blackjack" (BLC) game mode.

### Version 0.5.1 ("V.0.5, but enhanced GUI")
Added typewriter animations for bot responses and fixed core bugs.

### Version 0.5.2 ("Multilingual")
K0sh AI now supports multiple languages based on user input.

### Version 0.5.3 ("QOL fixes!")
Fixed a bug allowing user input during bot responses. Enhanced Q&A pairs for better communication.

### Version 0.6 ("???")
Added a chat history feature with a dedicated UI window. Changed the GUI. Fixed core bugs in Blackjack and Guess the Number.

### Version 0.6.1 ("QOL")
Made several quality-of-life changes, including more secure data saving, resolved a history bug, added more in-game instructions, made Blackjack more challenging, and introduced a "Broke" state for negative point balances.

### Version 0.6.2 ("🏆")
Added a cool loading screen with elegant animations. Also, the main update was the achievement system I made. Also fixed the broke state and many more. There are some core bugs 🐛 to fix, so stay tuned for next update!
---

## The Inspiration

This program's inspiration comes from the real K0sh:

<img width="3060" height="4080" alt="The real K0sh" src="https://github.com/user-attachments/assets/feccb714-3670-4985-a1ac-b2e2b642ddc0" />

<img width="2556" height="3408" alt="Another photo of K0sh" src="https://github.com/user-attachments/assets/9d706290-6f8c-4cc3-8d93-a89b14c81363" />

---

## 👨‍💻 Author

**Alex Kotsovolis**
- GitHub: [@AlexKotsovolis](https://github.com/AlexKotsovolis)
- Discord: @myboialex3

⭐ If you find this project useful, consider starring the repository

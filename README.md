# 🤖 K0sh AI — Semantic Chat & Gaming Machine
---
<img width="1024" height="506" alt="image" src="https://github.com/user-attachments/assets/6cb327cd-2d87-4973-a716-a66c2c0a3c70" />

and another version of this image ;)

<img width="1024" height="506" alt="image" src="https://github.com/user-attachments/assets/4a0b7fdc-54ae-439f-8fd0-16471000cd4f" />

---
> **Preview Note:** UI changes between versions. Screenshots below reflect specific releases.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-K0sh%20Personal%20Use%20v1.0-red) ![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A modern desktop AI chatbot and gaming platform powered by local NLP, built entirely with Python.

**Semantic. Multilingual. Fun.**

---

## ✨ Features

- 🧠 **Semantic AI Conversations** — Powered by Sentence-BERT (`paraphrase-multilingual-MiniLM-L12-v2`) using cosine similarity to understand typos, slang, and language variations
- 🎮 **Three Game Modes** — Guess the Number (GTN), Rock-Paper-Scissors (RPS), and Blackjack (BLC)
- 🌍 **Multilingual Support** — Recognizes and responds in English, Greek, and phonetic Greeklish
- 👤 **Player Profiles** — Login system with persistent score tracking via JSON
- 💬 **Typewriter Animations** — Smooth character-by-character response rendering
- 📜 **Chat History** — In-app history window with session logging
- 🖥️ **Sleek Dark GUI** — Retro cyberpunk-inspired interface built with Tkinter
- ⚡ **Multithreaded Architecture** — Non-blocking responses for smooth performance

---

## 📸 Preview

**VER. 0.3 & 0.2**

![Preview 0.2-0.3](img_preview.png)

**VER. 0.4 & 0.4.1**

![Preview 0.4](img_preview.png)

**VER. 0.5 — 0.5.3**

![Preview 0.5](img_preview.png)


**VER. 0.6**
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/3ddd5bed-6f2f-419f-a2f2-5be1f0898317" />

&

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/20fa9bc7-72a0-4365-81e9-f1cde2a79075" />

---
## 🛠️ Requirements

- Python 3.8+
- Internet connection (first run only, to download the model)

---

## 📦 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/AlexKotsovolis/k0sh-ai.git
cd k0sh-ai
```

**2. Install dependencies:**
```bash
pip install sentence-transformers torch pillow langdetect
```

**3. Run the application:**
```bash
python Game.py
```

> **Note:** On first startup, the app will briefly download the `paraphrase-multilingual-MiniLM-L12-v2` model locally.

---

## 🎮 How to Play

1. Launch the app and enter your name when prompted
2. Chat with K0sh freely, or jump straight into a game
3. Type one of the game commands to start:

| Command | Game |
|---------|------|
| `GTN` | Guess the Number (0–100) |
| `RPS` | Rock-Paper-Scissors |
| `BLC` | Blackjack (dice to 21) |

---

## 🏗️ Project Structure

```
.
├── Game.py
├── userdata.json
├── Chat History.txt
├── K0sh2.png
├── README.md
└── requirements.txt
```

---

## 🔧 Built With

| Technology | Purpose |
|---|---|
| Python | Core application |
| Tkinter | Desktop GUI |
| Sentence-Transformers | Semantic NLP engine |
| PyTorch | Tensor computations |
| Threading | Non-blocking response streaming |
| JSON | Player data persistence |

---

## 🔒 License

K0sh AI is licensed under the **K0sh AI Personal Use License v1.0**.

**What you may do:**
- Use the software for personal, non-commercial purposes
- Modify the software for personal, non-commercial purposes

**What you may NOT do:**
- Commercialize, sell, or monetize the software
- Distribute, redistribute, publish, or share the software or modified versions
- Incorporate the software into distributed or commercial projects
- Remove copyright notices or author attribution

For full terms, see the `LICENSE` file included in this repository.

© 2026 Alex Kotsovolis. All rights reserved.

---

## 👨‍💻 Author

**Alex Kotsovolis**
- GitHub: [@AlexKotsovolis](https://github.com/AlexKotsovolis)
- Discord: @myboialex3

⭐ If you find this project useful, consider starring the repository.

*Built with Python, SentenceTransformers, and a lot of free time 🎮*

---

## 📋 UPDATE LOG

### What is the update log?
The update log is basically a file here in github, where I will be updating the text of the file, whenever a new version of K0sh or even of minor fixes/updates are posted. So, starting from now, 03/06/2026 i am releasing this log.

---

### Version 0.1 (RELEASE)
Released K0sh AI.

Simple "Guess the number" and "Chat".

Simple GUI.

Kinda boring... :(

---

### Version 0.2: (REWORK)
Reworked chat messages!

Cool UI and design! (Feel free to make suggestions if you want!)

NOTICE: Hey everyone! I have decided (from now on) to keep every version here in github, if anyone would like to use previous versions (with of course more coming soon). I think it is really cool, so next update, you can choose which version you like the most!

---

### Version: 0.3 : "One.. More.. Game!"
Introducing... Rock-Paper-Scissors! (NEW GAME MODE)

Really simple, maybe buggy.

New messages.

Next update is gonna be FIRE

Kept old version's code, as promised.

---

### Version: 0.4: "Wait.. I know you!" (what even are these names really)
Introducing our new feature... LOG-IN / PLAYER DATA!

New Point system!

New messages.

I have a headache...

New GUI, more professional-like and some gaming vibes! (It is going to change anytime soon, the GUI will never stay the same!)

Kept old version's code, as promised.

How it works: Make a new account (with a json which is already being made in the code), play, leave, rejoin, say your name and K0sh is going to know you know!

---

### Version 0.4.1 : "Threading"
Added threading, for a better experience.

Lagging? Not anymore! Threading is here.

Really small update, before version 0.5.

---

### Version: 0.5 "Another One."
Changed the GUI! (Scroll up to check the Image I pasted)

Added "Blackjack" game mode, which activates by sending the word "BLC", or "Blc", or even "blc"

Kept previous version's code, as promised

PLEASE NOTICE: This new game mode is not meant for MISUING (gambling), it is just for fun, and a way to spend time with your friend K0sh!

I will run out of ideas sometime, so please give me recommendations 🙏

---

### Version: 0.5.1 ("V.0.5, but enhanced GUI)
Really small update, but I added typewriter animations.

New message added, now you can ask K0sh for the latest updates.

Fixed Core Bugs on Version 0.5.1, today's version, because the typewriter update is a little buggy.

I am really sorry if you find any bugs, I will try to fix them ASAP.

Kept previous version's code, as promised.

---

### Version 0.5.2: "Multilingual"
K0sh AI now supports multiple languages! (Depending on which language you talk to him)

Please notice that there are still bugs in the program, and I am trying to find a solution for all of them.

Next Update coming in 1-2 weeks! (Sorry for the wait)

Kept previous version's code, as promised.

---

### Version 0.5.3: "QOL fixes!"
Hey everyone! I recently noticed that there was a massive bug and basically, when K0sh is answering, you could send something, thus breaking the entire answer.

For this reason, I decided to fix it, and enhance the q_a pairs, so that you can communicate more efficiently with K0sh.

Generally minor QOL changes.

Kept previous version's code, as promised.

Thanks for starring!

---
### Version 0.6: "???"
K0sh now keeps track of your conversations, by using a .txt file. You can now click the history button and see it!

Kept previous version's code, as promised.

Fixed Core issues/bugs in Blackjack and Guess the Number

Changed the GUI!

Please notice that there are still bugs in the program, and I am trying to find a solution for all of them.

Sorry for the wait!

WE FINALLY HIT 1K LINES!

---
### Next Version: (Coming soon!)
  Plans on what I am going to add in the future:
    - Achievements to users. For example: "You won your first game!". Those will be accessible in the .json file, where your name is and you can see it by asking K0sh for your achievements.
    - More, which I am not saying because I will spoil the next update.
---

`LINE COUNTER: 1008 (VER. 0.6.0)`

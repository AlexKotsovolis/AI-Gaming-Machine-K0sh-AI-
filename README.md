<div align="center">

<!-- HEADER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=K0sh%20AI&fontSize=80&fontColor=00d4ff&fontAlignY=38&desc=Semantic%20Chat%20%26%20Gaming%20Machine&descColor=a78bfa&descSize=22&descAlignY=62&animation=fadeIn" width="100%"/>

<br/>

<!-- BADGES -->
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Torch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Sentence Transformers](https://img.shields.io/badge/Sentence--BERT-Multilingual-8b5cf6?style=for-the-badge&logo=huggingface&logoColor=white)](https://www.sbert.net/)
[![License](https://img.shields.io/badge/License-K0sh%20Personal%20Use%20v1.0-00d4ff?style=for-the-badge)](./LICENCE)
[![Version](https://img.shields.io/badge/Version-0.6.2-a78bfa?style=for-the-badge)](#)
[![Stars](https://img.shields.io/github/stars/AlexKotsovolis/AI-Gaming-Machine-K0sh-AI-?style=for-the-badge&color=fbbf24&logo=github)](https://github.com/AlexKotsovolis/AI-Gaming-Machine-K0sh-AI-)

<br/>

> *Semantic. Multilingual. Built with love for one grumpy, magnificent cat.*

<br/>

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/AlexKotsovolis/AI-Gaming-Machine-K0sh-AI-)

</div>

---

<div align="center">
<img src="https://github.com/user-attachments/assets/6cb327cd-2d87-4973-a716-a66c2c0a3c70" width="80%" alt="K0sh AI Preview" style="border-radius: 12px;"/>
</div>

<br/>

## 🌐 What is K0sh AI?

**K0sh AI** is a fully local desktop AI chatbot and mini gaming platform — built from scratch in **pure Python**. It uses **Sentence-BERT** with cosine similarity to understand what you *mean*, not just what you *type*. Typos, slang, Greeklish — K0sh gets it.

No APIs. No subscriptions. No cloud. Just your machine, your model, and your moves.

---

## ✨ Feature Highlights

| | Feature | Description |
|---|---|---|
| 🧠 | **Semantic NLP** | Powered by `paraphrase-multilingual-MiniLM-L12-v2` for intent matching beyond keywords |
| 🌍 | **Multilingual** | Supports English, Greek, and phonetic Greeklish natively |
| 🎮 | **3 Game Modes** | Guess the Number · Rock-Paper-Scissors · Blackjack |
| 👤 | **Player Profiles** | Login system with persistent score tracking via JSON |
| 💬 | **Typewriter Replies** | Smooth character-by-character response animations |
| 📜 | **Chat History** | In-app history window with full session logging |
| 🖥️ | **Cyberpunk GUI** | Retro dark interface built with Tkinter |
| ⚡ | **Multithreaded** | Non-blocking UI — zero freezes during AI responses |
| 🏆 | **Achievements** | Unlock rewards as you play and chat |
| 💀 | **Broke State** | Go negative? K0sh won't let you forget it |

---

## 🎮 Game Modes

<div align="center">

| Command | Game | Description |
|:---:|:---:|:---|
| `GTN` | 🔢 Guess the Number | K0sh picks a number — can you crack it? |
| `RPS` | ✂️ Rock-Paper-Scissors | Classic. Instant. Competitive. |
| `BLC` | 🃏 Blackjack | The dice-based card challenge. Don't go broke. |

</div>

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Role |
|:---|:---|
| **Python 3.8+** | Core application logic |
| **Tkinter** | Desktop GUI & animations |
| **Sentence-Transformers** | Semantic NLP engine (SBERT) |
| **PyTorch** | Tensor computations for embeddings |
| **Threading** | Non-blocking UI architecture |
| **JSON** | Player data & score persistence |
| **LangDetect** | Runtime language detection |

</div>

---

## 🚀 Getting Started

### 1 — Clone the Repository

```bash
git clone https://github.com/AlexKotsovolis/AI-Gaming-Machine-K0sh-AI-.git
cd AI-Gaming-Machine-K0sh-AI-
```

### 2 — Install Dependencies

```bash
pip install sentence-transformers torch pillow langdetect
```

### 3 — Run the App

Navigate to the latest version folder and launch:

```bash
cd "CODE_VERSIONS/CODE (VER. 0.6.2)"
python k0sh_ai.py
```

> **⚠️ First Run Notice:** K0sh AI will download the `paraphrase-multilingual-MiniLM-L12-v2` model on first startup (~120MB). Internet connection required once.

---

## 📸 Screenshots

<div align="center">
<img src="https://github.com/user-attachments/assets/3ddd5bed-6f2f-419f-a2f2-5be1f0898317" width="80%" alt="K0sh AI Main Interface"/>
<br/><br/>
<img src="https://github.com/user-attachments/assets/20fa9bc7-72a0-4365-81e9-f1cde2a79075" width="80%" alt="K0sh AI Game Mode"/>
<br/><br/>
<img src="https://github.com/user-attachments/assets/4a0b7fdc-54ae-439f-8fd0-16471000cd4f" width="80%" alt="K0sh AI Chat"/>
<br/><br/>
<img width="1919" height="1079" alt="Screenshot 2026-06-16 111851" src="https://github.com/user-attachments/assets/8ef04085-2bd0-48f1-9b95-5157d0ac1a05" />
</div>

---

## 📋 Version History

<details>
<summary><strong>Click to expand full changelog</strong></summary>

<br/>

| Version | Codename | Highlights |
|:---:|:---|:---|
| `2.0` | GIANT UPDATE | Added strong frontend, removed the good old tkinter gui, so it is finally clean |
| `0.6.6` | Minor Fixes | Minor Fixes in the core code, bugs in BLC (from diffs) reworked achievements|
| `0.6.5` | ?! | After a long time, introduced difficulties, (more in releases) bug fixes and more QOL changes. |
| `0.6.4` | 🐛 | Basically version 0.6.3 (so sub-version), but with core bugs fixed and comms added (/stats, /ach) |
| `0.6.3` | ⚡ | Enhanced K0sh's answers, more q_a pairs, fixed core bugs (go see in releases) |
| `0.6.2` | 🏆 | Achievement system, animated loading screen, Broke state fixes |
| `0.6.1` | QOL | Secure data saving, history bug fix, harder Blackjack, Broke state |
| `0.6` | ??? | Chat history UI window, GUI overhaul, core bug fixes |
| `0.5.3` | QOL Fixes | Input lock during bot response, enhanced Q&A pairs |
| `0.5.2` | Multilingual | English, Greek, and Greeklish support |
| `0.5.1` | Enhanced GUI | Typewriter animations, core bug fixes |
| `0.5` | Another One | Blackjack (BLC) game mode, GUI refresh |
| `0.4.1` | Threading | Non-blocking multithreaded responses |
| `0.4` | Wait.. I know you! | Login system, player profiles, persistent scores |
| `0.3` | One.. More.. Game! | Rock-Paper-Scissors (RPS) added |
| `0.2` | Rework | Chat UI rework, version history tracking begins |
| `0.1` | Release | Initial release — Guess the Number + Chat |

</details>

---

## 🐱 The Inspiration

K0sh AI is named after a real cat. Here he is — the grumpy mastermind behind it all. (The images are not made with ai, they are completely real.)

<div align="center">
<img src="https://github.com/user-attachments/assets/feccb714-3670-4985-a1ac-b2e2b642ddc0" width="45%" alt="The real K0sh"/>
&nbsp;&nbsp;
<img src="https://github.com/user-attachments/assets/9d706290-6f8c-4cc3-8d93-a89b14c81363" width="45%" alt="K0sh, the original AI"/>
&nbsp;&nbsp;
<img width="3060" height="4080" alt="20260614_085406" src="https://github.com/user-attachments/assets/b106db8e-eb46-43aa-8418-82075b8505ad" />


*The original K0sh — he helped me code the project, as well as making my day. His name is Cinammon.*
</div>

---

## 🔒 License

This project is licensed under the **K0sh AI Personal Use License v1.0**.

- ✅ You **may**: Use and modify the software for personal, non-commercial purposes.
- ❌ You **may NOT**: Commercialize, sell, distribute, or republish the software or modified versions.

For full terms, see the [`LICENCE`](./LICENCE) file. © 2026 Alex Kotsovolis. All rights reserved.

---

## 👨‍💻 Author

<div align="center">

**Alex Kotsovolis**

[![GitHub](https://img.shields.io/badge/GitHub-@AlexKotsovolis-181717?style=for-the-badge&logo=github)](https://github.com/AlexKotsovolis)
[![Discord](https://img.shields.io/badge/Discord-@myboialex3-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/)

<br/>

*If K0sh AI made you smile, smash that ⭐ — it means a lot!*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>

</div>

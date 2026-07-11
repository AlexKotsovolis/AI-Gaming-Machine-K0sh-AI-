const ACHIEVEMENTS2 = [
  { id: "Ten Wins",         label: "First Streak", desc: "Win 10 games" },
  { id: "Fifty Wins",       label: "Fifty Strong",  desc: "Win 50 games" },
  { id: "One Hundred Wins", label: "Centurion",     desc: "Win 100 games" },
  { id: "High Roller",      label: "High Roller",   desc: "Score 10,000+ pts" },
  { id: "Legend",           label: "Legend",        desc: "Score 100,000+ pts" },
  { id: "Millionaire",      label: "Millionaire",   desc: "Score 1,000,000+ pts" },
  { id: "Blackjack Master", label: "BLC Master",    desc: "Win 50 Blackjack rounds" },
  { id: "Veteran Gamer",    label: "Veteran",       desc: "Play 100 games total" },
];

let playerName = null;
let registered = false;
let activeGame = null;

const messagesEl    = document.getElementById("messages2");
const inputEl        = document.getElementById("text-input2");
const sendBtn         = document.getElementById("send-btn2");
const micBtn          = document.getElementById("mic-btn2");
const playerPill      = document.getElementById("player-pill");
const playerPillName  = document.getElementById("player-pill-name");
const playerPillScore = document.getElementById("player-pill-score");
const badgeEl         = document.getElementById("game-badge2");

function addMessage(sender, text) {
  const div = document.createElement("div");
  div.className = `msg2 ${sender}`;
  if (sender === "bot") {
    const tag = document.createElement("div");
    tag.className = "msg2-tag";
    tag.textContent = "K0SH";
    div.appendChild(tag);
  }
  div.appendChild(document.createTextNode(text));
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function setActiveGame(game) {
  activeGame = game;
  document.querySelectorAll(".game-tile").forEach(t => {
    t.classList.toggle("active", t.dataset.game === game);
  });
  if (game) {
    badgeEl.style.display = "inline-block";
    badgeEl.textContent = game + " · in progress";
  } else {
    badgeEl.style.display = "none";
  }
}

function updateStatsPanel(data) {
  if (!data) return;
  document.getElementById("stat-score2").textContent  = (data.InGameScore ?? 0).toLocaleString();
  document.getElementById("stat-games2").textContent  = data.Games ?? 0;
  document.getElementById("stat-wins2").textContent   = data.Wins ?? 0;
  document.getElementById("stat-losses2").textContent = data.Losses ?? 0;
  document.getElementById("stat-draws2").textContent  = data.Draws ?? 0;
  document.getElementById("stat-blcw2").textContent   = data.BLCW ?? 0;
  document.getElementById("win-streak2").textContent  = data.Wins ?? 0;

  playerPillScore.textContent = (data.InGameScore ?? 0).toLocaleString() + " pts";
  playerPillScore.style.color = (data.InGameScore ?? 0) < 0 ? "var(--red)" : "var(--green)";

  renderAchievements(data);
}

function renderAchievements(data) {
  const unlocked = new Set(data.Achievements || []);
  const listEl = document.getElementById("ach-list2");
  listEl.innerHTML = "";
  ACHIEVEMENTS2.forEach(a => {
    const isUnlocked = unlocked.has(a.id);
    const item = document.createElement("div");
    item.className = "ach-item2" + (isUnlocked ? " unlocked" : "");
    item.innerHTML = `
      <div>
        <div class="ach-name2${isUnlocked ? "" : " locked"}">${a.label}</div>
        <div class="muted" style="font-size:10px; color: var(--muted);">${a.desc}</div>
      </div>
      ${isUnlocked ? '<div class="ach-check2">DONE</div>' : ""}
    `;
    listEl.appendChild(item);
  });
}

function inferGameStateFromReply(text) {
  const upper = text.toUpperCase();
  if (/PICK A DIFFICULTY/.test(upper)) { setActiveGame(null); return; }
  if (/HAVE \d+ TRIES/.test(upper))    { setActiveGame("GTN"); return; }
  if (/ENTER YOUR MOVE TO BEGIN/.test(upper)) { setActiveGame("RPS"); return; }
  if (/TYPE 'HIT' TO ROLL AGAIN/.test(text))   { setActiveGame("BLC"); return; }
  if (/LETTER BY LETTER|LIVES:\s*\d+/.test(upper)) { setActiveGame("HMN"); return; }
  if (/THE WORD WAS/.test(upper)) { setActiveGame(null); return; }
  if (/PLAY AGAIN!|TRY AGAIN!|FOR ANOTHER ROUND!|CHOOSE GTN \/ RPS!/.test(text)) {
    setActiveGame(null);
  }
}

async function handleSend() {
  const text = inputEl.value.trim();
  if (!text) return;
  inputEl.value = "";

  if (!registered) {
    addMessage("user", text);
    const result = await window.pywebview.api.register(text);
    if (result.ok) {
      playerName = text;
      registered = true;
      playerPill.style.display = "flex";
      playerPillName.textContent = playerName.toUpperCase();
      document.getElementById("stat-name2").textContent = playerName.toUpperCase();
      inputEl.placeholder = "Chat or type GTN / RPS / BLC / HMN...";
      const data = await window.pywebview.api.get_data(playerName);
      updateStatsPanel(data);
    }
    addMessage("bot", result.response);
    return;
  }

  addMessage("user", text);
  const result = await window.pywebview.api.send_message(playerName, text);
  addMessage("bot", result.response);
  if (result.player_data) updateStatsPanel(result.player_data);
  inferGameStateFromReply(result.response);
}

sendBtn.addEventListener("click", handleSend);
inputEl.addEventListener("keydown", e => { if (e.key === "Enter") handleSend(); });

document.querySelectorAll(".game-tile").forEach(tile => {
  tile.addEventListener("click", () => {
    if (!registered) {
      // Switch to chat tab and prompt
      document.querySelector('.rail-btn[data-tab="chat"]').click();
      addMessage("bot", "Enter your name first to start playing!");
      return;
    }
    document.querySelector('.rail-btn[data-tab="chat"]').click();
    inputEl.value = tile.dataset.game;
    handleSend();
  });
});

// ───────── Rail tab switching ─────────
document.querySelectorAll(".rail-btn[data-tab]").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".rail-btn[data-tab]").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    const tab = btn.dataset.tab;
    document.getElementById("pane-chat").style.display    = tab === "chat"    ? "flex" : "none";
    document.getElementById("pane-games").style.display   = tab === "games"   ? "flex" : "none";
    document.getElementById("pane-profile").style.display = tab === "profile" ? "flex" : "none";
  });
});

// ───────── History modal ─────────
const historyModal   = document.getElementById("history-modal");
const historyContent = document.getElementById("history-content");

document.getElementById("history-btn").addEventListener("click", async () => {
  const result = await window.pywebview.api.get_chat_history();
  historyContent.textContent = result.history;
  historyModal.style.display = "flex";
});
document.getElementById("history-close").addEventListener("click", () => {
  historyModal.style.display = "none";
});
historyModal.addEventListener("click", (e) => {
  if (e.target === historyModal) historyModal.style.display = "none";
});
document.getElementById("history-erase-btn").addEventListener("click", async () => {
  await window.pywebview.api.erase_chat_history();
  historyContent.textContent = "No chat history yet.";
});

// ───────── Leave button ─────────
document.getElementById("leave-btn").addEventListener("click", async () => {
  await window.pywebview.api.quit_app();
});

// ───────── Voice input (mic button) ─────────
(function setupVoiceInput() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    micBtn.classList.add("unsupported");
    micBtn.title = "Voice input not supported in this window";
    micBtn.addEventListener("click", () => {
      addMessage("system", "Voice input isn't available in this environment.");
    });
    return;
  }

  const recognition = new SpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = true;
  recognition.lang = "en-US"; // change to "el-GR", "es-ES", "fr-FR", "de-DE", "it-IT" etc. if you prefer

  let listening = false;

  recognition.onstart = () => {
    listening = true;
    micBtn.classList.add("listening");
    micBtn.textContent = "⏺";
  };

  recognition.onresult = (event) => {
    let transcript = "";
    for (let i = 0; i < event.results.length; i++) {
      transcript += event.results[i][0].transcript;
    }
    inputEl.value = transcript;
  };

  recognition.onerror = (event) => {
    addMessage("system", `Voice input error: ${event.error}`);
  };

  function stopListening() {
    listening = false;
    micBtn.classList.remove("listening");
    micBtn.textContent = "🎤";
  }

  recognition.onend = () => {
    stopListening();
    if (inputEl.value.trim()) handleSend();
  };

  micBtn.addEventListener("click", () => {
    if (listening) {
      recognition.stop();
    } else {
      inputEl.value = "";
      try {
        recognition.start();
      } catch (err) {
        addMessage("system", "Couldn't start the microphone. Check your system mic permissions.");
      }
    }
  });
})();

// Initial greeting
addMessage("system", "K0SH AI — EMBER THEME\nHello! I'm K0sh, your digital game master.\nBefore we start — what's your name?");

const ACHIEVEMENTS = [
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
let activeGame = null; // "GTN" | "RPS" | "BLC" | null

const messagesEl   = document.getElementById("messages");
const inputEl       = document.getElementById("text-input");
const sendBtn        = document.getElementById("send-btn");
const playerChip     = document.getElementById("player-chip");
const playerChipName = document.getElementById("player-chip-name");
const playerChipScore= document.getElementById("player-chip-score");
const badgeEl        = document.getElementById("active-game-badge");

function addMessage(sender, text) {
  const div = document.createElement("div");
  div.className = `msg ${sender}`;
  if (sender === "bot") {
    const tag = document.createElement("div");
    tag.className = "msg-tag";
    tag.textContent = "K0SH";
    div.appendChild(tag);
  }
  div.appendChild(document.createTextNode(text));
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function setActiveGame(game) {
  activeGame = game;
  document.querySelectorAll(".game-card").forEach(c => {
    c.classList.toggle("active", c.dataset.game === game);
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
  document.getElementById("stat-score").textContent  = (data.InGameScore ?? 0).toLocaleString();
  document.getElementById("stat-games").textContent  = data.Games ?? 0;
  document.getElementById("stat-wins").textContent   = data.Wins ?? 0;
  document.getElementById("stat-losses").textContent = data.Losses ?? 0;
  document.getElementById("stat-draws").textContent  = data.Draws ?? 0;
  document.getElementById("stat-blcw").textContent   = data.BLCW ?? 0;

  const streakEl = document.getElementById("win-streak-number");
  streakEl.textContent = data.Wins ?? 0;
  streakEl.classList.toggle("has-wins", (data.Wins ?? 0) > 0);

  playerChipScore.textContent = (data.InGameScore ?? 0).toLocaleString() + " pts";
  playerChipScore.style.color = (data.InGameScore ?? 0) < 0 ? "var(--red)" : "var(--green)";

  renderAchievements(data);
}

function renderAchievements(data) {
  const unlocked = new Set(data.Achievements || []);
  const listEl = document.getElementById("ach-list");
  listEl.innerHTML = "";
  ACHIEVEMENTS.forEach(a => {
    const isUnlocked = unlocked.has(a.id);
    const item = document.createElement("div");
    item.className = "ach-item" + (isUnlocked ? " unlocked" : "");
    item.innerHTML = `
      <div style="flex:1;">
        <div class="ach-name${isUnlocked ? "" : " locked"}">${a.label}</div>
        <div class="muted small">${a.desc}</div>
      </div>
      ${isUnlocked ? '<div class="ach-check">DONE</div>' : ""}
    `;
    listEl.appendChild(item);
  });
}

// Detect which game just finished / started, purely from the message text,
// so the UI badge stays in sync (Python doesn't need to expose extra state for this).
function inferGameStateFromReply(text, wasReplyTo) {
  const upper = text.toUpperCase();
  if (/PICK A DIFFICULTY/.test(upper)) { setActiveGame(null); return; }
  if (/HAVE \d+ TRIES/.test(upper))    { setActiveGame("GTN"); return; }
  if (/ENTER YOUR MOVE TO BEGIN/.test(upper)) { setActiveGame("RPS"); return; }
  if (/TYPE 'HIT' TO ROLL AGAIN/.test(text))   { setActiveGame("BLC"); return; }
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
      playerChip.style.display = "flex";
      playerChipName.textContent = playerName.toUpperCase();
      document.getElementById("stat-name").textContent = playerName.toUpperCase();
      inputEl.placeholder = "Chat or type GTN / RPS / BLC...";
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

document.querySelectorAll(".game-card").forEach(card => {
  card.addEventListener("click", () => {
    if (!registered) {
      addMessage("bot", "Enter your name first to start playing!");
      return;
    }
    inputEl.value = card.dataset.game;
    handleSend();
  });
});

document.querySelectorAll(".tab-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    const tab = btn.dataset.tab;
    document.getElementById("panel-stats").style.display = tab === "stats" ? "flex" : "none";
    document.getElementById("panel-achievements").style.display = tab === "achievements" ? "flex" : "none";
  });
});

document.getElementById("clear-btn").addEventListener("click", () => {
  messagesEl.innerHTML = "";
  addMessage("system", playerName ? `Chat cleared. Keep playing, ${playerName}!` : "Chat cleared.");
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

// Initial greeting
addMessage("system", "K0SH AI — DESKTOP\nHello! I'm K0sh, your digital game master.\nBefore we start — what's your name?");

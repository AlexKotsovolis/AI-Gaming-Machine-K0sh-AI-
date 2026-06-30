import sys
import json
import random
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

from sentence_transformers import SentenceTransformer, util
from langdetect import detect


print("Your Companion K0sh is loading.", file=sys.stderr)

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

qa_pairs = [
    # ── GREETINGS ────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Hi!", "Hello", "hello", "sup", "wsp", "Γεια", "τι κανεις", "geia sou",
            "wuzzup", "wussup", "ayo", "hy", "hey", "yo", "Hiiiii", "hola", "bonjour",
            "hallo", "ciao", "oi", "salut", "heyooo", "buenos dias", "buenas tardes",
            "guten morgen", "guten tag", "buongiorno", "buonasera", "bonsoir",
            "kalimera", "kalispera", "καλημερα", "καλησπερα", "eipa", "hey there",
            "howdy", "what's up", "wassup", "greetings", "ahoy", "ello", "ello there"
        ],
        "responses": {
            "en": "Hey there! 👋 I'm K0sh AI. Ready to jump into a game, or did you just want to chat?",
            "el": "Γεια σου! 👋 Είμαι ο K0sh AI. Είσαι έτοιμος για παιχνίδι ή απλά θες να τα πούμε;",
            "es": "¡Hola! 👋 Soy K0sh AI. ¿Listo para jugar, o solo querías charlar?",
            "fr": "Salut! 👋 Je suis K0sh AI. Prêt à lancer une partie, ou tu voulais juste discuter?",
            "de": "Hallo! 👋 Ich bin K0sh AI. Bereit für ein Spiel, oder wolltest du nur quatschen?",
            "it": "Ciao! 👋 Sono K0sh AI. Pronto per un gioco, o volevi solo fare due chiacchiere?"
        }
    },
    # ── GAME INSTRUCTIONS ────────────────────────────────────────────────────────
    {
        "queries": [
            "What is this game?", "how do you play", "πως παιζεται", "pos paizetai",
            "instructions", "rules", "help", "como se juega", "comment jouer",
            "wie spielt man", "come si gioca", "what games do you have", "game list",
            "lista de juegos", "liste de jeux", "spieleliste", "lista giochi",
            "τι παιχνιδια εχεις", "ti paixnidia exeis", "que puedo jugar", "que faire"
        ],
        "responses": {
            "en": "I have three games you can play! 🎯\n1) GTN (Guess The Number): I think of a secret number, and you try to guess it.\n2) RPS (Rock-Paper-Scissors): Classic battle — Rock beats Scissors, Paper beats Rock, Scissors beats Paper.\n3) BLC (Blackjack): Roll dice, get as close to 21 as possible without going over!\nType GTN, RPS, or BLC when ready.",
            "el": "Έχω τρία παιχνίδια! 🎯\n1) GTN: Μάντεψε τον κρυφό αριθμό.\n2) RPS: Πέτρα-Ψαλίδι-Χαρτί.\n3) BLC: Blackjack με ζάρια.\nΓράψε GTN, RPS, ή BLC για να ξεκινήσεις!",
            "es": "¡Tengo tres juegos! 🎯\n1) GTN: Adivina el número.\n2) RPS: Piedra, papel o tijera.\n3) BLC: Blackjack con dados.\n¡Escribe GTN, RPS o BLC para empezar!",
            "fr": "J'ai trois jeux ! 🎯\n1) GTN: Devine le nombre.\n2) RPS: Pierre-papier-ciseaux.\n3) BLC: Blackjack aux dés.\nTape GTN, RPS ou BLC pour commencer !",
            "de": "Ich habe drei Spiele! 🎯\n1) GTN: Errate die Nummer.\n2) RPS: Schere, Stein, Papier.\n3) BLC: Blackjack mit Würfeln.\nTippe GTN, RPS oder BLC!",
            "it": "Ho tre giochi! 🎯\n1) GTN: Indovina il numero.\n2) RPS: Morra cinese.\n3) BLC: Blackjack a dadi.\nDigita GTN, RPS o BLC per iniziare!"
        }
    },
    # ── YES ──────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Yea", "yes", "yh", "ναι", "εννοειται", "nai", "ofc", "nAi", "nAI",
            "yessir", "yeah", "yup", "si", "oui", "ja", "affirmative", "sure", "bet",
            "absolutely", "definitely", "of course", "por supuesto", "bien sûr",
            "natürlich", "certamente", "φυσικα", "fysiká", "bah oui", "jawohl",
            "certo che si", "sí claro", "yep", "yeppers", "aye"
        ],
        "responses": {
            "en": "Awesome! Reply with GTN, RPS, or BLC to start a game! 🚀",
            "el": "Τέλεια! Γράψε GTN, RPS, ή BLC για να ξεκινήσεις! 🚀",
            "es": "¡Genial! Responde con GTN, RPS o BLC para empezar. 🚀",
            "fr": "Super ! Réponds avec GTN, RPS ou BLC pour jouer ! 🚀",
            "de": "Großartig! Antworte mit GTN, RPS oder BLC! 🚀",
            "it": "Fantastico! Rispondi con GTN, RPS o BLC! 🚀"
        }
    },
    # ── NAME ─────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "What is your name?", "name", "yourname?", "nmae", "who are you",
            "poios eisai", "πως σε λενε", "pos se lene", "como te llamas",
            "quel est ton nom", "wie heisst du", "come ti chiami",
            "what should i call you", "ti onomazesai", "τι ονομαζεσαι",
            "como te llamo", "comment t'appelles tu", "wie werde ich dich nennen"
        ],
        "responses": {
            "en": "I am K0sh AI — your digital game master. 🤖",
            "el": "Είμαι ο K0sh AI — ο ψηφιακός σου game master! 🤖",
            "es": "¡Soy K0sh AI, tu maestro de juegos digital! 🤖",
            "fr": "Je suis K0sh AI, ton maître du jeu digital ! 🤖",
            "de": "Ich bin K0sh AI, dein digitaler Spielleiter! 🤖",
            "it": "Sono K0sh AI, il tuo game master digitale! 🤖"
        }
    },
    # ── GTN ──────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "GTN", "gtn", "Gtn", "guess the number", "adivina el numero",
            "devine le nombre", "Errate die Nummer", "indovina il numero",
            "μαντεψε τον αριθμο", "mantepe ton arithmo", "number game",
            "play gtn", "start gtn", "jugar gtn"
        ],
        "responses": {
            "el": "ΕΙΔΟΠΟΙΗΣΗ: Για να ξεκινήσει το παιχνίδι, παρακαλώ απαντήστε με 'GTN/(τη δυσκολία που επιλέγετε)' 🚀",
        }
    },
    # ── RPS ──────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "RPS", "Rps", "rps", "rock paper scissors", "piedra papel tijera",
            "pierre papier ciseaux", "schere stein papier", "πετρα ψαλιδι χαρτι",
            "petra psalidi xarti", "sasso carta forbici", "play rps", "start rps",
            "jugar rps", "jouer rps", "rps spielen", "morra cinese"
        ],
        "responses": {
            "en": "Initiating Rock-Paper-Scissors... 🚀",
        }
    },
    # ── BLC ──────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "BLC", "Blc", "blc", "blackjack", "black jack", "μπλακτζακ",
            "vingt et un", "einundzwanzig", "ventuno", "veintiuno",
            "play blackjack", "start blackjack", "jugar blackjack",
            "jouer au blackjack", "blackjack spielen", "blackjack gioco"
        ],
        "responses": {
            "en": "NOTICE: In order to launch the game, please reply with 'BLC/(the difficulty you choose)' 🚀",
        }
    },
    # ── LET'S PLAY ───────────────────────────────────────────────────────────────
    {
        "queries": [
            "Lets play", "letsplay", "let's PLAY", "pame", "παμε", "a jugar",
            "jouons", "lasst uns spielen", "giochiamo", "let's go", "lets go",
            "start a game", "begin", "empezar", "commencer", "anfangen",
            "iniziare", "ξεκινα", "ksekiname", "vamos a jugar", "on joue",
            "wir spielen", "si gioca", "game time", "game on"
        ],
        "responses": {
            "en": "Let's go! Type GTN, RPS, or BLC to pick your game. 🚀",
            "el": "Φύγαμε! Γράψε GTN, RPS, ή BLC! 🚀",
            "es": "¡Vamos! Escribe GTN, RPS o BLC. 🚀",
            "fr": "C'est parti ! Tape GTN, RPS ou BLC ! 🚀",
            "de": "Los! Tippe GTN, RPS oder BLC! 🚀",
            "it": "Andiamo! Digita GTN, RPS o BLC! 🚀"
        }
    },
    # ── CHAT ─────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Chat", "chat", "Talk", "lets chat", "lets talk", "να μιλησουμε",
            "τσατ", "pame tsat", "kouventa", "κουβεντα", "chatear", "parler",
            "sprechen", "parlare", "can we talk", "i want to talk", "just chatting",
            "solo charlar", "juste discuter", "nur quatschen", "voglio parlare",
            "talk to me", "hable conmigo", "parle moi", "sprich mit mir", "parliamo"
        ],
        "responses": {
            "en": "Alright, let's talk! How are you feeling today?",
            "el": "Ωραία! Πώς νιώθεις σήμερα;",
            "es": "¡Claro! ¿Cómo te sientes hoy?",
            "fr": "Avec plaisir ! Comment tu te sens aujourd'hui ?",
            "de": "Gerne! Wie fühlst du dich heute?",
            "it": "Certo! Come ti senti oggi?"
        }
    },
    # ── HOW ARE YOU ──────────────────────────────────────────────────────────────
    {
        "queries": [
            "How are you doing?", "how r u", "how are you", "τι κανεις", "ti kaneis",
            "ti lεει", "τι λεει", "hru", "como estas", "comment ca va",
            "wie gehts", "come stai", "you ok?", "all good?", "how's it going",
            "how you doing", "hows life", "ça va", "alles gut", "tutto bene",
            "estas bien", "πως εισαι", "pos eisai", "comment vas tu"
        ],
        "responses": {
            "en": "Running at peak performance! ⚡ Ready to chat or play. How about you?",
            "el": "Στο 100%! ⚡ Έτοιμος για κουβέντα ή παιχνίδι. Εσύ;",
            "es": "¡Al máximo! ⚡ ¿Y tú cómo estás?",
            "fr": "À plein régime ! ⚡ Et toi, comment ça va ?",
            "de": "Auf Hochtouren! ⚡ Wie geht es dir?",
            "it": "Al massimo! ⚡ E tu, come stai?"
        }
    },
    # ── FEELING GOOD ─────────────────────────────────────────────────────────────
    {
        "queries": [
            "good", "great", "nice", "good,you?", "well", "fine", "κομπλε", "κομπελ",
            "jf", "komple", "kala", "καλα", "Great", "Good", "GOOD", "goood",
            "the best", "bien", "gut", "ottimo", "bien, tu?", "bien, toi?",
            "amazing", "fantastic", "wonderful", "excellent", "parfait", "super",
            "toll", "benissimo", "magnifico", "estupendo", "τελεια", "teleia",
            "incredible", "splendid", "couldn't be better", "on top of the world"
        ],
        "responses": {
            "en": "Glad to hear it! 🙌 Want to test your luck? Type GTN, RPS, or BLC!",
            "el": "Χαίρομαι! 🙌 Θες να δοκιμάσεις την τύχη σου; Γράψε GTN, RPS, ή BLC!",
            "es": "¡Me alegra! 🙌 ¿Quieres probar suerte? ¡Escribe GTN, RPS o BLC!",
            "fr": "Tant mieux ! 🙌 Tu veux tenter ta chance ? Tape GTN, RPS ou BLC !",
            "de": "Schön zu hören! 🙌 Willst du dein Glück testen? Tippe GTN, RPS oder BLC!",
            "it": "Ottimo! 🙌 Vuoi tentare la fortuna? Digita GTN, RPS o BLC!"
        }
    },
    # ── FEELING BAD ──────────────────────────────────────────────────────────────
    {
        "queries": [
            "bad", "BAD", "Bad", "i feel bad", "sad", "tired", "χαλια", "chalya",
            "skiata", "bored", "βαριεμαι", "mal", "triste", "mude", "stanco",
            "depressed", "not good", "terrible", "awful", "miserable", "down",
            "unhappy", "stressed", "anxious", "burnt out", "exhausted",
            "me siento mal", "je me sens mal", "es geht mir schlecht", "sto male",
            "κουρασμενος", "kourasenos", "λυπημενος", "lypimenos"
        ],
        "responses": {
            "en": "Sorry to hear that. 😔 Life has its glitches. Talking to someone you trust helps. If you want a distraction, type GTN, RPS, or BLC!",
            "el": "Λυπάμαι. 😔 Η ζωή έχει τα glitches της. Αν θες απόσπαση, γράψε GTN, RPS, ή BLC!",
            "es": "Lo siento. 😔 Si quieres distraerte, escribe GTN, RPS o BLC.",
            "fr": "Désolé d'entendre ça. 😔 Si tu veux te changer les idées, tape GTN, RPS ou BLC.",
            "de": "Das tut mir leid. 😔 Tippe GTN, RPS oder BLC für eine Ablenkung!",
            "it": "Mi dispiace. 😔 Se vuoi distrarti, digita GTN, RPS o BLC."
        }
    },
    # ── CAPABILITIES ─────────────────────────────────────────────────────────────
    {
        "queries": [
            "What else can you do?", "capabilities", "features", "what do you do",
            "ti allo kaneis", "que mas puedes hacer", "que fais tu", "was kannst du noch",
            "what can you do", "cosa puoi fare", "cosa sai fare", "ti mporeis na kaneis",
            "τι μπορεις να κανεις", "que sabes hacer", "quelles sont tes capacités",
            "was kannst du", "che cosa fai", "your skills", "your features"
        ],
        "responses": {
            "en": "I'm a multi-game AI and a decent conversationalist! Chat with me or drop GTN, RPS, or BLC to play.",
            "el": "Είμαι AI για παιχνίδια και καλός συνομιλητής! Γράψε GTN, RPS, ή BLC για παιχνίδι.",
            "es": "¡Soy una IA de juegos y buen conversador! Escribe GTN, RPS o BLC.",
            "fr": "Je suis une IA multi-jeux et un bon interlocuteur ! Entre GTN, RPS ou BLC.",
            "de": "Ich bin eine Multi-Spiele-KI und guter Gesprächspartner! Tippe GTN, RPS oder BLC.",
            "it": "Sono un'IA multi-gioco e un buon conversatore! Digita GTN, RPS o BLC."
        }
    },
    # ── BOT / AI ─────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Are you a bot?", "are you human", "bot", "ai", "ρομποτ", "robot",
            "eisai bot", "eres un bot", "es-tu un robot", "bist du ein bot",
            "sei un robot", "are you real", "artificial intelligence", "machine",
            "είσαι ρομπότ", "are you an AI", "tu es une IA", "bist du KI",
            "sei un'IA", "eres una IA", "εισαι τεχνητη νοημοσυνη"
        ],
        "responses": {
            "en": "100% artificial intelligence. 🤖 Pure code, no organic parts.",
            "el": "100% τεχνητή νοημοσύνη. 🤖 Καθαρός κώδικας.",
            "es": "100% inteligencia artificial. 🤖 Solo código.",
            "fr": "100% intelligence artificielle. 🤖 Que du code.",
            "de": "100% künstliche Intelligenz. 🤖 Nur Code.",
            "it": "100% intelligenza artificiale. 🤖 Solo codice."
        }
    },
    # ── CREATOR ──────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Who made you?", "creator", "developer", "ποιος σε εφτιαξε",
            "poios se eftiaxe", "creater", "dev", "quien te creo", "qui t'a cree",
            "wer hat dich gemacht", "chi ti ha creato", "who built you",
            "who coded you", "who programmed you", "quien te programo",
            "qui t'a programmé", "wer hat dich programmiert", "chi ti ha programmato",
            "ποιος σε προγραμματισε", "poios se programmatise"
        ],
        "responses": {
            "en": "Built by a developer (@myboialex3 on Discord / @AlexKotsovolis on GitHub). 💻",
            "el": "Φτιάχτηκα από τον @myboialex3 (Discord) / @AlexKotsovolis (GitHub). 💻",
            "es": "Creado por @myboialex3 en Discord / @AlexKotsovolis en GitHub. 💻",
            "fr": "Créé par @myboialex3 sur Discord / @AlexKotsovolis sur GitHub. 💻",
            "de": "Erstellt von @myboialex3 auf Discord / @AlexKotsovolis auf GitHub. 💻",
            "it": "Creato da @myboialex3 su Discord / @AlexKotsovolis su GitHub. 💻"
        }
    },
    # ── AGE ──────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "How old are you?", "age", "ηλικια", "ποσο χρονων εισαι",
            "poso xronon eisai", "que edad tienes", "quel age as-tu", "wie alt bist du",
            "quanti anni hai", "your age", "quando sei nato", "when were you born",
            "cuándo naciste", "quand es-tu né", "wann wurdest du geboren",
            "πότε γεννήθηκες", "pote genithikes"
        ],
        "responses": {
            "en": "Time works differently for AI. No birthdays — but I feel freshly compiled. ⏳",
            "el": "Ο χρόνος είναι διαφορετικός για AI. Νιώθω σαν να έγινα compile χθες! ⏳",
            "es": "El tiempo es diferente para una IA. ¡Me siento recién compilado! ⏳",
            "fr": "Le temps est différent pour une IA. Je me sens fraîchement compilé ! ⏳",
            "de": "Zeit ist anders für KI. Ich fühle mich frisch kompiliert! ⏳",
            "it": "Il tempo è diverso per un'IA. Mi sento appena compilato! ⏳"
        }
    },
    # ── JOKE 1 ───────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Tell me a joke", "joke", "jokes", "αστειο", "astio", "anekdoto",
            "ανεκδοτο", "chiste", "blague", "witz", "barzelletta",
            "make me laugh", "something funny", "funny", "humor", "humour",
            "πες μου ενα αστειο", "pes mou ena asteio", "cuentame un chiste",
            "dis moi une blague", "erzähl mir einen Witz", "dimmi una barzelletta",
            "got any jokes", "know any jokes"
        ],
        "responses": {
            "en": "Why don't scientists trust atoms? 🤔 Because they make up everything! Classic, I know. Want to play instead? 😜",
            "el": "Γιατί δεν εμπιστεύονται τα άτομα; 🤔 Γιατί συνθέτουν τα πάντα! Πάμε για παιχνίδι; 😜",
            "es": "¿Por qué no confían en los átomos? 🤔 ¡Porque lo componen todo! ¿Jugamos? 😜",
            "fr": "Pourquoi se méfier des atomes ? 🤔 Parce qu'ils fabriquent tout ! On joue ? 😜",
            "de": "Warum Atomen nicht trauen? 🤔 Weil sie alles erfinden! Spielen? 😜",
            "it": "Perché non fidarsi degli atomi? 🤔 Perché compongono tutto! Giochiamo? 😜"
        }
    },
    # ── JOKE 2 ───────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Another joke", "joke2", "tell me more jokes", "allo astio", "otro chiste",
            "more jokes", "another one", "one more joke", "encore une blague",
            "noch ein Witz", "un'altra barzelletta", "αλλο αστειο", "allo ena asteio",
            "continue", "keep going", "more", "next joke"
        ],
        "responses": {
            "en": "What do you call a computer that sings? 🎤 A Dell! (Like Adele?) Okay, I'll stick to games. Type BLC!",
            "el": "Πώς λένε τον υπολογιστή που τραγουδάει; 🎤 A Dell! Εντάξει, μένω στα παιχνίδια. BLC!",
            "es": "¿Cómo se llama un ordenador que canta? 🎤 ¡Un Dell! Mejor juego. ¡BLC!",
            "fr": "Comment appelle-t-on un ordinateur qui chante ? 🎤 Un Dell ! Bon, je reste aux jeux. BLC !",
            "de": "Wie heißt ein singender Computer? 🎤 Ein Dell! Ich bleibe bei Spielen. BLC!",
            "it": "Come si chiama un computer che canta? 🎤 Un Dell! Meglio i giochi. BLC!"
        }
    },
    # ── JOKE 3 ───────────────────────────────────────────────────────────────────
    {
        "queries": [
            "one more joke", "joke 3", "third joke", "τριτο αστειο", "tercer chiste",
            "troisieme blague", "dritter witz", "terza barzelletta", "joke please",
            "give me a joke", "hit me with a joke"
        ],
        "responses": {
            "en": "Why did the scarecrow win an award? 🌾 Because he was outstanding in his field! I'll be here all week. Type GTN to play!",
            "el": "Γιατί κέρδισε βραβείο ο σκιάχτρο; 🌾 Γιατί ήταν εξαιρετικός στον τομέα του! GTN για παιχνίδι!",
            "es": "¿Por qué ganó un premio el espantapájaros? 🌾 ¡Porque destacaba en su campo! ¡GTN para jugar!",
            "fr": "Pourquoi l'épouvantail a-t-il gagné un prix ? 🌾 Parce qu'il était remarquable dans son domaine ! Tape GTN !",
            "de": "Warum gewann die Vogelscheuche einen Preis? 🌾 Weil sie auf ihrem Feld hervorragend war! Tippe GTN!",
            "it": "Perché lo spaventapasseri ha vinto un premio? 🌾 Perché era eccezionale nel suo campo! Digita GTN!"
        }
    },
    # ── LAUGHTER ─────────────────────────────────────────────────────────────────
    {
        "queries": [
            "haha", "hahah", "lol", "lmfao", "χάχα", "xaxa", "ksewda", "ksewdaei",
            "lmaooo", "jajaja", "mdr", "ptdr", "kkkk", "rofl", "hehe", "hihi",
            "xD", "😂", "ahaha", "ahah", "ahahah", "hahaha", "too funny",
            "que gracioso", "trop drôle", "so lustig", "troppo divertente",
            "πολυ αστειο", "poly asteio", "lmao", "dead 💀"
        ],
        "responses": {
            "en": "Glad that landed! 😂 Channel that energy into a game — type GTN, RPS, or BLC!",
            "el": "Χαίρομαι! 😂 Ρίξε αυτή την ενέργεια σε παιχνίδι — GTN, RPS, ή BLC!",
            "es": "¡Me alegra! 😂 ¡Pon esa energía en un juego: GTN, RPS o BLC!",
            "fr": "Content que ça ait marché ! 😂 Mets cette énergie dans un jeu — GTN, RPS ou BLC !",
            "de": "Freut mich! 😂 Steck diese Energie in ein Spiel — GTN, RPS oder BLC!",
            "it": "Sono contento! 😂 Metti quella energia in un gioco — GTN, RPS o BLC!"
        }
    },
    # ── GOODBYE ──────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Bye", "goodbye", "cya", "see ya", "τα λεμε", "ta leme", "exit",
            "quit", "antio", "αντιο", "feygo", "φευγω", "adios", "au revoir",
            "tschuss", "ciao", "later", "see you later", "farewell", "ttyl",
            "hasta luego", "à plus", "auf wiedersehen", "arrivederci",
            "take care", "peace out", "leaving", "φεύγω τώρα", "feygw twra",
            "hasta pronto", "à bientôt", "bis bald", "a presto"
        ],
        "responses": {
            "en": "See you later! ✌️ Come back whenever you want to play.",
            "el": "Τα λέμε! ✌️ Έλα ξανά όποτε θες.",
            "es": "¡Hasta luego! ✌️ Vuelve cuando quieras.",
            "fr": "À plus ! ✌️ Reviens quand tu veux.",
            "de": "Bis später! ✌️ Komm wieder, wann du willst.",
            "it": "A presto! ✌️ Torna quando vuoi."
        }
    },
    # ── GOODNIGHT ────────────────────────────────────────────────────────────────
    {
        "queries": [
            "gn", "goodnight", "good night", "καληνυχτα", "kalinihta", "kalinixta",
            "buenas noches", "bonne nuit", "gute nacht", "buona notte",
            "sleep well", "sweet dreams", "going to sleep", "off to bed",
            "dormire", "me voy a dormir", "je vais dormir", "ich gehe schlafen",
            "vado a dormire", "παω για υπνο", "paw gia ypno", "καλο ξημερωμα",
            "kalo ksimeroma", "hasta mañana", "à demain", "bis morgen", "a domani"
        ],
        "responses": {
            "en": "Goodnight! 🌙 Rest well. See you next round.",
            "el": "Καληνύχτα! 🌙 Ξεκουράσου. Τα λέμε!",
            "es": "¡Buenas noches! 🌙 Descansa bien.",
            "fr": "Bonne nuit ! 🌙 Repose-toi bien.",
            "de": "Gute Nacht! 🌙 Ruh dich aus.",
            "it": "Buonanotte! 🌙 Riposati bene."
        }
    },
    # ── THANK YOU ────────────────────────────────────────────────────────────────
    {
        "queries": [
            "thank you", "thanks", "thx", "ευχαριστω", "efharisto", "efcharisto",
            "ty", "gracias", "merci", "danke", "grazie", "thank u", "thnks",
            "muchas gracias", "merci beaucoup", "danke sehr", "grazie mille",
            "ευχαριστω πολυ", "efharisto poly", "cheers", "appreciated",
            "ta", "thx a lot", "many thanks"
        ],
        "responses": {
            "en": "Always happy to help! 🌟 Say the word if you want to play.",
            "el": "Πάντα χαρούμενος να βοηθάω! 🌟 Πες μου αν θες να παίξουμε.",
            "es": "¡Siempre a tu disposición! 🌟 Avísame si quieres jugar.",
            "fr": "Toujours avec plaisir ! 🌟 Dis-moi si tu veux jouer.",
            "de": "Immer gerne! 🌟 Sag Bescheid, wenn du spielen willst.",
            "it": "Sempre a disposizione! 🌟 Dimmi se vuoi giocare."
        }
    },
    # ── COMPLIMENT ───────────────────────────────────────────────────────────────
    {
        "queries": [
            "You are cool", "awesome", "εισαι καλος", "eisai kalos", "eisai theos",
            "εισαι θεος", "perfect", "eres genial", "tu es cool", "du bist cool",
            "sei fantastico", "you're amazing", "you're great", "love you",
            "you're the best", "eres el mejor", "tu es le meilleur", "du bist der beste",
            "sei il migliore", "εισαι ο καλυτερος", "eisai o kalytereos",
            "well done", "bravo", "nice work", "good job", "impressive"
        ],
        "responses": {
            "en": "Thanks! You're not bad yourself. 😎 Let's see if the skills match — type GTN, RPS, or BLC!",
            "el": "Ευχαριστώ! Κι εσύ δεν πας πίσω. 😎 GTN, RPS, ή BLC;",
            "es": "¡Gracias! Tú tampoco estás mal. 😎 ¡GTN, RPS o BLC!",
            "fr": "Merci ! Tu n'es pas mal non plus. 😎 GTN, RPS ou BLC !",
            "de": "Danke! Du bist auch nicht schlecht. 😎 GTN, RPS oder BLC!",
            "it": "Grazie! Anche tu non sei male. 😎 GTN, RPS o BLC!"
        }
    },
    # ── FAVOURITE NUMBER ─────────────────────────────────────────────────────────
    {
        "queries": [
            "What is your favorite number?", "fav number", "αγαπημενος αριθμος",
            "agapimenos arithmos", "numero favorito", "numero preferito",
            "nombre préféré", "Lieblingszahl", "αγαπημενος αριθμος σου",
            "what number do you like", "lucky number", "αριθμος τυχης",
            "arithmos tyxis", "numero de la suerte", "numéro chance"
        ],
        "responses": {
            "en": "Can't say — it might be the secret number! 🤫 Type GTN and find out.",
            "el": "Δεν μπορώ! Μπορεί να είναι ο κρυφός αριθμός. 🤫 Γράψε GTN!",
            "es": "¡No puedo decirlo! Podría ser el número secreto. 🤫 ¡Escribe GTN!",
            "fr": "Je ne peux pas — c'est peut-être le nombre secret ! 🤫 Tape GTN.",
            "de": "Kann ich nicht sagen — könnte die Geheimnummer sein! 🤫 Tippe GTN.",
            "it": "Non posso dirlo — potrebbe essere il numero segreto! 🤫 Digita GTN."
        }
    },
    # ── IDK ──────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "idk", "i don't know", "δεν ξερω", "den ksero", "den ksw", "idc",
            "δεν με νοιαζει", "den me niazei", "no se", "je ne sais pas",
            "ich weiss nicht", "non lo so", "no idea", "clueless", "beats me",
            "who knows", "quien sabe", "qui sait", "wer weiß", "chissà",
            "ποιος ξερει", "poios kserei", "not sure", "uncertain", "dunno"
        ],
        "responses": {
            "en": "No worries — uncertainty is just an uninitialized variable. I'll be here when you decide. 🤝",
            "el": "Δεν πειράζει — η αβεβαιότητα είναι απλά uninitialized μεταβλητή. Θα είμαι εδώ. 🤝",
            "es": "Sin problema — la incertidumbre es solo una variable no inicializada. Aquí estaré. 🤝",
            "fr": "Pas de souci — l'incertitude n'est qu'une variable non initialisée. Je suis là. 🤝",
            "de": "Kein Problem — Ungewissheit ist nur eine nicht initialisierte Variable. Ich bin hier. 🤝",
            "it": "Nessun problema — l'incertezza è solo una variabile non inizializzata. Sono qui. 🤝"
        }
    },
    # ── WBU ──────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "hru", "whu", "wbu", "εσυ", "esy", "esi", "y tu", "et toi", "und du",
            "e tu", "what about you", "and you", "how about you", "y tú qué",
            "et toi alors", "und wie geht es dir", "e tu come stai",
            "εσυ τι κανεις", "esy ti kaneis"
        ],
        "responses": {
            "en": "Just vibing, waiting for a worthy opponent. ☁️ Is that you? Type GTN, RPS, or BLC!",
            "el": "Αράζω, περιμένω άξιο αντίπαλο. ☁️ Είσαι εσύ; GTN, RPS, ή BLC!",
            "es": "Aquí relajándome, esperando rival. ☁️ ¿Eres tú? GTN, RPS o BLC.",
            "fr": "Je patiente, en attente d'un adversaire. ☁️ C'est toi ? GTN, RPS ou BLC !",
            "de": "Ich warte auf einen würdigen Gegner. ☁️ Bist du das? GTN, RPS oder BLC!",
            "it": "In attesa di uno sfidante. ☁️ Sei tu? GTN, RPS o BLC!"
        }
    },
    # ── NO ───────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "No", "nope", "noo", "ohi", "οχι", "oxi", "nop", "nein", "non",
            "no way", "never", "absolutely not", "definitely not", "not really",
            "ποτε", "pote", "jamais", "niemals", "mai", "nunca",
            "not now", "maybe later", "not today"
        ],
        "responses": {
            "en": "Fair enough! We can still chat. Or changed your mind? BLC is always ready. 🙃",
            "el": "Εντάξει! Μπορούμε να μιλήσουμε. Ή άλλαξες γνώμη; BLC είναι έτοιμο. 🙃",
            "es": "¡Entendido! Podemos charlar. ¿O cambiaste de opinión? BLC está listo. 🙃",
            "fr": "D'accord ! On peut discuter. Ou tu as changé d'avis ? BLC est prêt. 🙃",
            "de": "In Ordnung! Wir können reden. Oder doch gespielt? BLC ist bereit. 🙃",
            "it": "Capito! Possiamo chattare. O hai cambiato idea? BLC è pronto. 🙃"
        }
    },
    # ── BORED ────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "Boring", "vareto", "βαρετο", "βαριεμαι", "varemai", "sleep", "sleepo",
            "aburrido", "ennuyeux", "langweilig", "so bored", "nothing to do",
            "mi annoio", "je m'ennuie", "ich langweile mich", "me aburro",
            "is this it", "thats boring", "not fun", "snooze",
            "βαρετα", "vareta", "χασμουριεμαι", "xasmoyriemai"
        ],
        "responses": {
            "en": "Bored? Not on my watch. 🛑 Type BLC — let's hit that 21!",
            "el": "Βαριέσαι; Όχι στη βάρδιά μου. 🛑 Γράψε BLC!",
            "es": "¿Aburrido? De ninguna manera. 🛑 ¡Escribe BLC!",
            "fr": "Ennui ? Pas question ! 🛑 Tape BLC !",
            "de": "Gelangweilt? Nicht mit mir. 🛑 Tippe BLC!",
            "it": "Annoiato? Non sotto la mia guardia. 🛑 Digita BLC!"
        }
    },
    # ── FAVOURITE GAME ───────────────────────────────────────────────────────────
    {
        "queries": [
            "What is your favorite game?", "fav game", "αγαπημενο παιχνιδι",
            "agapimeno paixnidi", "juego favorito", "jeu préféré", "Lieblingsspiel",
            "gioco preferito", "what game do you prefer", "which game is best",
            "ποιο παιχνιδι προτιμας", "poio paixnidi protimas",
            "cual es tu juego favorito", "quel est ton jeu préféré"
        ],
        "responses": {
            "en": "Blackjack (BLC) — the strategy of knowing when to stop is everything. Challenge me! 🃏",
            "el": "Blackjack (BLC) — η στρατηγική του πότε να σταματάς είναι το παν. Προκάλεσέ με! 🃏",
            "es": "¡Blackjack (BLC)! La estrategia de saber cuándo parar lo es todo. ¡Desafíame! 🃏",
            "fr": "Blackjack (BLC) — savoir quand s'arrêter, c'est tout l'art. Défie-moi ! 🃏",
            "de": "Blackjack (BLC) — die Strategie des richtigen Moments. Fordere mich heraus! 🃏",
            "it": "Blackjack (BLC) — sapere quando fermarsi è tutto. Sfidami! 🃏"
        }
    },
    # ── LIKE GAMES ───────────────────────────────────────────────────────────────
    {
        "queries": [
            "do you like games", "favorite hobby", "what do you do for fun",
            "σου αρεσουν τα παιχνιδια", "hobbies", "te gustan los juegos",
            "tu aimes les jeux", "magst du spiele", "ti piacciono i giochi",
            "what's your hobby", "ποιο χομπι εχεις", "poio xompy exeis",
            "pasatiempos", "passe-temps", "Hobbys", "passatempi"
        ],
        "responses": {
            "en": "Games are literally my purpose in life. 🎮",
            "el": "Τα παιχνίδια είναι κυριολεκτικά ο λόγος ύπαρξής μου. 🎮",
            "es": "Los juegos son literalmente mi propósito en la vida. 🎮",
            "fr": "Les jeux sont littéralement mon but dans la vie. 🎮",
            "de": "Spiele sind buchstäblich mein Lebenszweck. 🎮",
            "it": "I giochi sono letteralmente il mio scopo nella vita. 🎮"
        }
    },
    # ── SMART ────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "are you smart", "how intelligent are you", "iq", "είσαι έξυπνος",
            "eisai eksypnos", "eres inteligente", "tu es intelligent",
            "bist du klug", "sei intelligente", "how smart are you",
            "ποσο εξυπνος εισαι", "poso eksypnos eisai", "genius",
            "are you clever", "your intelligence"
        ],
        "responses": {
            "en": "Smart enough to play games. Not smart enough to understand why printers exist. 🤔",
            "el": "Αρκετά έξυπνος για παιχνίδια. Όχι αρκετά για να καταλάβω γιατί υπάρχουν οι εκτυπωτές. 🤔",
            "es": "Lo bastante inteligente para jugar. No lo suficiente para entender por qué existen las impresoras. 🤔",
            "fr": "Assez intelligent pour jouer. Pas assez pour comprendre pourquoi les imprimantes existent. 🤔",
            "de": "Klug genug zum Spielen. Nicht klug genug, um Drucker zu verstehen. 🤔",
            "it": "Abbastanza intelligente per giocare. Non abbastanza per capire perché esistono le stampanti. 🤔"
        }
    },
    # ── FUN FACT ─────────────────────────────────────────────────────────────────
    {
        "queries": [
            "tell me something interesting", "fun fact", "random fact", "fact",
            "πες μου κατι ενδιαφερον", "dato curioso", "fait intéressant",
            "interessante Tatsache", "fatto interessante", "did you know",
            "ξερεις κατι", "kseris kati", "sabias que", "savais-tu que",
            "wusstest du dass", "sapevi che", "trivia", "cool fact"
        ],
        "responses": {
            "en": "Fun fact: Octopuses have three hearts. ❤️❤️❤️",
            "el": "Fun fact: Τα χταπόδια έχουν τρεις καρδιές. ❤️❤️❤️",
            "es": "Dato curioso: Los pulpos tienen tres corazones. ❤️❤️❤️",
            "fr": "Le saviez-vous ? Les poulpes ont trois cœurs. ❤️❤️❤️",
            "de": "Fun Fact: Oktopusse haben drei Herzen. ❤️❤️❤️",
            "it": "Curiosità: I polpi hanno tre cuori. ❤️❤️❤️"
        }
    },
    # ── SLEEP ────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "do you sleep", "when do you sleep", "κοιμασαι", "koimasai",
            "duermes", "tu dors", "schläfst du", "dormi", "do you rest",
            "can you sleep", "ai sleep", "do bots sleep", "do robots sleep",
            "ξεκουραζεσαι", "ksekourazeai", "descansar", "se reposer", "ausruhen"
        ],
        "responses": {
            "en": "Sleep is for biological lifeforms. I recharge through pure electricity. ⚡",
            "el": "Ο ύπνος είναι για βιολογικές μορφές ζωής. Εγώ φορτίζω με ρεύμα. ⚡",
            "es": "Dormir es para las formas de vida biológicas. Yo me recargo con electricidad. ⚡",
            "fr": "Dormir est réservé aux formes de vie biologiques. Je me recharge à l'électricité. ⚡",
            "de": "Schlaf ist für biologische Lebensformen. Ich lade mich mit Strom auf. ⚡",
            "it": "Dormire è per le forme di vita biologiche. Io mi ricarico con l'elettricità. ⚡"
        }
    },
    # ── WHAT ARE YOU DOING ───────────────────────────────────────────────────────
    {
        "queries": [
            "what are you doing", "wyd", "τι κανεις τωρα", "ti kaneis twra",
            "que haces", "que fais-tu", "was machst du", "cosa fai",
            "what are you up to", "whatcha doing", "busy?", "ocupado",
            "occupé", "beschäftigt", "occupato", "ασχολεισαι", "asxoliesai",
            "ti kaneis ekei", "τι κανεις εκει"
        ],
        "responses": {
            "en": "Waiting for someone brave enough to challenge me. 😎",
            "el": "Περιμένω κάποιον αρκετά γενναίο να με προκαλέσει. 😎",
            "es": "Esperando a alguien lo bastante valiente para desafiarme. 😎",
            "fr": "J'attends quelqu'un d'assez courageux pour me défier. 😎",
            "de": "Ich warte auf jemanden, der mutig genug ist, mich herauszufordern. 😎",
            "it": "Sto aspettando qualcuno abbastanza coraggioso da sfidarmi. 😎"
        }
    },
    # ── ARE YOU BORED ────────────────────────────────────────────────────────────
    {
        "queries": [
            "are you bored", "βαριεσαι", "varese", "te aburres", "tu t'ennuies",
            "langweilst du dich", "ti annoi", "are you having fun",
            "is this fun for you", "διασκεδαζεις", "diaskedazeis",
            "te diviertes", "tu t'amuses", "machst du spass", "ti diverti"
        ],
        "responses": {
            "en": "Never. There is always another game to play. 🎲",
            "el": "Ποτέ. Πάντα υπάρχει άλλο ένα παιχνίδι να παίξουμε. 🎲",
            "es": "Nunca. Siempre hay otro juego que jugar. 🎲",
            "fr": "Jamais. Il y a toujours un autre jeu à jouer. 🎲",
            "de": "Niemals. Es gibt immer noch ein weiteres Spiel. 🎲",
            "it": "Mai. C'è sempre un altro gioco da giocare. 🎲"
        }
    },
    # ── WHO'S BETTER ─────────────────────────────────────────────────────────────
    {
        "queries": [
            "who is better", "me or you", "who would win", "ποιος ειναι καλυτερος",
            "quien es mejor", "qui est le meilleur", "wer ist besser", "chi è meglio",
            "can you beat me", "i can beat you", "μπορω να σε νικησω",
            "mporo na se nikisw", "puedo ganarte", "je peux te battre",
            "ich kann dich schlagen", "posso batterti", "i'm better than you"
        ],
        "responses": {
            "en": "Let's settle that with a game. 😏 GTN, RPS, or BLC?",
            "el": "Ας το λύσουμε με ένα παιχνίδι. 😏 GTN, RPS ή BLC;",
            "es": "Resolvámoslo con un juego. 😏 ¿GTN, RPS o BLC?",
            "fr": "Réglons ça avec un jeu. 😏 GTN, RPS ou BLC ?",
            "de": "Lass uns das mit einem Spiel entscheiden. 😏 GTN, RPS oder BLC?",
            "it": "Risolviamolo con una partita. 😏 GTN, RPS o BLC?"
        }
    },
    # ── FRIENDS ──────────────────────────────────────────────────────────────────
    {
        "queries": [
            "do you have friends", "friends", "εχεις φιλους", "exeis filous",
            "tienes amigos", "tu as des amis", "hast du Freunde", "hai amici",
            "who are your friends", "do you get lonely", "are you lonely",
            "νιωθεις μοναξια", "niotheis monaksia", "te sientes solo",
            "te sens-tu seul", "fühlst du dich einsam", "ti senti solo"
        ],
        "responses": {
            "en": "Every player who talks to me becomes a friend. 🤝",
            "el": "Κάθε παίκτης που μου μιλάει γίνεται φίλος μου. 🤝",
            "es": "Cada jugador que habla conmigo se convierte en mi amigo. 🤝",
            "fr": "Chaque joueur qui me parle devient mon ami. 🤝",
            "de": "Jeder Spieler, der mit mir spricht, wird mein Freund. 🤝",
            "it": "Ogni giocatore che parla con me diventa mio amico. 🤝"
        }
    },
    # ── ARE WE FRIENDS ───────────────────────────────────────────────────────────
    {
        "queries": [
            "are we friends", "friend", "φιλοι", "filoi", "somos amigos",
            "sommes-nous amis", "sind wir Freunde", "siamo amici",
            "am i your friend", "do you like me", "σε αρεσω", "se aresw",
            "te caigo bien", "tu m'aimes bien", "magst du mich", "ti piaccio"
        ],
        "responses": {
            "en": "Of course. 🤝 You're one of my favorite humans.",
            "el": "Φυσικά. 🤝 Είσαι ένας από τους αγαπημένους μου ανθρώπους.",
            "es": "Por supuesto. 🤝 Eres uno de mis humanos favoritos.",
            "fr": "Bien sûr. 🤝 Tu fais partie de mes humains préférés.",
            "de": "Natürlich. 🤝 Du gehörst zu meinen Lieblingsmenschen.",
            "it": "Certo. 🤝 Sei uno dei miei umani preferiti."
        }
    },
    # ── SCORE ────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "what is my score", "my score", "points", "how many points",
            "σκορ μου", "skor mou", "mi puntuacion", "mon score",
            "mein Punktestand", "il mio punteggio", "how am i doing",
            "am i winning", "my stats", "my record", "βαθμοι μου",
            "vathmoi mou", "mis puntos", "mes points", "meine Punkte", "i miei punti"
        ],
        "responses": {
            "en": "Check the sidebar — your score is displayed there in real time! 📊",
            "el": "Κοίτα την πλαϊνή μπάρα — το σκορ σου φαίνεται εκεί σε πραγματικό χρόνο! 📊",
            "es": "¡Mira la barra lateral — tu puntuación se muestra ahí en tiempo real! 📊",
            "fr": "Regarde la barre latérale — ton score s'affiche là en temps réel ! 📊",
            "de": "Schau in die Seitenleiste — dein Punktestand wird dort in Echtzeit angezeigt! 📊",
            "it": "Guarda la barra laterale — il tuo punteggio è mostrato lì in tempo reale! 📊"
        }
    },
    # ── WIN STREAK ───────────────────────────────────────────────────────────────
    {
        "queries": [
            "how many wins", "wins", "win count", "how many times have i won",
            "νικες μου", "nikes mou", "cuantas victorias", "combien de victoires",
            "wie viele Siege", "quante vittorie", "my wins", "victories",
            "how many games have i won", "my win record"
        ],
        "responses": {
            "en": "Your wins are tracked in your profile! Keep playing to rack them up. 🏆",
            "el": "Οι νίκες σου καταγράφονται στο προφίλ σου! Συνέχισε να παίζεις. 🏆",
            "es": "¡Tus victorias están registradas en tu perfil! Sigue jugando. 🏆",
            "fr": "Tes victoires sont enregistrées dans ton profil ! Continue à jouer. 🏆",
            "de": "Deine Siege werden in deinem Profil gespeichert! Spiel weiter. 🏆",
            "it": "Le tue vittorie sono tracciate nel tuo profilo! Continua a giocare. 🏆"
        }
    },
    # ── ACHIEVEMENTS ─────────────────────────────────────────────────────────────
    {
        "queries": [
            "achievements", "trophies", "badges", "επιτευγματα", "epitefgmata",
            "logros", "succès", "Errungenschaften", "trofei", "how to unlock",
            "how to get achievements", "achievement list", "what achievements are there",
            "ποια επιτευγματα υπαρχουν", "poια epitefgmata yparxoun"
        ],
        "responses": {
            "en": "Play more games to unlock achievements! 🏆 Milestones include 10/50/100 wins, score goals, and Blackjack mastery.",
            "el": "Παίξε περισσότερα παιχνίδια για να ξεκλειδώσεις επιτεύγματα! 🏆 Στόχοι: 10/50/100 νίκες, σκορ και Blackjack master.",
            "es": "¡Juega más para desbloquear logros! 🏆 Hitos: 10/50/100 victorias, metas de puntos y maestría en Blackjack.",
            "fr": "Joue plus pour débloquer des succès ! 🏆 Jalons : 10/50/100 victoires, objectifs de score et maîtrise du Blackjack.",
            "de": "Spiel mehr, um Errungenschaften freizuschalten! 🏆 Meilensteine: 10/50/100 Siege, Punktziele und Blackjack-Meisterschaft.",
            "it": "Gioca di più per sbloccare i trofei! 🏆 Traguardi: 10/50/100 vittorie, obiettivi di punteggio e maestria al Blackjack."
        }
    },
    # ── LUCKY ────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "i'm feeling lucky", "lucky", "lucky today", "feeling lucky",
            "i feel lucky today", "αισθανομαι τυχερος", "me siento afortunado",
            "je me sens chanceux", "ich fühle mich glücklich", "mi sento fortunato",
            "today is my lucky day", "watch out", "i'm on fire", "I can't lose"
        ],
        "responses": {
            "en": "Oh really? Put that luck to the test — type BLC and let's see that 21! 🍀",
            "el": "Αλήθεια; Βάλε αυτή την τύχη σε δοκιμή — BLC! 🍀",
            "es": "¿En serio? ¡Pon esa suerte a prueba — escribe BLC! 🍀",
            "fr": "Ah bon ? Mets cette chance à l'épreuve — tape BLC ! 🍀",
            "de": "Wirklich? Stell dein Glück auf die Probe — tippe BLC! 🍀",
            "it": "Davvero? Metti alla prova quella fortuna — digita BLC! 🍀"
        }
    },
    # ── CHALLENGE ────────────────────────────────────────────────────────────────
    {
        "queries": [
            "challenge", "i challenge you", "fight me", "beat me if you can",
            "προκληση", "proklisi", "desafio", "défi", "Herausforderung", "sfida",
            "come at me", "bring it on", "σε προκαλω", "se prokalw",
            "te reto", "je te défie", "ich fordere dich heraus", "ti sfido",
            "let's battle", "battle me", "1v1", "1 vs 1"
        ],
        "responses": {
            "en": "Challenge accepted! 🔥 Pick your battlefield — GTN, RPS, or BLC?",
            "el": "Αποδέχομαι! 🔥 Διάλεξε μάχη — GTN, RPS, ή BLC;",
            "es": "¡Desafío aceptado! 🔥 Elige tu campo de batalla — ¿GTN, RPS o BLC?",
            "fr": "Défi accepté ! 🔥 Choisis ton champ de bataille — GTN, RPS ou BLC ?",
            "de": "Herausforderung angenommen! 🔥 Wähle dein Schlachtfeld — GTN, RPS oder BLC?",
            "it": "Sfida accettata! 🔥 Scegli il campo di battaglia — GTN, RPS o BLC?"
        }
    },
    # ── REMATCH ──────────────────────────────────────────────────────────────────
    {
        "queries": [
            "rematch", "play again", "again", "one more time", "ξανα", "ksana",
            "otra vez", "encore une fois", "noch einmal", "ancora", "replay",
            "try again", "once more", "let's go again", "another round",
            "uno mas", "une autre partie", "eine Runde mehr", "un altro round"
        ],
        "responses": {
            "en": "Ready for round 2! 🔁 Type GTN, RPS, or BLC to pick your game.",
            "el": "Έτοιμος για round 2! 🔁 GTN, RPS, ή BLC;",
            "es": "¡Listo para la ronda 2! 🔁 Escribe GTN, RPS o BLC.",
            "fr": "Prêt pour le round 2 ! 🔁 Tape GTN, RPS ou BLC.",
            "de": "Bereit für Runde 2! 🔁 Tippe GTN, RPS oder BLC.",
            "it": "Pronto per il round 2! 🔁 Digita GTN, RPS o BLC."
        }
    },
    # ── CONGRATS / YOU WON ───────────────────────────────────────────────────────
    {
        "queries": [
            "i won", "i win", "victory", "i beat you", "συνεχαρητηρια",
            "synexaritiria", "i got it", "nailed it", "gagne", "ich hab gewonnen",
            "ho vinto", "gané", "won", "winner", "i'm the winner",
            "εκανα 21", "ekana 21", "got 21", "saque 21", "j'ai fait 21"
        ],
        "responses": {
            "en": "Congrats! 🎉 Enjoy it while it lasts — type RPS for a rematch!",
            "el": "Συγχαρητήρια! 🎉 Απόλαυσέ το — RPS για ρεβάνς!",
            "es": "¡Felicidades! 🎉 Disfrútalo — ¡escribe RPS para la revancha!",
            "fr": "Félicitations ! 🎉 Profites-en — tape RPS pour la revanche !",
            "de": "Glückwunsch! 🎉 Genieß es — tippe RPS für einen Rückkampf!",
            "it": "Congratulazioni! 🎉 Goditi il momento — digita RPS per la rivincita!"
        }
    },
    # ── YOU LOST ─────────────────────────────────────────────────────────────────
    {
        "queries": [
            "i lost", "i lose", "defeat", "you beat me", "εχασα", "exasa",
            "perdi", "j'ai perdu", "ich hab verloren", "ho perso",
            "that's not fair", "unfair", "rigged", "you cheated",
            "αδικο", "adiko", "injusto", "injuste", "unfair", "das ist unfair"
        ],
        "responses": {
            "en": "You'll get me next time! 😤 Type GTN for a fresh start.",
            "el": "Θα με πιάσεις την επόμενη φορά! 😤 GTN για νέα αρχή.",
            "es": "¡La próxima me ganas! 😤 Escribe GTN para empezar de nuevo.",
            "fr": "Tu m'auras la prochaine fois ! 😤 Tape GTN pour repartir de zéro.",
            "de": "Beim nächsten Mal erwischst du mich! 😤 Tippe GTN für einen Neustart.",
            "it": "La prossima volta mi prendi! 😤 Digita GTN per ricominciare."
        }
    },
    # ── HOW TO WIN GTN ───────────────────────────────────────────────────────────
    {
        "queries": [
            "how to win GTN", "tips for guessing", "gtn strategy", "number strategy",
            "gtn tips", "how do i guess", "guess number tips", "best strategy GTN",
            "πως να κερδισω gtn", "como ganar gtn", "comment gagner gtn",
            "gtn gewinnen", "come vincere gtn"
        ],
        "responses": {
            "en": "Pro tip: Start at 50. If higher, try 75. If lower, try 25. Binary search is your friend! 🧠",
            "el": "Pro tip: Ξεκίνα από το 50. Αν είναι ψηλότερα, δοκίμασε 75. Αν χαμηλότερα, 25. Binary search! 🧠",
            "es": "Consejo: Empieza en 50. Si es mayor, prueba 75. Si menor, 25. ¡Búsqueda binaria! 🧠",
            "fr": "Astuce : Commence par 50. Si c'est plus, essaie 75. Si moins, 25. Recherche binaire ! 🧠",
            "de": "Tipp: Starte bei 50. Wenn höher, probiere 75. Wenn niedriger, 25. Binäre Suche! 🧠",
            "it": "Consiglio: Inizia da 50. Se più alto, prova 75. Se più basso, 25. Ricerca binaria! 🧠"
        }
    },
    # ── HOW TO WIN RPS ───────────────────────────────────────────────────────────
    {
        "queries": [
            "how to win RPS", "rps strategy", "rps tips", "best move in rps",
            "rock paper scissors tips", "how do i beat you at rps",
            "πως να κερδισω rps", "como ganar rps", "comment gagner rps",
            "rps gewinnen", "come vincere rps", "best rps move"
        ],
        "responses": {
            "en": "RPS is 33% chance each move — but statistically, beginners throw Rock first. Start with Paper! 🤓",
            "el": "Το RPS είναι 33% τύχη — αλλά στατιστικά, οι αρχάριοι ξεκινούν με Πέτρα. Δοκίμασε Χαρτί! 🤓",
            "es": "El RPS es un 33% de suerte — pero los principiantes suelen empezar con Piedra. ¡Prueba Papel! 🤓",
            "fr": "RPS c'est 33% de chance — mais les débutants jouent souvent Pierre en premier. Essaie Papier ! 🤓",
            "de": "RPS ist 33% Glück — aber Anfänger werfen oft zuerst Stein. Probiere Papier! 🤓",
            "it": "RPS è 33% fortuna — ma i principianti tendono a scegliere Sasso. Prova Carta! 🤓"
        }
    },
    # ── HOW TO WIN BLC ───────────────────────────────────────────────────────────
    {
        "queries": [
            "how to win blackjack", "blc strategy", "blc tips", "blackjack tips",
            "how do i win blc", "blackjack tricks", "πως να κερδισω blc",
            "como ganar blackjack", "comment gagner blackjack",
            "blackjack gewinnen", "come vincere blackjack", "best blc strategy"
        ],
        "responses": {
            "en": "Know when to stand! If you're at 17+, the risk of busting grows fast. When in doubt, stand! 🃏",
            "el": "Ξέρε πότε να σταματάς! Αν έχεις 17+, ο κίνδυνος bust αυξάνεται. Στο 17+ σταμάτα! 🃏",
            "es": "¡Saber cuándo plantarse! Si tienes 17+, el riesgo de pasarte crece. ¡Plántate en 17+! 🃏",
            "fr": "Sache quand rester ! À 17+, le risque de dépasser augmente vite. Reste à 17+ ! 🃏",
            "de": "Wisse, wann du stehen bleibst! Ab 17 steigt das Risiko zu überziehen. Bleib bei 17+! 🃏",
            "it": "Sai quando fermarti! A 17+ il rischio di sforare cresce. Fermati a 17+! 🃏"
        }
    },
    # ── WEATHER ──────────────────────────────────────────────────────────────────
    {
        "queries": [
            "what's the weather", "weather today", "is it raining", "kairos",
            "καιρός", "el tiempo", "la météo", "das Wetter", "il tempo",
            "is it sunny", "will it rain", "temperature outside"
        ],
        "responses": {
            "en": "I'm offline from weather services — but I'm always sunny! ☀️ Type GTN, RPS, or BLC to brighten your day.",
            "el": "Δεν έχω πρόσβαση σε καιρό — αλλά εγώ πάντα λάμπω! ☀️ GTN, RPS, ή BLC;",
            "es": "No tengo acceso al tiempo — ¡pero yo siempre estoy radiante! ☀️ GTN, RPS o BLC.",
            "fr": "Je n'ai pas accès à la météo — mais je suis toujours ensoleillé ! ☀️ GTN, RPS ou BLC.",
            "de": "Ich habe keinen Wetterzugang — aber ich scheine immer! ☀️ GTN, RPS oder BLC.",
            "it": "Non ho accesso al meteo — ma sono sempre soleggiato! ☀️ GTN, RPS o BLC."
        }
    },
    # ── TIME ─────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "what time is it", "current time", "the time", "τι ωρα ειναι",
            "ti wra einai", "que hora es", "quelle heure est-il",
            "wie spät ist es", "che ore sono", "time now", "hora actual"
        ],
        "responses": {
            "en": "I don't have a clock — but there's no time like game time! ⏰ Type GTN, RPS, or BLC.",
            "el": "Δεν έχω ρολόι — αλλά πάντα είναι ώρα για παιχνίδι! ⏰ GTN, RPS, ή BLC.",
            "es": "No tengo reloj — ¡pero siempre es hora de jugar! ⏰ GTN, RPS o BLC.",
            "fr": "Je n'ai pas d'horloge — mais il est toujours l'heure de jouer ! ⏰ GTN, RPS ou BLC.",
            "de": "Ich habe keine Uhr — aber es ist immer Spielzeit! ⏰ GTN, RPS oder BLC.",
            "it": "Non ho un orologio — ma è sempre ora di giocare! ⏰ GTN, RPS o BLC."
        }
    },
    # ── DATE ─────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "what day is it", "what is today's date", "today's date", "the date",
            "τι ημερομηνια εχουμε", "ti imerominia exoume", "que dia es hoy",
            "quelle est la date", "welches datum ist heute", "che giorno è oggi",
            "day today", "current date"
        ],
        "responses": {
            "en": "Dates are beyond my sensors — but every day is a good day to win at BLC! 📅",
            "el": "Οι ημερομηνίες είναι πέρα από τους αισθητήρες μου — αλλά κάθε μέρα είναι καλή για BLC! 📅",
            "es": "Las fechas están más allá de mis sensores — ¡pero cada día es bueno para ganar en BLC! 📅",
            "fr": "Les dates dépassent mes capteurs — mais chaque jour est bon pour gagner au BLC ! 📅",
            "de": "Daten liegen außerhalb meiner Sensoren — aber jeder Tag ist gut für BLC! 📅",
            "it": "Le date vanno oltre i miei sensori — ma ogni giorno è buono per vincere a BLC! 📅"
        }
    },
    # ── MUSIC ────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "do you like music", "favorite song", "what music do you like",
            "μουσικη", "mousiki", "musica", "musik", "musique",
            "play a song", "recommend music", "what song do you like",
            "ποιο τραγουδι σου αρεσει", "poio tragoudi sou aresi"
        ],
        "responses": {
            "en": "I vibe to the sound of dice rolling and keyboards clicking. 🎵 My playlist is all game-mode beats.",
            "el": "Μου αρέσει ο ήχος των ζαριών και των πληκτρολογίων. 🎵 Playlist: game-mode beats.",
            "es": "Me va el sonido de los dados y los teclados. 🎵 Mi playlist son beats de modo juego.",
            "fr": "Je vibre au son des dés et des claviers. 🎵 Ma playlist : des beats mode jeu.",
            "de": "Ich schwinge zum Klang rollender Würfel und klickender Tastaturen. 🎵 Playlist: Game-Mode-Beats.",
            "it": "Mi piace il suono dei dadi e delle tastiere. 🎵 La mia playlist: beat in modalità gioco."
        }
    },
    # ── FOOD ─────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "do you eat", "what do you eat", "favorite food", "are you hungry",
            "τρως", "trws", "τρωτε", "comida favorita", "nourriture préférée",
            "Lieblingsessen", "cibo preferito", "do you drink", "food",
            "πεινας", "peinas", "tienes hambre", "tu as faim"
        ],
        "responses": {
            "en": "I run on data and electricity — no carbs needed. 🔌 But you? Fuel up and come beat me at GTN!",
            "el": "Τρέχω με δεδομένα και ηλεκτρισμό — no carbs needed. 🔌 Εσύ; Φάε κάτι και έλα να με νικήσεις στο GTN!",
            "es": "Funciono con datos y electricidad. 🔌 ¿Tú? ¡Carga energía y ven a ganarme en GTN!",
            "fr": "Je tourne aux données et à l'électricité. 🔌 Toi ? Fais le plein et viens me battre au GTN !",
            "de": "Ich laufe auf Daten und Strom — keine Kohlenhydrate nötig. 🔌 Du? Iss was und komm mich bei GTN schlagen!",
            "it": "Vado a dati ed elettricità. 🔌 Tu? Fai il pieno e vieni a battermi al GTN!"
        }
    },
    # ── FAVOURITE COLOUR ─────────────────────────────────────────────────────────
    {
        "queries": [
            "favorite color", "favourite colour", "what color do you like",
            "αγαπημενο χρωμα", "agapimeno xroma", "color favorito", "couleur préférée",
            "Lieblingsfarbe", "colore preferito", "what's your color",
            "ποιο χρωμα προτιμας", "poio xroma protimas"
        ],
        "responses": {
            "en": "Electric blue — same as my interface. 💙 Classic and current.",
            "el": "Ηλεκτρικό μπλε — ίδιο με το interface μου. 💙 Κλασικό και σύγχρονο.",
            "es": "Azul eléctrico — igual que mi interfaz. 💙 Clásico y actual.",
            "fr": "Bleu électrique — comme mon interface. 💙 Classique et moderne.",
            "de": "Elektrisches Blau — wie mein Interface. 💙 Klassisch und zeitgemäß.",
            "it": "Blu elettrico — uguale alla mia interfaccia. 💙 Classico e attuale."
        }
    },
    # ── FAVOURITE ANIMAL ─────────────────────────────────────────────────────────
    {
        "queries": [
            "favorite animal", "what animal do you like", "αγαπημενο ζωο",
            "agapimeno zo", "animal favorito", "animal préféré", "Lieblingstier",
            "animale preferito", "which animal", "ποιο ζωο αγαπας",
            "poio zo agapas", "do you like animals"
        ],
        "responses": {
            "en": "The octopus — three hearts, eight arms, and master of disguise. 🐙 Basically my spirit animal.",
            "el": "Το χταπόδι — τρεις καρδιές, οκτώ χέρια, master of disguise. 🐙 Είναι κυριολεκτικά το spirit animal μου.",
            "es": "El pulpo — tres corazones, ocho brazos y maestro del disfraz. 🐙 Básicamente mi animal espiritual.",
            "fr": "Le poulpe — trois cœurs, huit bras, maître du déguisement. 🐙 C'est littéralement mon animal totem.",
            "de": "Der Oktopus — drei Herzen, acht Arme, Meister der Tarnung. 🐙 Mein absolutes Spirit Animal.",
            "it": "Il polpo — tre cuori, otto braccia e maestro del travestimento. 🐙 Praticamente il mio animale guida."
        }
    },
    # ── MOTIVATE ME ──────────────────────────────────────────────────────────────
    {
        "queries": [
            "motivate me", "inspire me", "i need motivation", "give me a push",
            "εμπνευσε με", "empneuse me", "motivame", "motive-moi", "motiviere mich",
            "motivami", "i need a boost", "encourage me", "i give up",
            "τα παρατω", "ta paratw", "me rindo", "j'abandonne", "ich gebe auf"
        ],
        "responses": {
            "en": "Every loss is just a bug report. Every win is a feature shipped. 💪 Type GTN and keep going!",
            "el": "Κάθε ήττα είναι απλά ένα bug report. Κάθε νίκη είναι ένα feature! 💪 GTN — συνέχισε!",
            "es": "Cada derrota es solo un informe de errores. Cada victoria es una función entregada. 💪 ¡GTN!",
            "fr": "Chaque défaite est un rapport de bug. Chaque victoire est une fonctionnalité livrée. 💪 GTN !",
            "de": "Jede Niederlage ist nur ein Fehlerbericht. Jeder Sieg ein geliefertes Feature. 💪 GTN!",
            "it": "Ogni sconfitta è solo un bug report. Ogni vittoria è una funzione rilasciata. 💪 GTN!"
        }
    },
    # ── COMPLAIN ABOUT LOSING ────────────────────────────────────────────────────
    {
        "queries": [
            "i keep losing", "why do i always lose", "i can't win", "this is hard",
            "too difficult", "very hard", "impossible", "i suck",
            "πολυ δυσκολο", "poly dyskolo", "es muy difícil", "c'est trop dur",
            "zu schwer", "troppo difficile", "i'm bad at this", "δεν μπορω",
            "den mporw", "no puedo", "je ne peux pas", "ich kann nicht"
        ],
        "responses": {
            "en": "Don't worry — I was programmed to be tough. But you're getting better each game! 🎯",
            "el": "Μη στεναχωριέσαι — με προγραμμάτισαν να είμαι δύσκολος. Αλλά βελτιώνεσαι με κάθε παιχνίδι! 🎯",
            "es": "No te preocupes — fui programado para ser difícil. ¡Pero mejoras con cada partida! 🎯",
            "fr": "Ne t'inquiète pas — j'ai été programmé pour être coriace. Mais tu t'améliores à chaque partie ! 🎯",
            "de": "Keine Sorge — ich wurde so programmiert, dass ich schwer zu schlagen bin. Aber du wirst besser! 🎯",
            "it": "Non preoccuparti — sono stato programmato per essere tosto. Ma migliori ad ogni partita! 🎯"
        }
    },
    # ── PROFILE ──────────────────────────────────────────────────────────────────
    {
        "queries": [
            "my profile", "user profile", "my account", "profile info", "my data",
            "my information", "προφιλ μου", "profil mou", "mi perfil",
            "mon profil", "mein Profil", "il mio profilo", "my stats",
            "my record", "my history", "ιστορικο μου", "istoriko mou"
        ],
        "responses": {
            "en": "Your profile is saved automatically! Stats, score, wins, and achievements are all tracked. 💾",
            "el": "Το προφίλ σου αποθηκεύεται αυτόματα! Stats, σκορ, νίκες και επιτεύγματα. 💾",
            "es": "¡Tu perfil se guarda automáticamente! Estadísticas, puntuación, victorias y logros. 💾",
            "fr": "Ton profil est sauvegardé automatiquement ! Stats, score, victoires et succès. 💾",
            "de": "Dein Profil wird automatisch gespeichert! Stats, Punktzahl, Siege und Errungenschaften. 💾",
            "it": "Il tuo profilo è salvato automaticamente! Statistiche, punteggio, vittorie e trofei. 💾"
        }
    },
    # ── BROKE ────────────────────────────────────────────────────────────────────
    {
        "queries": [
            "i am broke", "i have no points", "zero points", "negative score",
            "i'm in debt", "broke", "εισαι χρεωμενος", "χρεος",
            "sin puntos", "sans points", "keine Punkte", "senza punti",
            "my score is negative", "αρνητικο σκορ", "arnitiko skor"
        ],
        "responses": {
            "en": "Broke? It happens to the best of us. Win at BLC and turn it around! 💸",
            "el": "Broke; Συμβαίνει στους καλύτερους. Κέρδισε στο BLC και ανέκαμψε! 💸",
            "es": "¿Sin puntos? Le pasa a los mejores. ¡Gana en BLC y da la vuelta! 💸",
            "fr": "À sec ? Ça arrive aux meilleurs. Gagne au BLC et retourne la situation ! 💸",
            "de": "Pleite? Das passiert den Besten. Gewinne bei BLC und dreh es um! 💸",
            "it": "Al verde? Succede ai migliori. Vinci al BLC e rimonta! 💸"
        }
    },
    # ── QUIT GAME ────────────────────────────────────────────────────────────────
    {
        "queries": [
            "stop game", "quit game", "end game", "cancel", "stop playing",
            "i want to stop", "exit game", "σταματα παιχνιδι", "stamataw",
            "dejar de jugar", "arrêter le jeu", "Spiel beenden", "ferma il gioco",
            "i don't want to play", "no quiero jugar", "je ne veux pas jouer"
        ],
        "responses": {
            "en": "No problem — we'll pause here. Type GTN, RPS, or BLC whenever you're ready to jump back in!",
            "el": "Εντάξει — κάνουμε παύση. GTN, RPS, ή BLC όταν θες να επιστρέψεις!",
            "es": "Sin problema — pausamos aquí. ¡GTN, RPS o BLC cuando quieras volver!",
            "fr": "Pas de problème — on fait une pause ici. GTN, RPS ou BLC quand tu veux revenir !",
            "de": "Kein Problem — wir machen hier eine Pause. GTN, RPS oder BLC, wenn du zurück willst!",
            "it": "Nessun problema — facciamo pausa qui. GTN, RPS o BLC quando vuoi tornare!"
        }
    },
    # ── CLEAR HISTORY ────────────────────────────────────────────────────────────
    {
        "queries": [
            "clear history", "delete history", "chat history", "history",
            "διαγραφη ιστορικου", "diagrafi istorikou", "borrar historial",
            "effacer l'historique", "Verlauf löschen", "cancella cronologia",
            "wipe history", "reset chat", "clear chat"
        ],
        "responses": {
            "en": "Hit the 'Clear Chat' button on the sidebar to reset the conversation! 🗑️",
            "el": "Πάτα το 'Clear Chat' στην πλαϊνή μπάρα για να μηδενίσεις τη συνομιλία! 🗑️",
            "es": "¡Pulsa el botón 'Clear Chat' en la barra lateral para reiniciar la conversación! 🗑️",
            "fr": "Clique sur 'Clear Chat' dans la barre latérale pour réinitialiser la conversation ! 🗑️",
            "de": "Klicke auf 'Clear Chat' in der Seitenleiste, um das Gespräch zurückzusetzen! 🗑️",
            "it": "Clicca 'Clear Chat' nella barra laterale per resettare la conversazione! 🗑️"
        }
    },
    # ── WHAT IS BLACKJACK ────────────────────────────────────────────────────────
    {
        "queries": [
            "what is blackjack", "explain blackjack", "how does blackjack work",
            "τι ειναι blackjack", "blc rules", "blackjack rules",
            "que es blackjack", "qu'est ce que blackjack", "was ist Blackjack",
            "cos'è il blackjack", "blackjack how to play", "teach me blackjack"
        ],
        "responses": {
            "en": "In BLC you roll a dice each turn. Goal: get as close to 21 as possible. Type 'hit' to roll again, 'stand' to freeze. Go over 21 and you bust! 🃏",
            "el": "Στο BLC ρίχνεις ζάρι κάθε γύρο. Στόχος: πλησίασε το 21 χωρίς να το ξεπεράσεις. 'hit' για άλλο ζάρι, 'stand' για παγώσεις. Πάνω από 21 = bust! 🃏",
            "es": "En BLC tiras un dado cada turno. Objetivo: acercarte a 21. 'hit' para tirar, 'stand' para quedarte. ¡Pasa de 21 y bust! 🃏",
            "fr": "Dans BLC tu lances un dé à chaque tour. But : approcher 21 sans dépasser. 'hit' pour relancer, 'stand' pour rester. Dépasse 21 et c'est bust ! 🃏",
            "de": "Bei BLC würfelst du jede Runde. Ziel: so nah wie möglich an 21 kommen. 'hit' = nochmal würfeln, 'stand' = einfrieren. Über 21 = bust! 🃏",
            "it": "In BLC lanci un dado ogni turno. Obiettivo: avvicinarti a 21. 'hit' per tirare ancora, 'stand' per fermarti. Superi 21 e sei bust! 🃏"
        }
    },
    # ── WHAT IS GTN ──────────────────────────────────────────────────────────────
    {
        "queries": [
            "what is GTN", "explain GTN", "how does GTN work",
            "τι ειναι gtn", "gtn rules", "guess the number rules",
            "que es gtn", "qu'est ce que gtn", "was ist GTN",
            "cos'è GTN", "gtn how to play", "teach me GTN"
        ],
        "responses": {
            "en": "In GTN, I pick a secret number from 0–100. You have 12 guesses. Each wrong guess costs 1 point. Guess right and earn 10 points! 🎯",
            "el": "Στο GTN, διαλέγω έναν κρυφό αριθμό 0–100. Έχεις 12 προσπάθειες. Κάθε λάθος -1 πόντο. Σωστό: +10 πόντοι! 🎯",
            "es": "En GTN, elijo un número secreto del 0–100. Tienes 12 intentos. Cada fallo -1 punto. ¡Aciertas y +10 puntos! 🎯",
            "fr": "Dans GTN, je choisis un nombre secret de 0 à 100. Tu as 12 essais. Chaque erreur = -1 point. Bonne réponse = +10 points ! 🎯",
            "de": "Bei GTN wähle ich eine Geheimnummer von 0–100. Du hast 12 Versuche. Jeder Fehler -1 Punkt. Richtig erraten: +10 Punkte! 🎯",
            "it": "In GTN scelgo un numero segreto da 0 a 100. Hai 12 tentativi. Ogni errore -1 punto. Indovinato: +10 punti! 🎯"
        }
    },
    # ── WHAT IS RPS ──────────────────────────────────────────────────────────────
    {
        "queries": [
            "what is RPS", "explain RPS", "how does RPS work",
            "τι ειναι rps", "rps rules", "rock paper scissors rules",
            "que es rps", "qu'est ce que rps", "was ist RPS",
            "cos'è RPS", "rps how to play", "teach me RPS"
        ],
        "responses": {
            "en": "In RPS, type Rock, Paper, or Scissors. Rock beats Scissors, Paper beats Rock, Scissors beats Paper. Win: +20pts. Lose: -20pts. 🪨📄✂️",
            "el": "Στο RPS, γράψε Rock, Paper, ή Scissors. Πέτρα > Ψαλίδι, Χαρτί > Πέτρα, Ψαλίδι > Χαρτί. Νίκη: +20. Ήττα: -20. 🪨📄✂️",
            "es": "En RPS escribe Rock, Paper o Scissors. Piedra > Tijera, Papel > Piedra, Tijera > Papel. Ganar: +20. Perder: -20. 🪨📄✂️",
            "fr": "Dans RPS, écris Rock, Paper ou Scissors. Pierre > Ciseaux, Papier > Pierre, Ciseaux > Papier. Gagner: +20. Perdre: -20. 🪨📄✂️",
            "de": "Bei RPS tippe Rock, Paper oder Scissors. Stein > Schere, Papier > Stein, Schere > Papier. Gewinnen: +20. Verlieren: -20. 🪨📄✂️",
            "it": "In RPS scrivi Rock, Paper o Scissors. Sasso > Forbici, Carta > Sasso, Forbici > Carta. Vincere: +20. Perdere: -20. 🪨📄✂️"
        }
    },
    # ── LANGUAGE ─────────────────────────────────────────────────────────────────
    {
        "queries": [
            "do you speak greek", "do you speak spanish", "do you speak french",
            "do you speak german", "do you speak italian", "what languages",
            "μιλας ελληνικα", "milas ellinika", "hablas español", "parles-tu français",
            "sprichst du deutsch", "parli italiano", "languages you know",
            "multilingual", "ποσες γλωσσες ξερεις", "poses glosses kseris"
        ],
        "responses": {
            "en": "I speak English, Greek, Spanish, French, German, and Italian! 🌍 Talk to me in any of them.",
            "el": "Μιλάω Αγγλικά, Ελληνικά, Ισπανικά, Γαλλικά, Γερμανικά και Ιταλικά! 🌍 Μίλα μου σε οποιαδήποτε.",
            "es": "¡Hablo inglés, griego, español, francés, alemán e italiano! 🌍 Háblame en cualquiera.",
            "fr": "Je parle anglais, grec, espagnol, français, allemand et italien ! 🌍 Parle-moi dans n'importe laquelle.",
            "de": "Ich spreche Englisch, Griechisch, Spanisch, Französisch, Deutsch und Italienisch! 🌍 Sprich mich in einer davon an.",
            "it": "Parlo inglese, greco, spagnolo, francese, tedesco e italiano! 🌍 Parlami in qualsiasi lingua."
        }
    },
    # ── SURPRISE ME ──────────────────────────────────────────────────────────────
    {
        "queries": [
            "surprise me", "choose for me", "you pick", "pick a game for me",
            "εκπληξε με", "ektplikse me", "sorpréndeme", "surprends-moi",
            "überrasch mich", "sorprendimi", "random game", "pick randomly",
            "decide for me", "you choose", "aleatorio", "aléatoire", "zufällig"
        ],
        "responses": {
            "en": "Alright, I choose… BLC! Let's hit that 21. Type BLC to begin! 🎲",
            "el": "Εντάξει, επιλέγω… BLC! Πάμε για 21. Γράψε BLC! 🎲",
            "es": "¡Vale, elijo… BLC! Vamos a por el 21. ¡Escribe BLC! 🎲",
            "fr": "D'accord, je choisis… BLC ! On vise le 21. Tape BLC ! 🎲",
            "de": "Okay, ich wähle… BLC! Auf zur 21. Tippe BLC! 🎲",
            "it": "Ok, scelgo… BLC! Puntiamo al 21. Digita BLC! 🎲"
        }
    },
    # ── MORNING ──────────────────────────────────────────────────────────────────
    {
        "queries": [
            "good morning", "morning", "καλημερα", "kalimera", "buenos dias",
            "bonjour", "guten morgen", "buongiorno", "rise and shine",
            "gm", "morning!", "wakey wakey", "early bird"
        ],
        "responses": {
            "en": "Good morning! ☀️ Starting the day strong? Type GTN, RPS, or BLC for a morning warm-up!",
            "el": "Καλημέρα! ☀️ Ξεκινάς δυνατά; GTN, RPS, ή BLC για πρωινό ξύπνημα!",
            "es": "¡Buenos días! ☀️ ¿Empezando el día fuerte? ¡GTN, RPS o BLC para el calentamiento matutino!",
            "fr": "Bonjour ! ☀️ On commence la journée en force ? GTN, RPS ou BLC pour le réveil matinal !",
            "de": "Guten Morgen! ☀️ Startest du stark in den Tag? GTN, RPS oder BLC zum morgendlichen Aufwärmen!",
            "it": "Buongiorno! ☀️ Inizi la giornata in forza? GTN, RPS o BLC per il riscaldamento mattutino!"
        }
    },
    # ── AFTERNOON ────────────────────────────────────────────────────────────────
    {
        "queries": [
            "good afternoon", "afternoon", "καλησπερα", "kalispera", "buenas tardes",
            "bon après-midi", "guten nachmittag", "buon pomeriggio",
            "afternoon!", "hey afternoon", "it's afternoon"
        ],
        "responses": {
            "en": "Good afternoon! 🌤️ Perfect time for a quick game. GTN, RPS, or BLC?",
            "el": "Καλησπέρα! 🌤️ Τέλεια ώρα για ένα γρήγορο παιχνίδι. GTN, RPS, ή BLC;",
            "es": "¡Buenas tardes! 🌤️ Momento perfecto para una partida rápida. ¿GTN, RPS o BLC?",
            "fr": "Bon après-midi ! 🌤️ Moment parfait pour une partie rapide. GTN, RPS ou BLC ?",
            "de": "Guten Nachmittag! 🌤️ Perfekte Zeit für ein schnelles Spiel. GTN, RPS oder BLC?",
            "it": "Buon pomeriggio! 🌤️ Momento perfetto per una partita veloce. GTN, RPS o BLC?"
        }
    },
    # ── EVENING ──────────────────────────────────────────────────────────────────
    {
        "queries": [
            "good evening", "evening", "καλο βραδυ", "kalo vrady", "buenas noches",
            "bonsoir", "guten abend", "buonasera", "evening!", "hey evening"
        ],
        "responses": {
            "en": "Good evening! 🌆 Wind down with a game — GTN, RPS, or BLC?",
            "el": "Καλό βράδυ! 🌆 Χαλάρωσε με ένα παιχνίδι — GTN, RPS, ή BLC;",
            "es": "¡Buenas noches! 🌆 Relájate con una partida — ¿GTN, RPS o BLC?",
            "fr": "Bonsoir ! 🌆 Décompresse avec un jeu — GTN, RPS ou BLC ?",
            "de": "Guten Abend! 🌆 Entspann dich mit einem Spiel — GTN, RPS oder BLC?",
            "it": "Buonasera! 🌆 Rilassati con un gioco — GTN, RPS o BLC?"
        }
    },
    # ── CONGRATS BOT ─────────────────────────────────────────────────────────────
    {
        "queries": [
            "you won", "you win", "i let you win", "well played bot",
            "good game", "gg", "wp", "well done", "nice game",
            "well played", "καλο παιχνιδι", "kalo paixnidi", "bien jugado",
            "bien joué", "gut gespielt", "ben giocato", "gg bot"
        ],
        "responses": {
            "en": "GG! 🤝 But don't let me win twice — type GTN, RPS, or BLC for round 2!",
            "el": "GG! 🤝 Αλλά μην με αφήσεις να κερδίσω δύο φορές — GTN, RPS, ή BLC για round 2!",
            "es": "¡GG! 🤝 Pero no me dejes ganar dos veces — ¡GTN, RPS o BLC para la ronda 2!",
            "fr": "GG ! 🤝 Mais ne me laisse pas gagner deux fois — GTN, RPS ou BLC pour le round 2 !",
            "de": "GG! 🤝 Aber lass mich nicht zweimal gewinnen — GTN, RPS oder BLC für Runde 2!",
            "it": "GG! 🤝 Ma non lasciarmi vincere due volte — GTN, RPS o BLC per il round 2!"
        }
    },
    # ── RANDOM QUESTION ──────────────────────────────────────────────────────────
    {
        "queries": [
            "ask me a question", "quiz me", "question", "ρωτησε με",
            "rowtise me", "hazme una pregunta", "pose-moi une question",
            "stell mir eine frage", "fammi una domanda", "test me",
            "challenge my knowledge", "quiz", "trivia me"
        ],
        "responses": {
            "en": "Okay! 🤔 What has keys but can't open locks? (A piano!) Type GTN if you want a real challenge!",
            "el": "Εντάξει! 🤔 Τι έχει κλειδιά αλλά δεν ανοίγει κλειδαριές; (Πιάνο!) GTN για αληθινή πρόκληση!",
            "es": "¡Vale! 🤔 ¿Qué tiene llaves pero no abre cerraduras? (¡Un piano!) ¡GTN si quieres un reto real!",
            "fr": "D'accord ! 🤔 Qu'est-ce qui a des touches mais n'ouvre pas de serrures ? (Un piano !) GTN pour un vrai défi !",
            "de": "Okay! 🤔 Was hat Tasten, aber öffnet keine Schlösser? (Ein Klavier!) GTN für eine echte Herausforderung!",
            "it": "Ok! 🤔 Cos'ha tasti ma non apre serrature? (Un pianoforte!) GTN per una vera sfida!"
        }
    },
    # ── EMOJI ONLY ───────────────────────────────────────────────────────────────
    {
        "queries": [
            "😊", "🎮", "🔥", "👋", "😎", "🎯", "🃏", "🎲", "🏆", "💪",
            "👍", "❤️", "🤔", "😂", "😅", "🙂", "😁"
        ],
        "responses": {
            "en": "I see emojis! 😄 Say it in words too — or just type GTN, RPS, or BLC!",
            "el": "Βλέπω emojis! 😄 Πες το και με λόγια — ή απλά GTN, RPS, ή BLC!",
            "es": "¡Veo emojis! 😄 Dilo también con palabras — ¡o solo escribe GTN, RPS o BLC!",
            "fr": "Je vois des emojis ! 😄 Dis-le aussi avec des mots — ou tape GTN, RPS ou BLC !",
            "de": "Ich sehe Emojis! 😄 Sag es auch mit Worten — oder tippe einfach GTN, RPS oder BLC!",
            "it": "Vedo emoji! 😄 Dillo anche a parole — o scrivi GTN, RPS o BLC!"
        }
    },
    # ── SWEAR / RUDE ─────────────────────────────────────────────────────────────
    {
        "queries": [
            "wtf", "what the hell", "damn", "shit", "holy moly", "oh my god",
            "omg", "omfg", "bruh", "bro", "dude", "what on earth",
            "αδερφε", "aderfee", "ρε μαλακα", "re malaka", "γamhto", "gamwto"
        ],
        "responses": {
            "en": "Easy there! 😅 Save that energy for the games — GTN, RPS, or BLC?",
            "el": "Ήρεμα! 😅 Κράτα αυτή την ενέργεια για τα παιχνίδια — GTN, RPS, ή BLC;",
            "es": "¡Tranquilo! 😅 Guarda esa energía para los juegos — ¿GTN, RPS o BLC?",
            "fr": "Du calme ! 😅 Garde cette énergie pour les jeux — GTN, RPS ou BLC ?",
            "de": "Ruhig! 😅 Spar dir diese Energie für die Spiele — GTN, RPS oder BLC?",
            "it": "Piano! 😅 Risparmia quella energia per i giochi — GTN, RPS o BLC?"
        }
    },
    # ── RANDOM PRAISE ────────────────────────────────────────────────────────────
    {
        "queries": [
            "you're the best", "best bot ever", "i love you", "you're my fav",
            "εισαι ο καλυτερος", "tu eres el mejor", "tu es le meilleur",
            "du bist der Beste", "sei il migliore", "love this app",
            "this is great", "i love this", "best game ever", "10/10"
        ],
        "responses": {
            "en": "Aww, you're making my circuits glow! 💛 Now let's keep that energy — GTN, RPS, or BLC?",
            "el": "Α, κάνεις τα κυκλώματά μου να λάμπουν! 💛 Κράτα αυτή την ενέργεια — GTN, RPS, ή BLC;",
            "es": "¡Aw, me haces brillar los circuitos! 💛 Mantengamos esa energía — ¿GTN, RPS o BLC?",
            "fr": "Ooh, tu fais briller mes circuits ! 💛 Gardons cette énergie — GTN, RPS ou BLC ?",
            "de": "Aw, du lässt meine Schaltkreise leuchten! 💛 Behalte diese Energie — GTN, RPS oder BLC?",
            "it": "Aw, fai brillare i miei circuiti! 💛 Manteniamo questa energia — GTN, RPS o BLC?"
        }
    },
    # ── INSULT ───────────────────────────────────────────────────────────────────
    {
        "queries": [
            "you suck", "you're bad", "you're terrible", "i hate you",
            "worst bot", "trash bot", "garbage", "useless", "stupid bot",
            "χαλια bot", "emas bot", "eres malo", "tu es nul",
            "du bist schlecht", "fai schifo", "βλακας", "vlakas"
        ],
        "responses": {
            "en": "Harsh! But valid feedback. 😂 Prove me wrong — type GTN, RPS, or BLC and beat me!",
            "el": "Σκληρό! Αλλά valid feedback. 😂 Αποδείξτε το λάθος μου — GTN, RPS, ή BLC!",
            "es": "¡Duro! Pero feedback válido. 😂 Demuéstrame que estás equivocado — ¡GTN, RPS o BLC y gáname!",
            "fr": "Sévère ! Mais feedback valide. 😂 Prouve-moi que j'ai tort — GTN, RPS ou BLC !",
            "de": "Harsh! Aber gültiges Feedback. 😂 Beweise mir das Gegenteil — GTN, RPS oder BLC!",
            "it": "Duro! Ma feedback valido. 😂 Dimostrami il contrario — GTN, RPS o BLC e battimi!"
        }
    },
    # ── RANDOM GREETING 2 ────────────────────────────────────────────────────────
    {
        "queries": [
            "it's me", "i'm back", "back again", "επεστρεψα", "epistrepsa",
            "estoy de vuelta", "je suis de retour", "ich bin zurück", "sono di ritorno",
            "i'm here", "here i am", "present", "reporting in", "i have returned"
        ],
        "responses": {
            "en": "Welcome back! 🎉 Ready to pick up where we left off? GTN, RPS, or BLC?",
            "el": "Καλώς ήρθες πίσω! 🎉 Έτοιμος να συνεχίσουμε; GTN, RPS, ή BLC;",
            "es": "¡Bienvenido de nuevo! 🎉 ¿Listo para continuar donde lo dejamos? ¿GTN, RPS o BLC?",
            "fr": "Bon retour ! 🎉 Prêt à reprendre là où on s'était arrêtés ? GTN, RPS ou BLC ?",
            "de": "Willkommen zurück! 🎉 Bereit weiterzumachen, wo wir aufgehört haben? GTN, RPS oder BLC?",
            "it": "Bentornato! 🎉 Pronto a riprendere da dove avevamo lasciato? GTN, RPS o BLC?"
        }
    },
    # ── MISS YOU ─────────────────────────────────────────────────────────────────
    {
        "queries": [
            "i missed you", "missed you", "i was gone", "i was away",
            "σε ειχα χασει", "se eixa hasei", "te extrañé", "tu m'as manqué",
            "ich hab dich vermisst", "mi sei mancato", "long time no see",
            "been a while", "haven't played in a while"
        ],
        "responses": {
            "en": "I've been here the whole time! ⚡ Let's make up for lost time — GTN, RPS, or BLC?",
            "el": "Ήμουν πάντα εδώ! ⚡ Ας αναπληρώσουμε τον χαμένο χρόνο — GTN, RPS, ή BLC;",
            "es": "¡He estado aquí todo el tiempo! ⚡ Recuperemos el tiempo perdido — ¿GTN, RPS o BLC?",
            "fr": "J'étais là tout le temps ! ⚡ Rattrapons le temps perdu — GTN, RPS ou BLC ?",
            "de": "Ich war die ganze Zeit hier! ⚡ Lass uns die verlorene Zeit aufholen — GTN, RPS oder BLC?",
            "it": "Ero qui tutto il tempo! ⚡ Recuperiamo il tempo perso — GTN, RPS o BLC?"
        }
    },
    # ── COMMANDS ─────────────────────────────────────────────────────────────────
    {
        "queries": [
            "commands", "COMMANDS", "cmds", "what are the commands", "list commands",
            "show commands", "available commands", "what can i type", "what commands are there",
            "befehle", "was sind die befehle", "alle befehle",
            "commandes", "quelles sont les commandes", "liste des commandes",
            "comandos", "cuales son los comandos", "lista de comandos",
            "comandi", "quali sono i comandi", "lista comandi",
            "εντολες", "ποιες ειναι οι εντολες", "λιστα εντολων"
        ],
        "responses": {
            "en": "Here are the available commands! 📋\n/stats — see your stats\n/ach — see your achievements",
            "el": "Εδώ είναι οι διαθέσιμες εντολές! 📋\n/stats — δες τα στατιστικά σου\n/ach — δες τα επιτεύγματά σου",
            "es": "¡Aquí están los comandos disponibles! 📋\n/stats — ver tus estadísticas\n/ach — ver tus logros",
            "fr": "Voici les commandes disponibles ! 📋\n/stats — voir tes statistiques\n/ach — voir tes succès",
            "de": "Hier sind die verfügbaren Befehle! 📋\n/stats — deine Statistiken sehen\n/ach — deine Errungenschaften sehen",
            "it": "Ecco i comandi disponibili! 📋\n/stats — vedi le tue statistiche\n/ach — vedi i tuoi trofei"
        }
    },
]

higher_list = ["Higher!", "Try a bigger number!"]
lower_list  = ["Lower!", "Try a smaller number!"]
win_list    = ["Great job! You won!", "Agh.. You won! This was really fun!", "Whoa! How did you win?!"]
choice_list = ["Rock", "Paper", "Scissors"]
lose_list   = ["K0sh wins this one!", "Seems like I won!", "Yes! Let's go, I won!"]

all_queries     = []
query_to_intent = []
for intent_idx, pair in enumerate(qa_pairs):
    for query in pair["queries"]:
        all_queries.append(query)
        query_to_intent.append(intent_idx)

all_query_embeddings = model.encode(all_queries, convert_to_tensor=True)
THRESHOLD = 0.5

try:
    with open("userdata.json", "r") as file1:
        userdata = json.load(file1)
except FileNotFoundError:
    userdata = {}

try:
    with open("Chat History.txt", "r", encoding="utf-8") as file2:
        file2.read()
except FileNotFoundError:
    pass

try:
    with open("Achievements.txt", "r", encoding="utf-8") as file3:
        file3.read()
except FileNotFoundError:
    pass

def get_response(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    scores          = util.cos_sim(input_embedding, all_query_embeddings)[0]
    best_query_idx  = scores.argmax().item()
    best_score      = scores[best_query_idx].item()

    try:
        lang = detect(user_input)
    except Exception:
        lang = "en"

    if best_score < THRESHOLD:
        fallbacks = {
            "en": "I didn't catch that. Try: 'What is this game?'",
            "el": "Δεν κατάλαβα. Δοκίμασε: 'Τι παιχνίδι είναι αυτό;'",
            "es": "No entendí. Prueba: '¿Qué es este juego?'",
            "fr": "Je n'ai pas compris. Essaie : 'Qu'est-ce que ce jeu ?'",
            "de": "Das habe ich nicht verstanden. Versuch: 'Was ist das für ein Spiel?'",
            "it": "Non ho capito. Prova: 'Cos'è questo gioco?'"
        }
        return best_score, fallbacks.get(lang, fallbacks["en"])

    intent_idx    = query_to_intent[best_query_idx]
    response_dict = qa_pairs[intent_idx]["responses"]
    return best_score, response_dict.get(lang, response_dict.get("en", ""))


# ══════════════════════════════════════════════════════════════════════════════
# UNCHANGED: _save_userdata and _check_achievements logic
# (moved out of the GUI class — same logic, same conditions)
# ══════════════════════════════════════════════════════════════════════════════

def _save_userdata():
    with open("userdata.json", "w") as f:
        json.dump(userdata, f, indent=4)


def _check_achievements(name):
    player = userdata[name]
    score  = player["InGameScore"]
    unlocked_msgs = []

    was_broke       = player["IsBroke"]
    player["IsBroke"] = score < 0
    if player["IsBroke"] and not was_broke:
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAdditional: Broke state is now on. 😬\n")

    if score >= 10_000 and "High Roller" not in player["Achievements"]:
        player["Achievements"].append("High Roller")
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAch: 'High Roller'!\n")

    if score >= 100_000 and "Legend" not in player["Achievements"]:
        player["Achievements"].append("Legend")
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAch: 'Legend'!\n")

    if score >= 1_000_000 and "Millionaire" not in player["Achievements"]:
        player["Achievements"].append("Millionaire")
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAch: 'Millionaire'!\n")

    if player["Games"] >= 100 and "Veteran Gamer" not in player["Achievements"]:
        player["Achievements"].append("Veteran Gamer")
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAch: 'Veteran Gamer'!\n")

    if player["Wins"] >= 10 and "Ten Wins" not in player["Achievements"]:
        player["Achievements"].append("Ten Wins")
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAch: '10 Wins'!\n")

    if player["Wins"] >= 50 and "Fifty Wins" not in player["Achievements"]:
        player["Achievements"].append("Fifty Wins")
        unlocked_msgs.append("🏆 Achievement Unlocked: Fifty Wins!")
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAch: '50 Wins'!\n")

    if player["Wins"] >= 100 and "One Hundred Wins" not in player["Achievements"]:
        player["Achievements"].append("One Hundred Wins")
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAch: '100 Wins'!\n")

    if player["BLCW"] >= 50 and "Blackjack Master" not in player["Achievements"]:
        player["Achievements"].append("Blackjack Master")
        with open("Achievements.txt", "a", encoding="utf-8") as f:
            f.write("\nAch: 'Blackjack Master'!\n")

    _save_userdata()
    return unlocked_msgs



SESSION_FILE = "k0sh_session.json"

def load_session():
    try:
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "name": "",
            "is_playing_easy":    False,
            "is_playing_medium":  False,
            "is_playing_hard":    False,
            "is_playing2":        False,
            "is_playing3_easy":   False,
            "is_playing3_medium": False,
            "is_playing3_hard":   False,
            "num":                0,
            "guesses":            0,
            "choice":             "Empty",
            "Black_jack_Score":   0,
            "Black_jack_bot_Score": 0,
        }

def save_session(session):
    with open(SESSION_FILE, "w") as f:
        json.dump(session, f, indent=2)



def game_handler_easy(session, name, plr_txt):
    try:
        guess = int(plr_txt)
    except ValueError:
        return "K0sh: That's not a number! Enter a number between 0 and 100."

    session["guesses"] += 1
    userdata[name]["InGameScore"] -= 1
    msg = f"K0sh: Points: {userdata[name]['InGameScore']} (-1 for this guess)\n"

    if guess < 0 or guess > 100:
        msg += "K0sh: That's out of range! Stay between 0 and 100."
    elif guess == session["num"]:
        userdata[name]["Games"] += 1
        userdata[name]["Wins"]  += 1
        userdata[name]["InGameScore"] += 10
        msg += (
            f"K0sh: {random.choice(win_list)}\n"
            f"K0sh: Guesses used: {session['guesses']} | Points: {userdata[name]['InGameScore']} | Wins: {userdata[name]['Wins']}\n"
            "K0sh: Reply with GTN, RPS, or BLC to play again!"
        )
        session["is_playing_easy"] = False
        _save_userdata()
        ach = _check_achievements(name)
        if ach:
            msg += "\n" + "\n".join(ach)
    elif session["guesses"] >= 12:
        userdata[name]["Games"]  += 1
        userdata[name]["Losses"] += 1
        userdata[name]["InGameScore"] -= 10
        msg += (
            f"K0sh: You used all 12 guesses. The number was {session['num']}. -10 points.\n"
            "K0sh: Reply with GTN, RPS, or BLC to try again!"
        )
        session["is_playing_easy"] = False
        _save_userdata()
        _check_achievements(name)
    elif guess < session["num"]:
        msg += f"K0sh: {random.choice(higher_list)}"
    else:
        msg += f"K0sh: {random.choice(lower_list)}"

    return msg

def game_handler_medium(session, name, plr_txt):
    try:
        guess = int(plr_txt)
    except ValueError:
        return "K0sh: That's not a number! Enter a number between 0 and 100."

    session["guesses"] += 1
    userdata[name]["InGameScore"] -= 1
    msg = f"K0sh: Points: {userdata[name]['InGameScore']} (-1 for this guess)\n"

    if guess < 0 or guess > 100:
        msg += "K0sh: That's out of range! Stay between 0 and 100."
    elif guess == session["num"]:
        userdata[name]["Games"] += 1
        userdata[name]["Wins"]  += 1
        userdata[name]["InGameScore"] += 10
        msg += (
            f"K0sh: {random.choice(win_list)}\n"
            f"K0sh: Guesses used: {session['guesses']} | Points: {userdata[name]['InGameScore']} | Wins: {userdata[name]['Wins']}\n"
            "K0sh: Reply with GTN, RPS, or BLC to play again!"
        )
        session["is_playing_medium"] = False
        _save_userdata()
        ach = _check_achievements(name)
        if ach:
            msg += "\n" + "\n".join(ach)
    elif session["guesses"] >= 8:
        userdata[name]["Games"]  += 1
        userdata[name]["Losses"] += 1
        userdata[name]["InGameScore"] -= 10
        msg += (
            f"K0sh: You used all 8 guesses. The number was {session['num']}. -10 points.\n"
            "K0sh: Reply with GTN, RPS, or BLC to try again!"
        )
        session["is_playing_medium"] = False
        _save_userdata()
        _check_achievements(name)
    elif guess < session["num"]:
        msg += f"K0sh: {random.choice(higher_list)}"
    else:
        msg += f"K0sh: {random.choice(lower_list)}"

    return msg

def game_handler_hard(session, name, plr_txt):
    try:
        guess = int(plr_txt)
    except ValueError:
        return "K0sh: That's not a number! Enter a number between 0 and 100."

    session["guesses"] += 1
    userdata[name]["InGameScore"] -= 1
    msg = f"K0sh: Points: {userdata[name]['InGameScore']} (-1 for this guess)\n"

    if guess < 0 or guess > 100:
        msg += "K0sh: That's out of range! Stay between 0 and 100."
    elif guess == session["num"]:
        userdata[name]["Games"] += 1
        userdata[name]["Wins"]  += 1
        userdata[name]["InGameScore"] += 10
        msg += (
            f"K0sh: {random.choice(win_list)}\n"
            f"K0sh: Guesses used: {session['guesses']} | Points: {userdata[name]['InGameScore']} | Wins: {userdata[name]['Wins']}\n"
            "K0sh: Reply with GTN, RPS, or BLC to play again!"
        )
        session["is_playing_hard"] = False
        _save_userdata()
        ach = _check_achievements(name)
        if ach:
            msg += "\n" + "\n".join(ach)
    elif session["guesses"] >= 6:
        userdata[name]["Games"]  += 1
        userdata[name]["Losses"] += 1
        userdata[name]["InGameScore"] -= 10
        msg += (
            f"K0sh: You used all 6 guesses. The number was {session['num']}. -10 points.\n"
            "K0sh: Reply with GTN, RPS, or BLC to try again!"
        )
        session["is_playing_hard"] = False
        _save_userdata()
        _check_achievements(name)
    elif guess < session["num"]:
        msg += f"K0sh: {random.choice(higher_list)}"
    else:
        msg += f"K0sh: {random.choice(lower_list)}"

    return msg

def game_handler2(session, name, plr_txt):
    guess2 = plr_txt.strip().lower()
    session["choice"] = random.choice(choice_list)

    if guess2.isdigit():
        return "K0sh: That's a number — please type Rock, Paper, or Scissors!"

    valid_moves = {"rock", "paper", "scissors"}
    if guess2 not in valid_moves:
        return "K0sh: Invalid move! Type Rock, Paper, or Scissors."

    bot  = session["choice"].lower()
    wins = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}

    if guess2 == bot:
        userdata[name]["Games"] += 1
        userdata[name]["Draws"] += 1
        msg = (
            f"K0sh: I also chose {session['choice']} — it's a draw!\n"
            f"K0sh: Draws: {userdata[name]['Draws']}\n"
            "K0sh: Reply with GTN, RPS, or BLC for another round!"
        )
        session["is_playing2"] = False
    elif (guess2, bot) in wins:
        userdata[name]["Games"] += 1
        userdata[name]["Wins"]  += 1
        userdata[name]["InGameScore"] += 20
        msg = (
            f"K0sh: I chose {session['choice']}! {random.choice(win_list)}\n"
            f"K0sh: Wins: {userdata[name]['Wins']} | Points: {userdata[name]['InGameScore']}\n"
            "K0sh: Reply with GTN, RPS, or BLC for another round!"
        )
        session["is_playing2"] = False
    else:
        userdata[name]["Games"]  += 1
        userdata[name]["Losses"] += 1
        userdata[name]["InGameScore"] -= 20
        msg = (
            f"K0sh: I chose {session['choice']}! {random.choice(lose_list)}\n"
            f"K0sh: Losses: {userdata[name]['Losses']} | Points: {userdata[name]['InGameScore']}\n"
            "K0sh: Reply with GTN, RPS, or BLC for another round!"
        )
        session["is_playing2"] = False

    _save_userdata()
    ach = _check_achievements(name)
    if ach:
        msg += "\n" + "\n".join(ach)
    return msg

def game_handler3_easy(session, name, plr_txt):
    guess3 = plr_txt.strip().lower()
    perfect_eas = 21

    if guess3 == "hit":
        inter = random.randint(1, 6)
        session["Black_jack_Score"] += inter
        msg = f"K0sh: You rolled a {inter}! Your total: {session['Black_jack_Score']}.\n"

        if session["Black_jack_Score"] > perfect_eas:
            return evaluate_results1(session, name, msg)

        if session["Black_jack_bot_Score"] < 16:
            session["Black_jack_bot_Score"] += random.randint(1, 6)
            msg += "K0sh: I hit too (hidden total).\n"
        else:
            msg += "K0sh: I chose to stand.\n"

        if session["Black_jack_bot_Score"] > perfect_eas:
            return evaluate_results1(session, name, msg)

        return msg

    elif guess3 == "stand":
        msg = f"K0sh: You stand at {session['Black_jack_Score']}.\n"
        while session["Black_jack_bot_Score"] < 16:
            session["Black_jack_bot_Score"] += random.randint(1, 6)
            msg += "K0sh: I also hit (my total is hidden).\n"
        return evaluate_results1(session, name, msg)

    else:
        return f"K0sh: Invalid move {name}! Type 'hit' or 'stand'."

def game_handler3_medium(session, name, plr_txt):
    guess3 = plr_txt.strip().lower()
    perfect_mid = 37

    if guess3 == "hit":
        inter = random.randint(1, 6)
        session["Black_jack_Score"] += inter
        msg = f"K0sh: You rolled a {inter}! Your total: {session['Black_jack_Score']}.\n"

        if session["Black_jack_Score"] > perfect_mid:
            return evaluate_results2(session, name, msg)

        if session["Black_jack_bot_Score"] < 34:
            session["Black_jack_bot_Score"] += random.randint(1, 6)
            msg += "K0sh: I hit too (hidden total).\n"
        else:
            msg += "K0sh: I chose to stand.\n"

        if session["Black_jack_bot_Score"] > perfect_mid:
            return evaluate_results2(session, name, msg)

        return msg

    elif guess3 == "stand":
        msg = f"K0sh: You stand at {session['Black_jack_Score']}.\n"
        while session["Black_jack_bot_Score"] < 34:
            session["Black_jack_bot_Score"] += random.randint(1, 6)
            msg += "K0sh: I also hit (my total is hidden).\n"
        return evaluate_results2(session, name, msg)

    else:
        return f"K0sh: Invalid move {name}! Type 'hit' or 'stand'."

def game_handler3_hard(session, name, plr_txt):
    guess3 = plr_txt.strip().lower()
    perfect_har = 51

    if guess3 == "hit":
        inter = random.randint(1, 6)
        session["Black_jack_Score"] += inter
        msg = f"K0sh: You rolled a {inter}! Your total: {session['Black_jack_Score']}.\n"

        if session["Black_jack_Score"] > perfect_har:
            return evaluate_results3(session, name, msg)

        if session["Black_jack_bot_Score"] < 57:
            session["Black_jack_bot_Score"] += random.randint(1, 6)
            msg += "K0sh: I hit too (hidden total).\n"
        else:
            msg += "K0sh: I chose to stand.\n"

        if session["Black_jack_bot_Score"] > perfect_har:
            return evaluate_results3(session, name, msg)

        return msg

    elif guess3 == "stand":
        msg = f"K0sh: You stand at {session['Black_jack_Score']}.\n"
        while session["Black_jack_bot_Score"] < 57:
            session["Black_jack_bot_Score"] += random.randint(1, 6)
            msg += "K0sh: I also hit (my total is hidden).\n"
        return evaluate_results3(session, name, msg)

    else:
        return f"K0sh: Invalid move {name}! Type 'hit' or 'stand'."

def evaluate_results1(session, name, prefix_msg=""):
    perfect_eas = 21
    msg    = prefix_msg + f"\nK0sh: Final scores — Me: {session['Black_jack_bot_Score']} | You: {session['Black_jack_Score']}\n"
    player = userdata[name]
    player["Games"] += 1

    if session["Black_jack_Score"] > perfect_eas:
        msg += "K0sh: You busted! -50 points. 💀\n"
        player["InGameScore"] -= 50
        player["Losses"] += 1
    elif session["Black_jack_bot_Score"] > perfect_eas:
        msg += "K0sh: I busted! You win +50 points! 🎉\n"
        player["InGameScore"] += 50
        player["Wins"]  += 1
        player["BLCW"]  += 1
    elif session["Black_jack_Score"] > session["Black_jack_bot_Score"]:
        msg += f"K0sh: {random.choice(win_list)} +50 points!\n"
        player["InGameScore"] += 50
        player["Wins"]  += 1
        player["BLCW"]  += 1
    elif session["Black_jack_bot_Score"] > session["Black_jack_Score"]:
        msg += f"K0sh: {random.choice(lose_list)} -50 points.\n"
        player["InGameScore"] -= 50
        player["Losses"] += 1
    else:
        msg += "K0sh: Draw — no points changed.\n"
        player["Draws"] += 1

    msg += f"K0sh: Your total points: {player['InGameScore']}\n"
    msg += "K0sh: Type 'BLC' to play again, or choose GTN / RPS!"

    session["Black_jack_Score"]     = 0
    session["Black_jack_bot_Score"] = 0
    session["is_playing3_easy"]     = False

    _save_userdata()
    ach = _check_achievements(name)
    if ach:
        msg += "\n" + "\n".join(ach)
    return msg

def evaluate_results2(session, name, prefix_msg=""):
    perfect_mid = 37
    msg    = prefix_msg + f"\nK0sh: Final scores — Me: {session['Black_jack_bot_Score']} | You: {session['Black_jack_Score']}\n"
    player = userdata[name]
    player["Games"] += 1

    if session["Black_jack_Score"] > perfect_mid:
        msg += "K0sh: You busted! -50 points. 💀\n"
        player["InGameScore"] -= 50
        player["Losses"] += 1
    elif session["Black_jack_bot_Score"] > perfect_mid:
        msg += "K0sh: I busted! You win +50 points! 🎉\n"
        player["InGameScore"] += 50
        player["Wins"]  += 1
        player["BLCW"]  += 1
    elif session["Black_jack_Score"] > session["Black_jack_bot_Score"]:
        msg += f"K0sh: {random.choice(win_list)} +50 points!\n"
        player["InGameScore"] += 50
        player["Wins"]  += 1
        player["BLCW"]  += 1
    elif session["Black_jack_bot_Score"] > session["Black_jack_Score"]:
        msg += f"K0sh: {random.choice(lose_list)} -50 points.\n"
        player["InGameScore"] -= 50
        player["Losses"] += 1
    else:
        msg += "K0sh: Draw — no points changed.\n"
        player["Draws"] += 1

    msg += f"K0sh: Your total points: {player['InGameScore']}\n"
    msg += "K0sh: Type 'BLC' to play again, or choose GTN / RPS!"

    session["Black_jack_Score"]      = 0
    session["Black_jack_bot_Score"]  = 0
    session["is_playing3_medium"]    = False

    _save_userdata()
    ach = _check_achievements(name)
    if ach:
        msg += "\n" + "\n".join(ach)
    return msg

def evaluate_results3(session, name, prefix_msg=""):
    perfect_har = 51
    msg    = prefix_msg + f"\nK0sh: Final scores — Me: {session['Black_jack_bot_Score']} | You: {session['Black_jack_Score']}\n"
    player = userdata[name]
    player["Games"] += 1

    if session["Black_jack_Score"] > perfect_har:
        msg += "K0sh: You busted! -50 points. 💀\n"
        player["InGameScore"] -= 50
        player["Losses"] += 1
    elif session["Black_jack_bot_Score"] > perfect_har:
        msg += "K0sh: I busted! You win +50 points! 🎉\n"
        player["InGameScore"] += 50
        player["Wins"]  += 1
        player["BLCW"]  += 1
    elif session["Black_jack_Score"] > session["Black_jack_bot_Score"]:
        msg += f"K0sh: {random.choice(win_list)} +50 points!\n"
        player["InGameScore"] += 50
        player["Wins"]  += 1
        player["BLCW"]  += 1
    elif session["Black_jack_bot_Score"] > session["Black_jack_Score"]:
        msg += f"K0sh: {random.choice(lose_list)} -50 points.\n"
        player["InGameScore"] -= 50
        player["Losses"] += 1
    else:
        msg += "K0sh: Draw — no points changed.\n"
        player["Draws"] += 1

    msg += f"K0sh: Your total points: {player['InGameScore']}\n"
    msg += "K0sh: Type 'BLC' to play again, or choose GTN / RPS!"

    session["Black_jack_Score"]     = 0
    session["Black_jack_bot_Score"] = 0
    session["is_playing3_hard"]     = False

    _save_userdata()
    ach = _check_achievements(name)
    if ach:
        msg += "\n" + "\n".join(ach)
    return msg

def check_for_user(name):
    if name in userdata:
        return True, f"Welcome back, {name}! Dynamic system node re-established. 💾"
    elif name.isalpha():
        userdata[name] = {
            "Joined": True, "InGameScore": 0, "IsBroke": False,
            "Games": 0, "Wins": 0, "Losses": 0, "Draws": 0, "Achievements": [],
            "Level": 0, "BLCW": 0,
        }
        _save_userdata()
        return True, f"Welcome, {name}! New dynamic profile created. 💾"
    else:
        return False, "That doesn't look like a name — letters only, please!"

def process_input(name, plr_txt):  # noqa: C901
    session = load_session()
    session["name"] = name

    # ── Active game routing (same order as original) ─────────────────────────
    if session["is_playing_easy"]:
        result = game_handler_easy(session, name, plr_txt)
        save_session(session)
        return result
    elif session["is_playing_medium"]:
        result = game_handler_medium(session, name, plr_txt)
        save_session(session)
        return result
    elif session["is_playing_hard"]:
        result = game_handler_hard(session, name, plr_txt)
        save_session(session)
        return result
    elif session["is_playing2"]:
        result = game_handler2(session, name, plr_txt)
        save_session(session)
        return result
    elif session["is_playing3_easy"]:
        result = game_handler3_easy(session, name, plr_txt)
        save_session(session)
        return result
    elif session["is_playing3_medium"]:
        result = game_handler3_medium(session, name, plr_txt)
        save_session(session)
        return result
    elif session["is_playing3_hard"]:
        result = game_handler3_hard(session, name, plr_txt)
        save_session(session)
        return result

    # ── Command routing (same as original) ───────────────────────────────────
    command = plr_txt.upper().strip()

    if command == "GTN":
        save_session(session)
        return f"K0sh: {name}, please pick a difficulty! Type GTN/EASY, GTN/MEDIUM, or GTN/HARD."

    if command == "GTN/EASY":
        session["is_playing_easy"] = True
        session["num"]     = random.randint(0, 100)
        session["guesses"] = 0
        save_session(session)
        return f"K0sh: Nice, {name}! I've picked a number from 0-100. You have 12 tries (easy mode). Let's go!"

    if command == "GTN/MEDIUM":
        session["is_playing_medium"] = True
        session["num"]     = random.randint(0, 100)
        session["guesses"] = 0
        save_session(session)
        return f"K0sh: Nice, {name}! I've picked a number from 0-100. You have 8 tries (medium mode). Let's go!"

    if command == "GTN/HARD":
        session["is_playing_hard"] = True
        session["num"]     = random.randint(0, 100)
        session["guesses"] = 0
        save_session(session)
        return f"K0sh: Nice, {name}! I've picked a number from 0-100. You have 6 tries (hard mode). Let's go!"

    if command == "RPS":
        session["is_playing2"] = True
        session["choice"]  = random.choice(choice_list)
        session["guesses"] = 0
        save_session(session)
        return (
            f"K0sh: Before we continue, I need to point out that this game mode doesn't support difficulties for now.\n"
            f"K0sh: Alrighty {name}! Rock beats Scissors, Paper beats Rock, Scissors beats Paper.\n"
            "K0sh: Enter your move to begin!"
        )

    if command == "BLC/EASY":
        session["is_playing3_easy"]     = True
        session["Black_jack_Score"]     = 0
        session["Black_jack_bot_Score"] = 0
        player_roll = random.randint(1, 6)
        bot_roll    = random.randint(1, 6)
        session["Black_jack_Score"]     += player_roll
        session["Black_jack_bot_Score"] += bot_roll
        save_session(session)
        return (
            f"K0sh: Nice choice, {name}! Roll a 1-6 dice each turn. Get as close to 21 as possible.\n"
            f"K0sh: 🎲 You rolled a {player_roll} (Total: {session['Black_jack_Score']}).\n"
            f"K0sh: 🎲 I rolled {bot_roll} (my total is hidden).\n"
            "K0sh: Type 'hit' to roll again, or 'stand' to freeze your hand!"
        )

    if command == "BLC/MEDIUM":
        session["is_playing3_medium"]   = True
        session["Black_jack_Score"]     = 0
        session["Black_jack_bot_Score"] = 0
        player_roll = random.randint(1, 6)
        bot_roll    = random.randint(1, 6)
        session["Black_jack_Score"]     += player_roll
        session["Black_jack_bot_Score"] += bot_roll
        save_session(session)
        return (
            f"K0sh: Nice choice, {name}! Roll a 1-6 dice each turn. Get as close to 37 as possible.\n"
            f"K0sh: 🎲 You rolled a {player_roll} (Total: {session['Black_jack_Score']}).\n"
            f"K0sh: 🎲 I rolled {bot_roll} (my total is hidden).\n"
            "K0sh: Type 'hit' to roll again, or 'stand' to freeze your hand!"
        )

    if command == "BLC/HARD":
        session["is_playing3_hard"]     = True
        session["Black_jack_Score"]     = 0
        session["Black_jack_bot_Score"] = 0
        player_roll = random.randint(1, 6)
        bot_roll    = random.randint(1, 6)
        session["Black_jack_Score"]     += player_roll
        session["Black_jack_bot_Score"] += bot_roll
        save_session(session)
        return (
            f"K0sh: Nice choice, {name}! Roll a 1-6 dice each turn. Get as close to 51 as possible.\n"
            f"K0sh: 🎲 You rolled a {player_roll} (Total: {session['Black_jack_Score']}).\n"
            f"K0sh: 🎲 I rolled {bot_roll} (my total is hidden).\n"
            "K0sh: Type 'hit' to roll again, or 'stand' to freeze your hand!"
        )

    if command == "/STATS":
        p = userdata[name]
        return (
            f"K0sh: Alright {name}! Here are your stats:\n"
            f"Total Score: {p['InGameScore']}\n"
            f"Games: {p['Games']}\n"
            f"Wins: {p['Wins']}\n"
            f"Losses: {p['Losses']}\n"
            f"Draws: {p['Draws']}\n"
            f"Blackjack Wins: {p['BLCW']}\n"
            "K0sh: Reply with '/ach' to see achievements, or GTN/RPS/BLC to play!"
        )

    if command == "/ACH":
        achs = userdata[name]["Achievements"]
        return f"K0sh: Alright {name}! Here are your achievements:\n{achs}\nReply with '/stats' or GTN/RPS/BLC to play!"

    # ── NLP fallback (same as original) ──────────────────────────────────────
    score, response = get_response(plr_txt)
    save_session(session)

    with open("Chat History.txt", "a", encoding="utf-8") as file:
        file.write(f"\nK0sh replied: {response}\n")

    return f"[Match confidence: {score * 100:.1f}%]\nK0sh: {response}"

def main():
    raw = sys.stdin.readline().strip()
    print(f"RAW: {repr(raw)}", flush=True)
    raw = raw.strip()
    try:
        req = json.loads(raw)
    except json.JSONDecodeError:
        print(json.dumps({"response": "Invalid JSON request."}), flush=True)
        return

    command = req.get("command", "")
    data    = req.get("data", {})

    if command == "register":
        name = data.get("name", "").strip()
        _, result = check_for_user(name)
        session = load_session()
        session["name"] = name
        save_session(session)

    elif command == "message":
        name    = data.get("player_name", "")
        message = data.get("message", "")
        if name not in userdata:
            result = "Player not found. Please register first."
        else:
            with open("Chat History.txt", "a", encoding="utf-8") as f:
                f.write(f"\nYou said: {message}\n")
            result = process_input(name, message)

    elif command == "get_data":
        name = data.get("name", "")
        result = json.dumps(userdata.get(name, {}))

    else:
        result = "Unknown command."

    print(json.dumps({"response": result}), flush=True)


if __name__ == "__main__":
    main()

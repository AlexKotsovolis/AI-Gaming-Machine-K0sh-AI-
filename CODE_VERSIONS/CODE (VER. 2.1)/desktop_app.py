import os
import sys
import webview

def resource_path():
    if getattr(sys, "frozen", False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def save_data_path():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))

os.chdir(save_data_path())

sys.path.insert(0, resource_path())

import K0sh


class Api:
    def register(self, name):
        name = (name or "").strip()
        ok, message = K0sh.check_for_user(name)
        if ok:
            session = K0sh.load_session()
            session["name"] = name
            K0sh.save_session(session)
        return {"ok": ok, "response": message}

    def send_message(self, name, message):
        if name not in K0sh.userdata:
            return {"ok": False, "response": "Player not found. Please register first."}

        with open("Chat History.txt", "a", encoding="utf-8") as f:
            f.write(f"\nYou said: {message}\n")

        result = K0sh.process_input(name, message)
        return {
            "ok": True,
            "response": result,
            "player_data": K0sh.userdata.get(name, {}),
        }

    def get_data(self, name):
        return K0sh.userdata.get(name, {})

    def get_chat_history(self):
        try:
            with open("Chat History.txt", "r", encoding="utf-8") as f:
                content = f.read().strip()
            return {"ok": True, "history": content or "No chat history yet."}
        except FileNotFoundError:
            return {"ok": True, "history": "No chat history yet."}

    def erase_chat_history(self):
        with open("Chat History.txt", "w", encoding="utf-8") as f:
            f.write("")
        return {"ok": True}

    def quit_app(self):
        webview.windows[0].destroy()


if __name__ == "__main__":
    api = Api()
    index_path = os.path.join(resource_path(), "index.html")
    window = webview.create_window(
        "K0sh AI",
        index_path,
        js_api=api,
        width=1100,
        height=720,
        background_color="#04050f",
        min_size=(820, 560),
    )
    webview.start()

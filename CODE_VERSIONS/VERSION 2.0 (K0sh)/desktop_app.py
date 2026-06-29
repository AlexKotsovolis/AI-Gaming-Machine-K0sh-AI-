import os
import webview

os.chdir(os.path.dirname(os.path.abspath(__file__)))

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

        with open("../Chat History.txt", "a", encoding="utf-8") as f:
            f.write(f"\nYou said: {message}\n")

        result = K0sh.process_input(name, message)
        return {
            "ok": True,
            "response": result,
            "player_data": K0sh.userdata.get(name, {}),
        }

    def get_data(self, name):
        return K0sh.userdata.get(name, {})


if __name__ == "__main__":
    api = Api()
    window = webview.create_window(
        "K0sh AI",
        "index.html",
        js_api=api,
        width=1100,
        height=720,
        background_color="#04050f",
        min_size=(820, 560),
    )
    webview.start()

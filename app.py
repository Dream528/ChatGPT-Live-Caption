from flask import Flask, render_template, jsonify
from threading import Thread
import time

from transcriber import record_and_transcribe
from translator import translate_with_chatgpt, translate_with_claude

app = Flask(__name__)

chatgpt_translation = ""
claude_translation = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translations')
def get_translations():
    return jsonify(chatgpt=chatgpt_translation, claude=claude_translation)

def update_translations():
    global chatgpt_translation, claude_translation
    transcribers = record_and_transcribe()
    while True:
        try:
            text = next(transcribers)
            chatgpt_translation = translate_with_chatgpt(text)
            # claude_translation = translate_with_claude(text)
            time.sleep(1)
        except StopIteration:
            break

if __name__ == '__main__':
    thread = Thread(target=update_translations)
    thread.start()
    app.run(debug=True)
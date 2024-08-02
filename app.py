import json
import threading
import time
from queue import Queue
from flask import Flask, Response, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

prompt_queue = Queue()
sse_event_queue = Queue()
response_thread = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global prompt_queue

    if request.method == 'POST':

        prompt = request.form.get('prompt')

        prompt_queue.put(prompt)

        return {'status': 'success'}, 200

    return render_template('index.html')

def send_sse_data():
    global prompt_queue, sse_event_queue, response_thread
    while True:
        if not prompt_queue.empty():
            if response_thread and response_thread.is_alive():
                continue

            prompt = prompt_queue.get()

            response_thread = threading.Thread(target=stream, args=(prompt, model))
            response_thread.start()

        while not sse_event_queue.empty():
            sse_event = sse_event_queue.get()
            yield f"data: {json.dumps(sse_event)}\n\n"

        time.sleep(1)

@app.route('/stream', methods=['GET'])
def get_bot_response():
    def event_stream():
        return send_sse_data()

    return Response(event_stream(), mimetype='text/event-stream')

def globalize(m, s):
    global model, stream
    model, stream = m, s

def main(model, stream):
    globalize(model, stream)
    app.run(debug=True, use_reloader=False)
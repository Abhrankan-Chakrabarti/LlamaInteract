from flask import *
app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    userText = request.args.get('msg') if request.method == "POST" else None
    return Response(stream(input=userText, model=model) if request.method == "POST" else None, mimetype='text/event-stream')
def globalize(m, s):
    global model, stream
    model, stream = m, s
def main(model, stream):
    globalize(model, stream)
    app.run()
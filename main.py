from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def news():
    with open("package.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('page.html', news=news_list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
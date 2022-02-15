from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/taste_select', methods=['POST'])
def select_taste():
    body_receive = request.form['body_give']
    acidity_receive = request.form['acidity_give']
    sweet_receive = request.form['sweet_give']
    flavor_receive = request.form['flavor_give']
    bitter_receive = request.form['bitter_give']

    doc= {
        'body':body_receive,
        'acidity':acidity_receive,
        'sweet':sweet_receive
        'flavor':flavor_receive
        'bitter':bitter_receive
    }

    db.coffee_like.insert_one(doc)
    return jsonify({'msg': '저장완료!'})


@app.route('/taste_select', methods=['GET'])
def select_taste():
    result = list(db.coffee_like.find({}, {'_id': False}))
    return jsonify({'all_tastes': tastes})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
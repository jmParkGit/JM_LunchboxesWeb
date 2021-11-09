from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbJM

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    lunchboxes = list(db.lunchbox.find({}, {'_id': False}))
    return jsonify({'all_lunchbox':lunchboxes})

@app.route('/api/like', methods=['POST'])
def like_lunchbox():
    title_receive = request.form['title_give'];
    target_lunchbox = db.lunchbox.find_one({'title': title_receive});
    current_like = target_lunchbox['like'];

    new_like=current_like+1;

    db.lunchbox.update_one({'title': title_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
   # app.run('0.0.0.0',port=5001,debug=True)
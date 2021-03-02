from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
# 내 컴퓨터에서 돌아가는 mongoDB에 접속
client = MongoClient('localhost', 27017)
# dbsparta라는 이름으로 접속 #없으면 자동으로 만들어줌 dbsparta라는 이름을
db = client.dbsparta

## HTML 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
# insert
@app.route('/shopping', methods=['POST'])
def make_order():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

   # 딕셔너리 만들기
    doc = {
        'name':name_receive,
        'number':number_receive,
        'address':address_receive,
        'phone':phone_receive
    }
    db.shopping.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

# find
@app.route('/shopping', methods=['GET'])
def show_order():
    orders = list(db.shopping.find({}, {'_id': False}))
    return jsonify({'all_orders':orders})

# delete
@app.route('/shopping/delete', methods=['POST'])
def delete_order():
    name_receive = request.form['name_give']

    db.shopping.delete_one({'name':name_receive})
    return jsonify({'msg': '삭제 완료'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

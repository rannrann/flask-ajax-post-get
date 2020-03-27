from flask import Flask,jsonify,request,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/send_json_to_web',methods=["GET"])
def send_json_to_web():
    return jsonify([{'id':1,'name':'James','drink':'Coffee'},{'id':2,'name':'John','drink':'Latte'}])


@app.route('/receive_json_from_web',methods=["POST"])
def receive_json_from_web():
    data = request.get_json(force=True)
    name = data["name"]
    drink = data["drink"]
    for i in data:
        print(data[i])
    return jsonify({'name':name , 'drink' : drink})

@app.route('/send_list_to_web',methods=["GET"])
def send_list_to_web():
    return jsonify({'result':['find','rannnrann']})

if __name__ == '__main__':
    app.run(debug=True)

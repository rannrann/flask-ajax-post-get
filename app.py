from flask import Flask,jsonify,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/send_json_to_web',methods=["POST"])
def send_json_to_web():
    return jsonify({'result':'Success','name':'Tom','age':'88'})


@app.route('/receive_json_from_web',methods=["POST"])
def receive_json_from_web():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    return jsonify({'result':'Success' , 'name' : name , 'location' : location, 'randomkeyinlist' : randomlist[1]})

if __name__ == '__main__':
    app.run(debug=True)

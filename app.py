from flask import Flask, redirect,url_for,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome To The Flask"

@app.route('/cal',methods=['GET'])
def mathoperation():
    operation = request.json["opearation"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]

    if operaion == 'add' :
        result = number1 + number2
    
    elif operation == 'multiply':
        result = number1 * number2
    
    elif operation == "devision":
        result = int(number1)/int(number2)
    
    else:
        result = number1 - number2
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
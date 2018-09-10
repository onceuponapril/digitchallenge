from flask import Flask, render_template,request,redirect,jsonify,url_for
import digitSumCtrl

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userInput=request.form['input']
        extractDigit=digitSumCtrl.ExtractDigit(userInput)
        userOutput=extractDigit.sumInput()
        return jsonify(result=userOutput)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

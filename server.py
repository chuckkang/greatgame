from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "thisisasecret"



@app.route('/', methods=['POST', 'GET'])
def index():
    isCorrect=False
    errMsg = False
    if (request.method=="GET"):
        #create random variable
        session['rnd']= random.randrange(0, 10)
        print session['rnd'], "this is the rnd"
        isCorrect = "new"
    elif (request.method=="POST"):
          guessedvalue = request.form['guess']
          if (guessedvalue==''):
              errMsg=True
          else:
              if int(request.form['guess'])==session['rnd']:
                    isCorrect = True
              else:
                    isCorrect = False
          print session['rnd'], "this is the rnd"

    return render_template("index.html", isCorrect=isCorrect, rnd=session['rnd'], errMsg=errMsg)

app.run(debug=True) # run our server
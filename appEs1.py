#realizzare unh server web che permetta di effettuare un login 
#l'utent einserisce user name e la password:
#se l'username è admin e la password xxx123# il sito saluta  con un messaggio
#altrimenti ci da messaggio di errore

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
         
    return render_template("oi.html") #importa il file html

@app.route('/data', methods=['GET'])
def hello_data():
    username = request.args['username']
    passs = request.args['password']
    if username == 'admin':
        if passs == 'xxx123#':
            return render_template('wecome.html',nome=username)
        else:
            return ('passwrod errata')
    else:
        return ('username errato')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True) 
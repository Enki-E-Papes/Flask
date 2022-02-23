from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("risp.html") #importa il file html
@app.route('/meteo', methods=['GET'])
def cio():
    n= (random(5))
    
    return render_template("ciaociao.html") #importa il file html



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
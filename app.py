from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("ccio.html") #importa il file html

@app.route('/it', methods=['GET'])
def ciao_Mondo():
    return render_template("ccio.html",ciocio="ciao bello") #importa il file html


@app.route('/fr', methods=['GET'])
def bonjure():
    return ('<h1>bonjure, monde!</h1>')



# da qui non si puo mettere nientaltro 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)


#(1)
#realizzare un sito web che permetta la registrazione degli utenti
#l'utente inserisce il nome 'username' and password  and conferma password amd sesso
#se le informazioni sono corrette 
#se sono corrette il sito salva i dati in una struttura dati oppurtuna in una lista

#(2)
#prevedere la possibilità di fare il login inserendo solite cose
#se sono corrette fornire un messaggio di benvenuto a seconda del sesso


from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
         
    return render_template("relEs.html") #importa il file html



@app.route('/data', methods=['GET'])
def data():
    nome= request.args['Name']
    username = request.args['username']
    passs = request.args['password']
    ci = request.args['password2']
    sex= request.args['Sex']
    if passs == ci:
        lista.append({'nome':nome,'username':username,'password': ci,'sex:':sex})
        print(lista)
        return render_template("log.html") #importa il file html
    else:
        return render_template("404.html")


@app.route('/log', methods=['GET'])
def log():
    username_log=request.args["username"]
    passs_log=request.args["passs"]
    for utente in lista:
        if utente.username == username_log and utente.password == passs_log:
            return  render_template("benvenuto.html",nome_user=username_log)
            
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True) 
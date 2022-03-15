
# analizzare un sito web che permetta di visualizzare alcune informazioni sull’andamento 
# dell’epidemia di covid nel nostro paese a partire dai dati presenti nel 
# file : https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv
# l’utente sceglie la regione da un elenco (menù a tendina), clicca su un bottone e il sito deve visualizzare
# una tabella contenente relativa alla situazione di quel regione
# i dati da inserire nel menù a tendina devono essere caricati automaticamente dalla pagina

from flask import Flask,render_template
import pandas as pd
app = Flask(__name__)
url="https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv"
df = pd.read_csv(url)

#oi=df[(df['nome_area'] == 'Abruzzo')].to_html()

@app.route('/', methods=['GET','POST'])
def hello_world():
    Abruzzo = request.form.get('Abruzzo')
    Calabria=request.form.get('Calabria')
    Campania=request.form.get('Campania')
    if Abruzzo == Abruzzo:
      return 


    return render_template("nonCapisco.html",  oi=df[(df['nome_area'] == 'Abruzzo')].to_html())
     #importa il file html


@app.route('/it', methods=['GET'])
def ciao_Mondo():
    return render_template("#.html") #importa il file html

# da qui non si puo mettere nientaltro 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
#realizzare un file web che ti permetta di conoscere capolughi di regioni l'utente inserisce il capoluogo è il programma restituisce il capoluogo
#caricare i capoluoghi di regioni in un oppuruna struttura dati


#1()
#mosificare l'esercizio precedente per permettere l'utente di inserire il capoluogo del regione 

#l'utente scegli se avere la regione o il capoluogo selezionando con un radioBUTTON;; 

from flask import Flask,render_template
app = Flask(__name__)


capGeo={'Abruzzo': 'LAquila', 'Basilicata': 'Potenza', 'Calabria': 'Catanzaro', 'Campania': 'Napoli', 'Emilia-Romagna': 'Bologna', 'Friuli-Venezia Giulia': 'Trieste', 'Lazio': 'Roma', 'Liguria': 'Genova', 'Lombardia': 'Ancona', 'Marche': 'Milano', 'Molise': 'Campobasso', 'Piemonte': 'Torino', 'Puglia': 'Bari', 'Sardegna': 'Cagliari', 'Sicilia': 'Palermo', 'Toscana': 'Firenze', 'Trentino-Alto-Adige': 'Trento', 'Umbria': 'Perugia', 'Vale dAosta': 'Aosta', 'Veneto': 'Venezia'}
@app.route('/', methods=['GET'])
def hello_world():
  return render_template("realiz.html",ui=c) #importa il file html


@app.route('/it', methods=['GET'])
def ciao_Mondo():
    return render_template("#.html") #importa il file html

# da qui non si puo mettere nientaltro 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
#realizzare un file web che ti permetta di conoscere capolughi di regioni l'utente inserisce il capoluogo è il programma restituisce il capoluogo
#caricare i capoluoghi di regioni in un oppuruna struttura dati


#1()
#modificare l'esercizio precedente per permettere l'utente di inserire il capoluogo del regione 

#l'utente scegli se avere la regione o il capoluogo selezionando con un radioBUTTON;; 

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

capoluoghiRegione = {'Abruzzo': 'Aquila', 'Basilicata': 'Potenza', 'Calabria': 'Catanzaro', 'Campania': 'Napoli','Emilia-Romagna': 'Bologna','FriuliVeneziaGiulia': 'Trieste', 'Lazio': 'Roma', 'Liguria': 'Genova','Lombardia': 'Milano','Marche': 'Ancona', 'Molise': 'Campobasso','Piemonte': 'Torino', 'Puglia': 'Bari', 'Sardegna': 'Cagliari', 'Sicilia': 'Palermo', 'Toscana': 'Firenze', 'Trentino-Alto-Adige': 'Trento', 'Umbria': 'Perugia', 'Valle Daosta': 'Aosta', 'Veneto': 'Venezia'}

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("wecome1.html") #importa il file html


@app.route('/output', methods=['GET'])
def risp():
    indice = request.args['indice']
    radio = request.args['sel']
    if radio == 'regione':
        if indice in capoluoghiRegione:
            capo = capoluoghiRegione[indice]
            return render_template('wecome.html', wabol=capo)
        return render_template('404.html')
    if radio == 'capoluogo':
        dct = {v: k for k, v in capoluoghiRegione.items()}
        if indice in dct:
            capo = dct[indice]
            return render_template('wecome.html', wabol=capo)
        return render_template('404.html')
    return render_template('404.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

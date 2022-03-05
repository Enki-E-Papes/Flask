from flask import Flask, render_template
from datetime import datetime
import random as rd
app = Flask(__name__)




@app.route('/', methods=['GET'])
def index():
    return render_template('risp.html')

@app.route('/meteo', methods=['GET'])
def meteo():
    n = rd.randint(0, 8)
    if n <= 2:
      previsione = 'rains cloudy'
      tempo = 'pioggia'
    else:
      if n >= 3 & n < 5:
        previsione = 'cloudy'
        tempo = 'nuvolo'
      if n > 5:
        previsione = 'sunny'
        tempo = 'sole'
    return render_template('by.html', ti = previsione, tempo = tempo)


@app.route('/frasiGolb', methods=['GET'])
def frasi():
  frasi = {1 : 'Chi comincia ad amare, deve essere pronto a soffrire., (Antoine Gombaud)', 2 : 'Tutto insegna, maturando, il tempo, (Eschilo)', 3 : 'Più piccola è la mente più grande è la presunzione , (Esopo)', 
           4 : 'Morire non è nulla, non vivere è spaventoso , (Victor Hugo)', 5 : 'Chi non osa nulla, non speri in nulla, (Friedrich von Schiller)', 
           6 : 'La pace comincia con un sorriso, (Madre Teresa di Calcutta)', 7:'A volte uno paga di più le cose che ha avuto gratis, (Albert Einstein)', 
           8:'Le cose non cambiano; siamo noi che cambiamo, (Henry David Thoreau)',9: 'La vita è imparare ad amare, (Abbé Pierre)',10:'L’ironia è sprecata quando si usa sugli stupidi, (Oscar Wilde)'}
  n1 = rd.randint(1, 10)
  frase = frasi[n1]
  return render_template('ciaociao.html', frase=frase, ran=n1)


@app.route('/quantomanca', methods=['GET'])
def quantomanca():
  oggi = datetime.now()
  Lafine = datetime(day=8, month=6, year=2022)
  differenza= fine - oggi
  return render_template('fineScuola.html', fine=differenza.days)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
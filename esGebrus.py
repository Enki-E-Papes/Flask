from flask import Flask, render_template, request, Response
app = Flask(__name__)


import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io
import pandas as pd

stazioni = pd.read_csv("/workspace/Flask/templates/ingressi_areac_varchi.csv",sep= ";")
stazionigeo=gpd.read_file("/workspace/Flask/templates/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson",sep= ";") 
quartieri =gpd.read_file("/workspace/Flask/templates/GeoDataFrameLichSenpai13^ds964_nil_wm.zip")

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/numero', methods=['GET'])
def numero():
#numero stazioni per ogni munnicipio
    global risultato
    risultato = stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()
    return render_template("elenco.html",risultato = risultato.to_html())

@app.route('/grafico', methods=['GET'])
def grafico():
    #costruzione del grafico
    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.OPERATORE

    ax.bar(x, y, color = "#304C89")
    #visualizzazione del grafico
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/selezione', methods=['GET'])
def selezione():
    scelta=request.args["scelta"]
    if scelta == "es1":
        return redirect(url_for("/numero"))
    return render_template("home.html")

@app.route('/input', methods=['GET'])
def input():
    return render_template("input.html")


@app.route('/ricerca', methods=['GET'])
def ricerca():
    global quartiere,stazioni_quartire
    nomequartiere=request.args["quartiere"]
    quartiere=quartieri[quartieri.NIL.str.contains(nomequartiere)]
    stazioni_quartire= stazionigeo[stazionigeo.within(quartiere.unary_union)]
    return render_template("elenco1.html",risultato=stazioni_quartire.to_html())

@app.route('/mappa', methods=['GET'])
def mappa():
    fig,ax =plt 
   
    return render_template("elenco.html",risultato = risultato.to_html())

@app.route('/drop_down', methods=['GET'])
def drop_down():
    nomi_stazioni = stazioni.OPERATRE.to_list()
    nomi_stazioni =list(set(nomi_stazioni))
    nomi_stazioni = nomi_stazioni.sort()
    return render_template("DropDown.html",stazioni = risultato.to_html())

@app.route('/scleStaz', methods=['GET'])
def scleStazv():
     
    stazione= request.args["stazione"]
    stazione_utente=stazionigeo[stazionigeo.OPERATORE==stazione]
    quartiere=quartieri[quartieri.contains(stazione_utente.geometry.squee)]
    

    return render_template("vistStazione.html",stazioni = risultato.to_html())
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
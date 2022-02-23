from flask import Flask,render_template
from datetime import datetime
import pytz

app = Flask(__name__)

#########################################################


#########################################################

@app.route('/', methods=['GET'])
def hello_world():
  return ("""<style="background-color:red">""")

cio=pytz.timezone('Europe/Rome')

ciocio=datetime.now(cio)
print(ciocio)
c=ciocio.strftime("%H:%M:%S %Z")    



# da qui non si puo mettere nientaltro
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
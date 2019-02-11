# services_adlibug.py - Flask wrapper for gvp2ax.py

from flask import Flask, request, Response, render_template
import sys

import gvp2ax as gvp

app = Flask(__name__)

valid_langs = ['nl', 'en', 'de', 'fr']

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/index_EN')
def index_EN():
    return render_template('index_EN.html')    

@app.route('/aat/search')
def search():
    term = request.args.get('term', default='')
    lang = request.args.get('lang', default='nl').lower()
    if lang not in valid_langs:
        lang = 'nl'

    Adlibxml = gvp.AAT(term, lang)    
    return Response(Adlibxml, mimetype='application/xml')
        
if __name__ == "__main__":
    app.run()

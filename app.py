#Importing Necessary modules
from flask import Flask, request, render_template
from sqlalchemy.sql.expression import true
from werkzeug.utils import redirect 
from datadumper import *


app = Flask(__name__)

@app.route('/')  
def dis():
    res=display()
    res=convert_json(res)
    return render_template('index.html',result=res)

@app.route('/letter', methods=['GET', 'POST'])    
def letter(): 
    selected_alphabet = request.args.get("letter")
    print(selected_alphabet)
    res=alphabetsearch(selected_alphabet)
    res=convert_json(res)
    return render_template('index.html',result=res)


@app.route('/search', methods=['GET','POST'])
def search():
    s = request.form.get("search")
    res=alphabetsearch(s)
    res=convert_json(res)
    return render_template('index.html',result=res)

@app.route('/createe', methods=['GET','POST'])
def createe():
    
    gene = request.form.get("genecreate")
    trans = request.form.get("transcreate")
    res=create(gene,trans)
    res=convert_json(res)
    return render_template('index.html',result=res)

@app.route('/updatee', methods=['GET','POST'])
def updatee():
    gene = request.form.get("geneupdate")
    trans = request.form.get("transupdate")
    res=update(gene,trans)
    res=convert_json(res)
    return render_template('index.html',result=res)

@app.route('/deletee', methods=['GET','POST'])
def deletee():
    gene = request.form.get("delete")
    res=delete(gene)
    res=convert_json(res)
    return render_template('index.html',result=res)


if __name__ == '__main__':
   app.run()

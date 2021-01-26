from flask import Flask
from flask import render_template, request, redirect

import pickle


app = Flask('Noteboook')

data = [
        {'title': 'Note 1', 'content': 'first note'},
        {'title': 'Note 2', 'content': 'second note'}
        ]

@app.route('/')
def home():
   # filename = 'pickle'
   # infile = open(filename,'rb')
   # data = pickle.load(infile)
   # infile.close()
    return render_template('home.html', data = data)


@app.route('/addNote', methods=["POST"])
def addNote():
    data.append({'title': request.form['title'], 'content': request.form['content']})
    #filename = 'pickle'
    #outfile = open(filename, 'wb')
    #pickle.dump(data,outfile)
    #outfile.close()
    return redirect('/')





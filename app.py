from flask import *

app = Flask(__name__)
app.debug = True
app.secret_key = 'Programmer-RD-AI'

@app.route('/')
def home():
    return render_template('./home/home.html')

@app.route('/Lessons')
def lesson():
    return render_template('./home/lessons.html')

@app.route('/Science A+')
def science_a_plus():
    return render_template('./home/science-A+.html')
if __name__ == '__main__':
    app.run(host='192.168.1.9')

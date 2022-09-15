from flask import Flask, render_template

app=Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return "THIS IS MY FIRST --- WEB APPLICATION!"
@app.route('/home/<name>')
def hello(name):
    return "Hello "+ name;
@app.route('/empid/<int:id>')
def empInfo(id):
    return "Your employee ID is : {} ".format(id);
@app.route('/info')
def informations():
    return render_template('info.html')

if __name__=='__main__':
    app.run(port=5001)



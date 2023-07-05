from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play', methods = [ 'GET'])
def play():
    return render_template('index.html', cajas=3, color='blue')

@app.route('/play/<int:num>', methods = [ 'GET'])
def play_x(num):
    return render_template('index.html', cajas=num, color='blue')

@app.route('/play/<int:num>/<color>', methods = [ 'GET'])
def play_x_color(num, color):
    return render_template('index.html', cajas=num, color=color)

if __name__ == '__main__':
    app.run( debug= True, port=5000 )
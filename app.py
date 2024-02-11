from flask_mysqldb import MySQL
from flask import Flask 
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '74863840'
app.config['MYSQL_DB'] = 'colegio4'

mysql = MySQL(app)

@app.route('/')
def index (): 
    return render_template('index.html')

@app.route('/dashboard')
def dashboard(): 
    return render_template ('dashboard.html')

@app.route('/insertar')
def formulario_insertar(): 
    return render_template('form.html')

@app.route('/insertar_datos', methods=['POST'])
def insert_datos():
    if request.method == 'POST':
        id_persona = request.form['id_persona']
        direccion = request.form['direccion']
        nombre = request.form['nombre']
        apellido_pat = request.form['apellido_pat']
        apellido_mat = request.form['apellido_mat']
        conn = mysql.connection
        cur = conn.cursor()
        cur.execute("INSERT INTO persona (id_persona, direccion, nombre, apellido_pat, apellido_mat) VALUES (%s, %s, %s, %s, %s)", (id_persona, direccion, nombre, apellido_pat, apellido_mat))
        conn.commit()
        cur.close()
        return redirect(url_for('dashboard'))

@app.route('/mostrar_datos')
def mostrar_datos():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute("SELECT * FROM persona")
    datos = cur.fetchall()
    cur.close()
    return render_template('datos.html', datos=datos)

if __name__== '__main__':
    app.run(debug=True, port =5000)

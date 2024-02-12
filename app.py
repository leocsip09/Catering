from flask_mysqldb import MySQL
from flask import Flask 
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ocsip'
app.config['MYSQL_DB'] =  'catering'

contra = '74863840'

mysql = MySQL(app)

@app.route('/')
def index (): 
    return render_template('index.html')

@app.route('/cotizar')
def dashboard(): 
    return render_template ('cotizar.html')

@app.route('/sesion')
def sesion():
    return render_template('sesion.html')

@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

@app.route('/ingresar_servicio')
def ingresar_servicio():
    return render_template('ingresar_servicio.html')

@app.route('/insertar')
def formulario_insertar(): 
    return render_template('form.html')

@app.route('/insertar_datos', methods=['POST'])
def insert_datos():
    if request.method == 'POST':
        dni = request.form['dni']
        primer_nombre = request.form['primer_nombre']
        segundo_nombre = request.form['segundo_nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        correo=request.form['correo']
        telefono= request.form['telefono']
        departamento=request.form['departamento']
        ciudad=request.form['ciudad']
        notas_adicionales=request.form['notas_adicionales']
        conn = mysql.connection
        cur = conn.cursor()
        cur.callproc('insertar', (dni,primer_nombre,segundo_nombre,apellido_paterno,apellido_materno,correo,telefono,departamento,ciudad,notas_adicionales))
        conn.commit()
        cur.close()
        return redirect(url_for('index'))

@app.route('/mostrar_datos')
def mostrar_datos():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute("SELECT * FROM persona")
    datos = cur.fetchall()
    cur.close()
    return render_template('datos.html', datos=datos)
if __name__== '__main__':
    app.run(debug=True)

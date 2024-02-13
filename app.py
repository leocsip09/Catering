from flask_mysqldb import MySQL
from flask import Flask 
from flask import flash
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'catering'

mysql = MySQL(app)

@app.route('/')
def index (): 
    return render_template('index.html')

@app.route('/cotizar')
def dashboard(): 
    return render_template ('cotizar.html')

@app.route('/ingresar_empleado')
def ingresar_empleado():
    return render_template('ingresar_empleado.html')

@app.route('/agregar_proveedor')
def proveedor():
    return render_template('agregar_proveedor.html')

@app.route('/agregar_ingrediente')
def agregar_ingrediente():
    return render_template('agregar_ingrediente.html')

@app.route('/agregar_producto')
def producto():
    return render_template('agregar_producto.html')
@app.route('/comentario')
def comentario():
    return render_template('comentario.html')

@app.route('/sesion')
def sesion():
    return render_template('sesion.html')

@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

@app.route('/ingresar_servicio')
def ingresar_servicio():
    return render_template('ingresar_servicio.html')

@app.route('/ingresar_menu')
def ingresar_menu():
    return render_template('ingresar_menu.html')

@app.route('/actualizar_dato')
def actualizar_dato():
    return render_template('actualizar_dato.html')

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
        nombre_evento=request.form['nombre_evento']
        fecha_evento=request.form['fecha_evento']
        hora_inicio=request.form['hora_inicio']
        hora_fin=request.form['hora_fin']
        tipo_evento=request.form['tipo_evento']
        ubicacion_evento=request.form['ubicacion_evento']
        cantidad=request.form['cantidad']
        tipo_servicio=request.form['tipo_servicio']
        cantidad_personas=request.form['cantidad_personas']
        nombre_menu=request.form['nombre_menu']
        metodo_pago=request.form['metodo_pago']
        conn = mysql.connection
        cur = conn.cursor()
        cur.callproc('insertar', (dni,primer_nombre,segundo_nombre,apellido_paterno,apellido_materno,correo,telefono,departamento,ciudad,notas_adicionales,nombre_evento,fecha_evento,hora_inicio,hora_fin,tipo_evento,ubicacion_evento,cantidad,tipo_servicio,cantidad_personas,nombre_menu,metodo_pago))
        conn.commit()
        cur.close()
        return redirect(url_for('mostrar_factura', dni=dni))

@app.route ('/ingresar_empleados', methods=['POST'])
def ingresar_empleados():
    if request.method=='POST':
        dni = request.form['dni']
        primer_nombre = request.form['primer_nombre']
        segundo_nombre = request.form['segundo_nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        correo=request.form['correo']
        telefono= request.form['telefono']
        fecha_contratacion=request.form['fecha_contratacion']
        puesto=request.form['puesto']
        direccion=request.form['direccion']
        salario=request.form['salario']
        id_evento=request.form['id_evento']
        hora_inicio=request.form['hora_inicio']
        hora_fin=request.form['hora_fin']
        fecha=request.form['fecha']
        conn= mysql.connection
        cur=conn.cursor()
        cur.callproc('ingresar_empleados',(dni,primer_nombre,segundo_nombre,apellido_paterno,apellido_materno,correo,telefono,fecha_contratacion,puesto,direccion,salario,id_evento,hora_inicio,hora_fin,fecha))
        conn.commit()
        cur.close()
        return redirect(url_for('administrador'))

@app.route('/actualizar_datos',methods=['POST'])
def actualizar_datos():
    if request.method== 'POST':
        dni_param = request.form['dni_param']
        fecha_contratacion_param = request.form['fecha_contratacion_param']
        puesto_param = request.form['puesto_param']
        direccion_param = request.form['direccion_param']
        salario_param = request.form['salario_param']
        id_evento_param = request.form['id_evento_param']
        conn=mysql.connection
        cur=conn.cursor()
        cur.callproc('actualizar_datos',(dni_param, fecha_contratacion_param, puesto_param, direccion_param, salario_param, id_evento_param))
        conn.commit()
        cur.close()
        return redirect(url_for('administrador'))
    
@app.route('/ingresar_comentario',methods=['POST'])
def ingresar_comentario():
    if request.method=='POST':
        comentario = request.form['comentario']
        calificacion = request.form['calificacion']
        dni_cliente = request.form['dni_cliente']
        conn=mysql.connection
        cur=conn.cursor()
        cur.callproc('comentario',(comentario,calificacion,dni_cliente))
        conn.commit()
        cur.close()
        return redirect(url_for('index'))

@app.route('/ingresar_proveedor',methods=['POST'])
def ingresar_proveedor():
    if request.method=='POST':
        nom_prv = request.form['nom_prv']
        tel = request.form['tel']
        cor = request.form['cor']
        dir = request.form['dir']
        dep = request.form['dep']
        ciu = request.form['ciu']
        conn=mysql.connection
        cur=conn.cursor()
        cur.callproc('Insertar_Proveedor',(nom_prv,tel,cor,dir,dep,ciu))
        conn.commit()
        cur.close()
        return redirect(url_for('administrador'))

@app.route('/ingresar_producto',methods=['POST'])
def ingresar_producto():
    if request.method=='POS':
        nom_prod = request.form['nom_prod']
        cant = request.form['cant']
        unidad = request.form['unidad']
        precio = request.form['precio']
        dep = request.form['dep']
        proveedor = request.form['proveedor']
        conn=mysql.connection
        cur=conn.cursor()
        cur.callproc('Insertar_Inventario',(nom_prod,cant,unidad,precio,dep,proveedor))
        conn.commit()
        cur.close()
        return redirect(url_for('administrador'))

@app.route('/ingresar_ingrediente',methods=['POST'])
def ingresar_ingrediente():
    if request.method=='POS':
        nom_ingr = request.form['nom_ingr']
        cant_req = request.form['cant_req']
        id_men = request.form['id_men']
        id_prov = request.form['id_prov']
        conn=mysql.connection
        cur=conn.cursor()
        cur.callproc('Agregar_Ingrediente',(nom_ingr,cant_req,id_men,id_prov))
        conn.commit()
        cur.close()
        return redirect(url_for('administrador'))

@app.route ('/ingresar_menus',methods=['POST'])
def ingresar_menus():
    if request.method=='POST':
        precio_persona=request.form['precio_persona']
        nombre_menu=request.form['nombre_menu']
        conn=mysql.connection
        cur=conn.cursor()
        cur.callproc('ingresar_servicio',(precio_persona,nombre_menu))
        conn.commit()
        cur.close()
        return redirect('administrador')
    
@app.route('/factura', methods=['POST'])
def factura():
    if request.method=='POST':
        conn=mysql.connection
        cur=conn.cursor()
        cur.callproc('facturar')
        cur.close()
        return redirect(url_for('mostrar_factura'))
    
@app.route('/mostrar_factura')
def mostrar_factura():
    conn = mysql.connection
    cur = conn.cursor()
    cur.callproc('facturar')
    conn.commit()
    cur.callproc('mostrar_factura')
    datos = cur.fetchall()
    cur.close()
    return render_template('mostrar_factura.html', datos=datos)

@app.route('/mostrar_servicios')
def mostrar_servicios():
    conn = mysql.connection
    cur = conn.cursor()
    cur.callproc('mostrar_servicios2')
    evento = cur.fetchall()
    cur.close()
    cur = conn.cursor()  
    cur.callproc('mostrar_servicios1')
    menu = cur.fetchall()
    cur.close()
    return render_template('mostrar_servicios.html',evento=evento,menu=menu)

@app.route('/mostrar_ingredientes')
def mostrar_ingredientes():
    conn = mysql.connection
    cur = conn.cursor()
    cur.callproc('Mostrar_IngredientesMenu')
    ing = cur.fetchall()
    cur.close()
    return render_template('mostrar_ingrediente.html', ing=ing)

@app.route('/mostrar_datos')
def mostrar_datos():
    conn = mysql.connection
    cur = conn.cursor()
    cur.callproc('mostrar_venta')
    venta = cur.fetchall()
    cur.close()
    return render_template('datos_facturas.html', venta=venta)
if __name__== '__main__':
    app.run(debug=True, port =5000)

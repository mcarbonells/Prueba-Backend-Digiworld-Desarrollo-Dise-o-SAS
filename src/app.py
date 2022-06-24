from distutils.log import debug
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from config import config
from jwtFuntion import write_token, val_token
import bcrypt
from re import split

app = Flask(__name__)

conexion = MySQL(app)
    
@app.route('/')
def home():
    return 'Pagina Principal'

#CRUD TASK
@app.route('/api/create_task', methods = ['POST'])
def create_task():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO task (NAME, DESCRIPTION, SEND_DATE) VALUES ('{0}', '{1}', '{2}')".format(request.json['NAME'], request.json['DESCRIPTION'], request.json['SEND_DATE'])
        cursor.execute(sql)
        conexion.connection.commit()
        
        response = {'data': request.json, 'menssage': 'Tarea Creada'}
        return jsonify(response)
    except Exception as ex:
        return jsonify({'menssage': 'error'})

@app.route('/api/update_task/<id>', methods = ['PUT'])
def update_task(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE task SET NAME = '{0}', DESCRIPTION = '{1}', SEND_DATE = '{2}' WHERE IDT = '{3}'".format(request.json['NAME'], request.json['DESCRIPTION'], request.json['SEND_DATE'], id)
        cursor.execute(sql)
        conexion.connection.commit()
        
        response = {'data': request.json, 'id': id, 'menssage': 'Tarea Actualizada'}
        return jsonify(response)
    except Exception as ex:
        return jsonify({'menssage': 'error'})

@app.route('/api/delete_task/<id>', methods = ['DELETE'])
def delete_task(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM task  WHERE IDT = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        
        response = {'data': id, 'menssage': 'Tarea Eliminada'}
        return jsonify(response)
    except Exception as ex:
        return jsonify({'menssage': 'error'})

@app.route('/api/get_task/<id>', methods = ['GET'])
def get_task(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDT, NAME, DESCRIPTION, SEND_DATE FROM task WHERE IDT = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchall()
        if  datos != None:
            task = {'IDT': datos[0][0], 'NAME': datos[0][1],' DESCRIPTION': datos[0][2], 'SEND_DATE': datos[0][3]}
            response = {'data': task, 'menssage': 'success'}
        else:
            response = {'menssage': 'Tarea no encontrada'}
        return jsonify(response)
    except Exception as ex:
        return jsonify({'menssage': 'error'})

@app.route('/api/get_all_task', methods = ['GET'])
def get_all_task():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IDT, NAME, DESCRIPTION, SEND_DATE FROM task"
        cursor.execute(sql)
        datos = cursor.fetchall()
        tasks = []
        for line in datos:
            task = {'IDT': line[0], 'NAME': line[1],' DESCRIPTION': line[2], 'SEND_DATE': line[3]}
            tasks.append(task)
        response = {'data': tasks, 'menssage': 'success'}
        return jsonify(response)
    except Exception as ex:
        return jsonify({'menssage': 'error'})
    

#Login
@app.route('/login', methods = ["POST"])
def login():
    username = request.json['USERNAME']
    password = request.json['PASSWORD']
    check = password.encode("utf-8")
    
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT USERNAME, PASSWORD FROM users WHERE USERNAME = '{0}'".format(username)
        cursor.execute(sql)
        datos = cursor.fetchall()
        if  datos != None:
            passworddb = datos[0][1]
            passworddb = passworddb.encode("utf-8")
            if  bcrypt.checkpw(check, passworddb):
                token = write_token(data=request.json)
                response = {'token': token.decode("utf-8"), 'menssage': 'Usuario exitosamente logeado'}
            else:
              response = {'menssage': 'Contraseña incorrecta'}
              response.status_code = 404 
        else:
            response = {'menssage': 'Usuario no encontrado'}
            response.status_code = 404
        return jsonify(response)
    except Exception as ex:
        return jsonify({'menssage': 'error'})
    
#VALIDATE TOKEN
@app.route('/verify_token', methods = ["GET"])
def verify_token():
    token = request.headers['Authorization'].split(" ")[1]
    return val_token(token, output=True)
    
  
#REGISTRO
@app.route('/register', methods = ["POST"])
def register():
    password = request.json['PASSWORD']
    password = password.encode("utf-8")
    encoded = bcrypt.hashpw(password, bcrypt.gensalt(10)) 
    encoded = encoded.decode("utf-8")
    
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO users (NAME, LASTNAME, USERNAME, EMAIL, PASSWORD) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(
            request.json['NAME'], request.json['LASTNAME'], request.json['USERNAME'], request.json['EMAIL'], encoded)
        cursor.execute(sql)
        conexion.connection.commit()
        
        request.json['PASSWORD'] = str(encoded)
        
        response = {'data': request.json, 'menssage': 'Registro Exitoso'}
        return jsonify(response)
    except Exception as ex:
        return jsonify({'menssage': 'error'})

        
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug = True)
    
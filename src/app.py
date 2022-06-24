from flask import Flask, request
from flask_mysqldb import MySQL
from flask import jsonify
from config import config

app = Flask(__name__)

conexion = MySQL(app)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
    
@app.route('/')
def home():
    return 'HOLA MUNDO'

@app.route('/api/create_task', methods = ['POST'])
def create_task():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO task (IDT, NAME, DESCRIPTION, SEND_DATE) VALUES ('{0}', '{1}', '{2}')".format(request.json['NAME'], request.json['DESCRIPTION'], request.json['SEND_DATE'])
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
        
        response = {'data': request.json, 'id': id, 'menssage': 'Tarea Creada'}
        return jsonify(response)
    except Exception as ex:
        return jsonify({'menssage': 'error'})

@app.route('/api/delete_task/<id>', methods = ['DELETE'])
def delete_task():
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
            task = {'IDT': datos[0], 'NAME': datos[1],' DESCRIPTION': datos[2], 'SEND_DATE': datos[3]}
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
    
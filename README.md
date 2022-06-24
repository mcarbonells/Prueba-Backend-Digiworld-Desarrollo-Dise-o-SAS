# Prueba-Backend-Digiworld-Desarrollo-Dise-o-SAS
## Base de Datos
La base de datos usada esta descrita en el archivo llamado db. 

## Packetes necesarios para descargar
*Flask
*Flask-MySQLdb
*PyJWT
*bcrypt

## Prueba del CRUD sobre la tabla TASK
**Crear nueva tarea**

POST http://127.0.0.1:5000/api/create_task (o http://localhost:5000/api/create_task)

body raw tipo JSON:
{
  "NAME": "Tarea Matematicas",
  "DESCRIPTION": "Ecuaciones matematicas de una variable",
  "SEND_DATE": "2022-07-21"
}

{
  "NAME": "Tarea Historia",
  "DESCRIPTION": "Ensayo revolucion rusa",
  "SEND_DATE": "2022-08-06"
}

{
  "NAME": "Tarea Fisica",
  "DESCRIPTION": "Ejercicios teoricos fuerzas",
  "SEND_DATE": "2022-07-15"
}


**Ver todas las tareas**

GET http://127.0.0.1:5000/api/get_all_task (o http://localhost:5000/api/get_all_task)


**Ver una tarea**

GET http://127.0.0.1:5000/api/get_task/1 (o http://localhost:5000/api/get_task/1)

GET http://127.0.0.1:5000/api/get_task/2 (o http://localhost:5000/api/get_task/2)


**Update una tarea**

PUT http://127.0.0.1:5000/api/update_task/1 (o http://localhost:5000/api/update_task/1)

body raw tipo JSON:
{
  "NAME": "Tarea Biologia",
  "DESCRIPTION": "Celula Vegetal con Dulces",
  "SEND_DATE": "2022-08-01"
}

PUT http://127.0.0.1:5000/api/update_task/2 (o http://localhost:5000/api/update_task/2)

body raw tipo JSON:
{
  "NAME": "Tarea Historia",
  "DESCRIPTION": "Ensayo revolucion rusa comparacion con francesa",
  "SEND_DATE": "2022-08-10"
}


**Eliminar una tarea**

DELETE http://127.0.0.1:5000/api/delete_task/1 (o http://localhost:5000/api/delete_task/1)

DELETE http://127.0.0.1:5000/api/delete_task/2 (o http://localhost:5000/api/delete_task/2)


## Login Registro y Validación token
**REGISTER**

POST http://127.0.0.1:5000/register (o http://localhost:5000/register)

body raw tipo JSON:
{
    "NAME": "Maria Fernanda",
    "LASTNAME": "Carbonell Santos",
    "USERNAME": "mafecarbo",
    "EMAIL": "mcarbonells@unal.edu.co",
    "PASSWORD": "123Mafe"
}


**LOGIN**

POST http://127.0.0.1:5000/login (o  http://localhost:5000/login)

body raw tipo JSON:
{
    "USERNAME": "mafecarbo",
    "PASSWORD": "123Mafe"
}


**VERIFY TOKEN**

GET http://127.0.0.1:5000/verify_token (o  http://localhost:5000/verify_token)

Authorization BearerToken Token del login


## PostMan
https://www.getpostman.com/collections/5fe7e2d7de3785c324ba


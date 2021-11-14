from dns import exception
from flask import Flask
from flask import  jsonify, make_response,  request,make_response,abort
import json

from flask import request
from flask.json import dump
from pymongo import MongoClient
import ssl

app = Flask(__name__)

client= MongoClient('mongodb+srv://test:test@cluster0.oh46f.mongodb.net/DeportesDB',ssl_cert_reqs=ssl.CERT_NONE)
db= client.ContactDB
contacto= [
    {
        'id':1,
        'nombre':'juan'
    },{
        'id':2,
        'nombre':'Julian'
    }
]

@app.route('/')
def pruebaRaiz():
    return 'Hola Mundo'

@app.route('/contacto/<int:contacto_id>',methods = ['GET'] )
def getContacto(contacto_id):
    return jsonify(
        {'id':contacto_id},
        {'contacto':contacto}
    )

@app.route('/contacto',methods = ['POST'] )
def recibirContacto():
    data= json.loads(request.data)
    idContact= data['id']
    nombreContacto= data['nombre']

    contactoTmp={
        'numeroDocumento': idContact,
        'nombre':nombreContacto
    }
    contacto.append(contactoTmp)
    return jsonify(
        {'contacto':contacto}
    )

@app.route('/contactoDb',methods = ['POST'] )
def recibirContactoDb():
    try:
        data= json.loads(request.data)
        idContact= data['id']
        nombreContacto= data['nombre']

        contactoTmp={
            'numeroDocumento': idContact,
            'nombre':nombreContacto
        }
        db.Contacts.insert_one(contactoTmp)


        return jsonify(
            {'status':"sussess"}
        ), 200
    except Exception as error:
        return dump({'Error': error})


@app.route('/contactoConsultaDb',methods = ['POST'] )
def recibirContactoConsultaDb():
    try:
        for x in db.Contacts.find():
            print(x)

        return json.loads(request.data)
    except Exception as error:
        return dump({'Error': error})

if __name__ =='__main__':
    app.run(debug=True)
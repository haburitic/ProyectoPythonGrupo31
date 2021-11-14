from flask import Flask
from flask import  jsonify, make_response,  request,make_response,abort
import json

from flask import request
app = Flask(__name__)

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
    data= json.loads(request.data)
    idContact= data['id']
    nombreContacto= data['nombre']

    contactoTmp={
        'numeroDocumento': idContact,
        'nombre':nombreContacto
    }
    
    return jsonify(
        {'contacto':contacto}
    )

if __name__ =='__main__':
    app.run(debug=True)
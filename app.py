from flask import Flask
from flask import  jsonify, make_response,  request,make_response,abort

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


if __name__ =='__main__':
    app.run(debug=True)
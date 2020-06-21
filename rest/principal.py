from flask import Flask, request, Response, jsonify
import json
import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from core.controller.test.TestController import *

app = Flask(__name__)

@app.route('/test/insertar', methods=['POST'])
def insertarAsesino():
    data = request.get_json()
    print(data)
    testController = TestController()
    test = testController.insertar(data['nombre'], data['intentos'])
    return json.dumps(test.__dict__ )

 
@app.route('/test/listar', methods=['GET'])
def listarTest():    
    testController = TestController()
    my_tests = testController.listarTodo()
    return json.dumps([test.__dict__ for test in my_tests])


'''En vista debe existir un scritp que controle el tiempo de sesion, unos minutos antes de la hora el deberia actualizar el token'''
    
app.run(debug=True)





















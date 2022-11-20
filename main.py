from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado

miControladorCandidato=ControladorCandidato()
miControladorPartido = ControladorPartido()
miControladorMesa = ControladorMesa()
miControladorResultado = ControladorResultado()

"""CANDIDATOS"""

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
@app.route("/Candidato",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/Candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/Candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/Candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/Candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

"""PARTIDOS"""

@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)


"""MESA"""

@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas", methods=['POST'])
def createMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getmesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)

@app.route("/mesas/mayor_participacion",methods=['GET'])
def getNotasMayores():
    json=miControladorMesa.votomasAltoxmesa()
    return jsonify(json)


""""RELACION CANDIDATOS & PARTIDOS"""

@app.route("/Candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartido(id, id_partido):
    json = miControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)


"""RESULTADO"""

@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)
@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['POST'])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>", methods=['PUT'])
def updateResultado(id_resultado):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado,data)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>", methods=['DELETE'])
def deleteResult(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_candidato>",methods=['GET'])
def resultadoxCandidato(id_candidato):
    json=miControladorResultado.listarResultadosxCandidato(id_candidato)
    return jsonify(json)

@app.route("/resultados/suma_votos/candidato/<string:id_candidato>",methods=['GET'])
def getSumaVotosXCandidato(id_candidato):
    json=miControladorResultado.sumaVotosxCandidato(id_candidato)
    return jsonify(json)



def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])



    """CONEXION A MONGO DB"""
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://User-3456:user3456@cluster0.5f9asz1.mongodb.net/votaciones2022_grupo5?retryWrites=true&w=majority")

db = client.test
print(db)
baseDatos = client["votaciones2022_grupo5"]
print(baseDatos.list_collection_names())
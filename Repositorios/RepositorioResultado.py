from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):

    def getListadoResultadosXCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def sumaVotosxCandidato(self, id_candidato):
        query1 = {
            "$match": {"candidato.$id": ObjectId(id_candidato)}
        }

        query2 = {
            "$group": {
                 "_id": "$candidato",
            "Totalvotos": {
                "$sum": "$total_votos"
                       }
                 }
         }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)
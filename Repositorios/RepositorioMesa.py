from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Mesa import Mesa



class RepositorioMesa(InterfaceRepositorio[Mesa]):
    def getMayorvotosxmesa(self):
        query1 = {
            "$group": {
                "_id": "$mesa",
                "max": {
                    "$max": "$votos"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }

        pipeline = [query1]
        return self.queryAggregation(pipeline)

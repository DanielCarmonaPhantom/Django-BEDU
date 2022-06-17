import graphene

class Query(graphene.ObjectType):
    ping = graphene.String()
    resta = graphene.Float(numa=graphene.Float(), numb=graphene.Float())

    def resolve_ping(root, info):
        return "pong"

    def reesolve_resta(root, info, numa, numb):
        return numa - numb

    

schema = graphene.Schema(query= Query, mutation=None)
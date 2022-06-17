from ctypes import DllGetClassObject
from dataclasses import fields
import graphene



from graphene_django import DjangoConnectionField, DjangoObjectType

from .models import Pokemon, Type

class TypeType(DllGetClassObject):
    class Metta:
        model = Type
        fields = '__alls__'

class CreateTypeMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    type = graphene.Field(TypeType)


    @classmethod
    def mutate(self, root, info, name):
        
        types = Type.objects.create(name=name)
        if types.exits():
            raise ValueError("El tipo ya existe")
        type = Type.objects.create(name=name)
        return CreateTypeMutation(type=type)



class PokemonType(DjangoConnectionField):
    class Meta:
        model = Pokemon
        fields = '__alls__'


class Query(graphene.ObjectType):
    all_pokemons = graphene.List(PokemonType)
    all_types = graphene.List(TypeType)

    def resolve_all_pokemons(root, info):
        return Pokemon.objects.select_related("").all()

    def resolve_all_types(root, info):
        return Type.objects.select_related 


class Mutation:
    create_type = CreateTypeMutation.Field()
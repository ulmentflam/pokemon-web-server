import hug

from falcon import HTTPBadRequest
from orator.exceptions.orm import ModelNotFound

from pokemon.schemas.base import Trainers, Pokemon
from psycopg2 import IntegrityError


@hug.post('/pokemon')
def create_pokemon(trainer_id: hug.types.number,
                   name: hug.types.text,
                   hp: hug.types.number,
                   level: hug.types.number,
                   type: hug.types.one_of(['normal', 'grass', 'fire', 'watter','flying', 'electric', 'ground', 'dragon','psychic', 'ghost'])):
    try:
        trainer = Trainers.find_or_fail(trainer_id)
    except ModelNotFound:
        raise HTTPBadRequest('trainer_not_found', 'Error finding trainer with this ID')

    try:
        new_pokemon = Pokemon()
        new_pokemon.name = name
        new_pokemon.hp = hp
        new_pokemon.level = level
        new_pokemon.type = type

        trainer.pokemon().save(new_pokemon)
    except IntegrityError:
        raise HTTPBadRequest('error_creating_trainer', 'Error creating trainer')

    return Pokemon.find(new_pokemon.id).serialize()


@hug.put('/pokemon')
def put_trainer(pokemon_id: hug.types.number,
                name: hug.types.text,
                hp: hug.types.number,
                level: hug.types.number,
                type: hug.types.one_of(['normal', 'grass', 'fire', 'water', 'flying', 'electric', 'ground', 'dragon', 'psychic', 'ghost'])):
    try:
        pokemon = Pokemon.find_or_fail(pokemon_id)
    except ModelNotFound:
        raise HTTPBadRequest('pokemon_not_found', 'Error finding a pokemon with this id.')
    try:
        if name:
            pokemon.name = name
        if hp:
            pokemon.hp = hp
        if level:
            pokemon.level = level
        if type:
            pokemon.type = type
        pokemon.save()
    except IntegrityError:
        raise HTTPBadRequest('error_creating_trainer', 'Error creating trainer')

    return Pokemon.find(pokemon.id).serialize()


@hug.patch('/pokemon')
def patch_trainer(pokemon_id: hug.types.number,
                name: hug.types.text = None,
                hp: hug.types.number = None,
                level: hug.types.number = None,
                type: hug.types.one_of(['normal', 'grass', 'fire', 'water', 'flying', 'electric', 'ground', 'dragon', 'psychic', 'ghost']) = None):
    try:
        pokemon = Pokemon.find_or_fail(pokemon_id)
    except ModelNotFound:
        raise HTTPBadRequest('pokemon_not_found', 'Error finding a pokemon with this id.')

    try:
        if name:
            pokemon.name = name
        if hp:
            pokemon.hp = hp
        if level:
            pokemon.level = level
        if type:
            pokemon.type = type
        pokemon.save()
    except IntegrityError:
        raise HTTPBadRequest('error_creating_trainer', 'Error creating trainer')

    return Pokemon.find(pokemon.id).serialize()


@hug.get('/pokemon/{pokemon_id}')
def get_pokemon(pokemon_id: hug.types.number):
    try:
        pokemon = Pokemon.find_or_fail(pokemon_id)
    except ModelNotFound:
        raise HTTPBadRequest('pokemon_not_found', 'Error finding a pokemon with this id.')

    return pokemon.serialize()

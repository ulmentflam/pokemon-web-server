import arrow
import secrets
import logging
import environs
from orator import Model, SoftDeletes, mutator
from orator.orm import (has_one, has_many, belongs_to, accessor, belongs_to_many, scope, has_many_through, morphed_by_many, morph_to_many)
from orator.database_manager import DatabaseManager

env = environs.Env()
log = logging.getLogger(__name__)

db = DatabaseManager({
    'postgres': {
        'driver': 'postgres',
        'host': env('POSTGRES_HOST'),
        'port': env('POSTGRES_PORT'),
        'database': env('POSTGRES_DB'),
        'user': env('POSTGRES_USER'),
        'password': env('POSTGRES_PASSWORD'),
        'prefix': '',
        'log_queries': True
    }
})
Model.set_connection_resolver(db)


class Trainers(Model):

    __fillable__ = ['name', 'gender', 'rival_name']
    __hidden__ = ['created_at', 'updated_at']
    __appends__ = []
    _with = ['pokemon']

    @belongs_to_many('trainer_pokemon', 'trainer_id', 'pokemon_id')
    def pokemon(self):
        return Pokemon


class Pokemon(Model):
    __fillable__ = ['name', 'hp', 'level', 'type']
    __hidden__ = ['created_at', 'updated_at']

    @has_many('pokemon_id')
    def attacks(self):
        return Attacks


class Attacks( Model):
    __fillable__ = ['name', 'hit_chance', 'damage', 'type']
    __hidden__ = ['created_at', 'updated_at']
    __appends__ = []

    @belongs_to('pokemon_id')
    def pokemon(self):
        return Pokemon
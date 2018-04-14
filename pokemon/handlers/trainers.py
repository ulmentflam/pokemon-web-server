import hug

from falcon import HTTPBadRequest
from orator.exceptions.orm import ModelNotFound

from pokemon.schemas.base import db, Trainers
from psycopg2 import IntegrityError


@hug.post('/trainers')
def create_trainer(name: hug.types.text,
                   gender: hug.types.one_of(['boy', 'girl', 'other']),
                   rival_name: hug.types.text):

    try:
        new_trainer = Trainers()
        new_trainer.name = name
        new_trainer.gender = gender
        new_trainer.rival_name = rival_name
        new_trainer.save()
    except IntegrityError:
        raise HTTPBadRequest('error_creating_trainer', 'Error creating trainer')

    return Trainers.find(new_trainer.id).serialize()


@hug.put('/trainers')
def put_trainer(trainer_id: hug.types.number,
                name: hug.types.text,
                gender: hug.types.one_of(['boy', 'girl', 'other']),
                rival_name: hug.types.text):

    try:
        trainer = Trainers.find_or_fail(trainer_id)
    except ModelNotFound:
        raise HTTPBadRequest('trainer_not_found', 'Error finding trainer with this ID')

    try:
        trainer.name = name
        trainer.gender = gender
        trainer.rival_name = rival_name
        trainer.save()
    except IntegrityError:
        raise HTTPBadRequest('error_creating_trainer', 'Error creating trainer')

    return Trainers.find(trainer.id).serialize()


@hug.patch('/trainers')
def patch_trainer(trainer_id: hug.types.number,
                  name: hug.types.text=None,
                  gender: hug.types.one_of(['boy', 'girl', 'other'])=None,
                  rival_name: hug.types.text=None):

    try:
        trainer = Trainers.find_or_fail(trainer_id)
    except ModelNotFound:
        raise HTTPBadRequest('trainer_not_found', 'Error finding trainer with this ID')

    try:
        trainer.name = name
        trainer.gender = gender
        trainer.rival_name = rival_name
        trainer.save()
    except IntegrityError:
        raise HTTPBadRequest('error_creating_trainer', 'Error creating trainer')

    return Trainers.find(trainer.id).serialize()


@hug.get('/trainers/{trainer_id}')
def get_trainer(trainer_id: hug.types.number):

    try:
        trainer = Trainers.find_or_fail(trainer_id)
    except ModelNotFound:
        raise HTTPBadRequest('trainer_not_found', 'A trainer with this ID was not found')

    return trainer.serialize()

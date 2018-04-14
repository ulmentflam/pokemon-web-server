import hug
import environs
import logging
from pokemon.handlers import trainers, attacks, pokemon

log = logging.getLogger(__name__)


@hug.get('/')
def great_success():
    return "success"


@hug.extend_api()
def with_other_apis():
    return [trainers, attacks, pokemon]
#Pokemon Web Server Development Tutorial 

This is a quick and dirty overview of how to build a RESTful web server in python. This guide
includes how to run a web server locally with docker and docker-compose. It also includes an 
overview of a basic relational database and how to interact with that database via api.
I will also include some information about non relational datastores and the pros and cons of 
each interaction.


#Frameworks
 - Docker
 - Python
 - Hug
 - Orator Active Record ORM

#RUN
To run hug locally, run the following command:
``hug -f {file_name}``
Hug documentation can be found [here](http://www.hug.rest)

The documentation for setting up postgres locally depends on your file system.
Documentation on orator can be found [here](https://orator-orm.com)

The commands for creating an orator migration and running orator migrations is as follows:

``orator make:migration {table_name}_table``
``orator migrate -d local``

The command for running the docker environment is as follows:

``docker-compose build``
``docker-compose up``

If you want docker compose detached run:

``docker-compose up -d``

To run docker commands in the docker bash environment run:

``docker-compose exec app bash``

A good resource for installing docker can be found [here](https://docs.docker.com/install/)

A good resource for making http requests called postman can be found [here](https://www.getpostman.com)
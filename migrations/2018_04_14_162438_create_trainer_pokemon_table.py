from orator.migrations import Migration


class CreateTrainerPokemonTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.db.transaction():
            with self.schema.create('trainer_pokemon') as table:
                table.integer('trainer_id')
                table.foreign('trainer_id').references('id').on('trainers').on_delete('cascade')
                table.integer('pokemon_id')
                table.foreign('pokemon_id').references('id').on('pokemons').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        with self.db.transaction():
            self.schema.drop('trainer_pokemon')

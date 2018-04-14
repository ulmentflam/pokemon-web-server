from orator.migrations import Migration


class CreatePokemonsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.db.transaction():
            with self.schema.create('pokemons') as table:
                table.increments('id')
                table.string('name')
                table.float('hp')
                table.integer('level')
                table.enum('type', ['normal', 'grass', 'fire', 'watter','flying', 'electric', 'ground', 'dragon', 'psychic', 'ghost']).default('normal')
                table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.db.transaction():
            self.schema.drop('pokemons')
from orator.migrations import Migration


class CreateAttacksTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.db.transaction():
            with self.schema.create('attacks') as table:
                table.increments('id')
                table.string('name')
                table.float('hit_chance')
                table.float('damage')
                table.integer('pokemon_id')
                table.foreign('pokemon_id').references('id').on('pokemons').on_delete('cascade')
                table.enum('type', ['normal', 'grass', 'fire', 'watter','flying', 'electric', 'ground', 'dragon', 'psychic', 'ghost']).default('normal')
                table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.db.transaction():
            self.schema.drop('attacks')
from orator.migrations import Migration


class CreateTrainerTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.db.transaction():
            with self.schema.create('trainers') as table:
                table.increments('id')
                table.string('name')
                table.string('gender')
                table.string('rival_name')
                table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.db.transaction():
            self.schema.drop('trainers')


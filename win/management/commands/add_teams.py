from django.core.management.base import BaseCommand

from win.models import Team


class Command(BaseCommand):
    help = "Add teams"

    def handle(self, *args, **options):
        with open(f'{"/".join(__file__.split("/")[:-1])}/teams.txt', "r") as f:
            for line in f.read().split("\n"):
                try:
                    name, code = line.split(",")
                except ValueError:
                    continue
                Team.objects.create(name=name, code=code)
        self.stdout.write(self.style.SUCCESS("Added the teams to the DB"))

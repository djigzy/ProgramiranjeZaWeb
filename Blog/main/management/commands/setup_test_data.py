import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *

NUM_KORISNIK = 5
NUM_REPUTACIJA = 5
NUM_KOMENTAR = 50
NUM_BLOG = 10


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Korisnik,Reputacija,Komentar,Blog]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_KORISNIK):
            korisnik = KorisnikFactory()

        for _ in range(NUM_REPUTACIJA):
            reputacija = ReputacijaFactroy()
            
        for _ in range(NUM_KOMENTAR):
            komentar = KomentarFactory()

        for _ in range(NUM_BLOG):
            blog = BlogFactory()

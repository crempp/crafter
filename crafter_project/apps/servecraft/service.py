from django.db.models.signals import post_save
from django.dispatch import receiver
from crafter.models import Game

print("HERE")
@receiver(post_save, sender=Game)
def create_game(sender, **kwargs):
    created = kwargs['created']
    print sender
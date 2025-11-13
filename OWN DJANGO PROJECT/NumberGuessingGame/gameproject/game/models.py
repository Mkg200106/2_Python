from django.db import models

# Create your models here

class Score(models.Model):
    player_name = models.CharField(max_length=50)
    attempts = models.IntegerField()
    level = models.CharField(max_length=10)
    time_taken = models.FloatField(help_text="Seconds taken to guess correctly")
    date_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_name} - {self.level} ({self.attempts} tries, {self.time_taken:.1f}s)"

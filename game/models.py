from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField('نام بازی',max_length=50)
    positive_score = models.IntegerField('امتیاز برنده')
    negative_score = models.IntegerField("امتیاز بازنده")

def __str__(self):
    return self.name


class Player(models.Model):
    username = models.CharField(verbose_name='نام کاربری' , blank=True , max_length=100)
    sessionKey = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.username
    
class Score(models.Model):
    # game = models.ForeignKey(Game,on_delete=models.CASCADE)
    # winner = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='winner')
    # loser = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='loser')
    game = models.CharField("نام بازی" , max_length=50)
    winner = models.CharField("نام برنده" , max_length=50)
    loser = models.CharField("نام بازنده" , max_length=50)

    def __str__(self):
        return self.game + self.winner + self.loser 
    


from django.db import models
from django.utils import timezone

class City(models.Model):
    name = models.CharField(max_length=100)
    city_id = models.CharField(max_length=10)
    last_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name

class PrayerTime(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    imsak = models.TimeField()
    subuh = models.TimeField()
    terbit = models.TimeField()
    dhuha = models.TimeField()
    dzuhur = models.TimeField()
    ashar = models.TimeField()
    maghrib = models.TimeField()
    isya = models.TimeField()
    
    class Meta:
        unique_together = ['city', 'date']

    def __str__(self):
        return f"{self.city.name} - {self.date}"
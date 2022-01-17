
from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return \
            f'News: {self.title}' \
            f'Anons: {self.anons}'\
            f'Full text: {self.full_text}'\
            f'Date: {self.date}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

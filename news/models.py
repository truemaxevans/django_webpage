from django.db import models
# Creating tables for database


class Articles(models.Model):
    title = models.CharField('Article name', max_length=50)
    anons = models.CharField('Announcement', max_length=255)
    full_text = models.TextField('Article body')
    date = models.DateTimeField('Date')
# show articles on page

    def __str__(self):
        return self.title

# correct singular and plural name

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'







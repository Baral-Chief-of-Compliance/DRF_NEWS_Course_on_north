from django.db import models
from datetime import date
from django.urls import reverse


class News(models.Model):
    photo_preview_news = models.ImageField("Изображение заставки новости", upload_to='photo_preview_news/')
    title = models.CharField("Название новости", max_length=256)
    shortDescription = models.TextField("Краткое описание новости")
    datePublished = models.DateField("дата публикации новости", default=date.today)
    textNews = models.TextField("Содержимое новости")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news-details", kwargs={"id": self.id})
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

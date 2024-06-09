from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.name


class Sites(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='links',on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    url = models.URLField()
    descricao = models.TextField()

    def __str__(self):
        return self.name

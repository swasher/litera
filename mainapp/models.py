import os
from django.db import models
from django.conf import settings


# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        font_dir = os.path.join(settings.MEDIA_ROOT, self.name)
        if not os.path.exists(font_dir):
            # TODO self.name must be safe
            os.mkdir(font_dir)
        super(Family, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # see signals.py for dir remove function
        pass

    class Meta:
        verbose_name_plural = "Families"

    def __str__(self):
        return self.name


class Font(models.Model):
    fontFamily = models.ForeignKey(Family, on_delete=models.CASCADE, help_text="Семейство")

    fontSubfamily = models.CharField(max_length=150, help_text="Подсемейство")
    fullName = models.CharField(max_length=150, help_text="Полное название шрифта")

    designer = models.CharField(max_length=150, help_text="Дизайнер")
    designerURL = models.CharField(max_length=150, help_text="URL дизайнера")
    manufacturer = models.CharField(max_length=150, help_text="Изготовитель")
    manufacturerURL = models.CharField(max_length=150, help_text="URL поставщика")
    trademark = models.CharField(max_length=150, help_text="Торговая марка")
    licenseURL = models.CharField(max_length=150, help_text="URL лицензии")

    postScriptName = models.CharField(max_length=150, help_text="PostScript название")
    uniqueID = models.CharField(max_length=150, help_text="Идентификатор")
    version = models.CharField(max_length=150, help_text="Версия")
    copyright = models.CharField(max_length=150, help_text="Copyright")

    free = models.BooleanField( default=False)
    fontfile = models.FileField(upload_to='fonts/')

    def __str__(self):
        return self.fontFamily


# class FontFiles(models.Model):
#     font = models.ForeignKey(Font, on_delete=models.CASCADE)

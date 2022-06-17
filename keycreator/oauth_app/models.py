from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Category(models.Model):
    """ Категории ключей """
    name = models.CharField("Категория", max_length=50)
    description = models.TextField("Описание")
    
    def __str__(self):
        return self.name

class LeverKeyModel(models.Model):
    """ Сувальдные Ключи """
    name = models.CharField("Название", max_length=50)
    category = models.ForeignKey(
        Category,
        related_name="leverKeyModel",
        on_delete=models.SET_NULL,
        null=True)
    keyBitWidth = models.FloatField("Ширина бородки")
    keyStemDiametr = models.FloatField("Диаметр стержня")
    keyStemLenght = models.IntegerField("Длинна стержня")
    keyImage = models.ImageField("Изображение", upload_to='imagekey/')
    keyObject = models.FileField(upload_to='uploads', blank=True)
    
    def __str__(self):
        return self.name
    
class PinKeyModel(models.Model):
    """ Штифтовые ключи """
    name = models.CharField("Название", max_length=50)
    category = models.ForeignKey(
        Category,
        related_name="pinKeyModel",
        on_delete=models.SET_NULL,
        null=True)
    keyWidth = models.FloatField("Ширина заготовки")
    keyThickness = models.FloatField("Толщина заготовки")
    keyLenght = models.FloatField("Длинна заготовки")
    keyProfile = models.ImageField("Изображение", upload_to='imageprofile/')
    keyObject = models.FileField(upload_to='uploads', blank=True)
    
    def __str__(self):
        return self.name

class StandartSizeLeverKey(models.Model):
    """ Типоразмеры """
    nameSize = models.IntegerField("Типоразмер")
    leverKeyModel = models.ForeignKey(
        LeverKeyModel,
        related_name="leverKeyModel",
        on_delete=models.SET_NULL,
        null=True)
    standartSize = models.FloatField("Размер")
    
    def __str__(self):
        return self.name
    
class StandartSizePinKey(models.Model):
    """ Типоразмеры """
    nameSize = models.IntegerField("Типоразмер")
    pinKeyModel = models.ForeignKey(
        PinKeyModel,
        related_name="pinKeyModel",
        on_delete=models.SET_NULL,
        null=True)
    standartSize = models.FloatField("Размер")
    
    def __str__(self):
        return self.name
    
class ListKey(models.Model):
    """ Список созданых моделей """
    emailUser = models.EmailField(max_length=100)
    objectKey = models.JSONField()
    
    def __str__(self):
        return self.name
    
    
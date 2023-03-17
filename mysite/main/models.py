from django.db import models


#Основная таблица
class Car(models.Model):
    model_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    body = models.ForeignKey('Body', on_delete=models.CASCADE)
    drive = models.ForeignKey('Drive', on_delete=models.CASCADE)
    transmission = models.ForeignKey('Transmission', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    fuel = models.ForeignKey('FuelType', on_delete=models.CASCADE)
    wheel = models.ForeignKey('SteeringWheel', on_delete=models.CASCADE)
    dealership = models.ForeignKey('Address', on_delete=models.CASCADE)
    engine = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    owners = models.PositiveIntegerField(max_length=3)
    power = models.PositiveIntegerField()

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name_plural = 'Автомобили'


# Базовые таблицы
class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name_plural = 'Марки'


class Body(models.Model):
    body_name = models.CharField(max_length=55)

    def __str__(self):
        return self.body_name

    class Meta:
        verbose_name_plural = 'Кузовы'


class Drive(models.Model):
    drive_name = models.CharField(max_length=55)

    def __str__(self):
        return self.drive_name

    class Meta:
        verbose_name_plural = 'Приводы'


class Transmission(models.Model):
    transmission_name = models.CharField(max_length=60)

    def __str__(self):
        return self.transmission_name

    class Meta:
        verbose_name_plural = 'Трансмиссии'


class Color(models.Model):
    color_name = models.CharField(max_length=60)

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name_plural = 'Цвета'


class SteeringWheel(models.Model):
    wheel = models.CharField(max_length=50)

    def __str__(self):
        return self.wheel

    class Meta:
        verbose_name = 'Руль'

class FuelType(models.Model):
    fuel = models.CharField(max_length=50)

    def __str__(self):
        return self.fuel

    class Meta:
        verbose_name = 'Топливо'
        verbose_name_plural = 'Топливо'

class Address(models.Model):
    dealership = models.CharField(max_length=200)

    def __str__(self):
        return self.dealership

    class Meta:
        verbose_name = 'Диллерский центр'
        verbose_name_plural = 'Диллерские центры'




from django.db import models
import uuid
from django.db.models.constraints import UniqueConstraint
import datetime


class Reference(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(verbose_name='Идентификатор', db_index=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, verbose_name='Наименование')
    short_name = models.CharField(max_length=55, verbose_name='Короткое наименование')
    description = models.TextField(verbose_name='Описание')
    version = models.CharField(max_length=55, verbose_name='Версия')
    date = models.DateField(verbose_name='Дата начала действия', default=datetime.date.today)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('uuid', 'version'), name='id_ver'),
        ]
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'

    def __str__(self):
        return self.name + ' Версия:'  + self.version


class Element(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(Reference, on_delete=models.CASCADE)
    code = models.CharField(max_length=25, verbose_name='Код элемента', blank=False)
    value = models.CharField(max_length=255, verbose_name='Значение', blank=False)

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return self.code

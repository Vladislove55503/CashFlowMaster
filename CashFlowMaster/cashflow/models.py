from datetime import date

from django.db import models
from smart_selects.db_fields import ChainedForeignKey



class StatusAction(models.Model):
    name = models.CharField(
                max_length=100, verbose_name='Статус', unique=True,
                error_messages={
                    'unique': 'Статус с таким именем уже существует',
                    })

    class Meta:
        verbose_name = 'Статус транзакций'
        verbose_name_plural = 'Статусы транзакций'

    def __str__(self):
        return self.name


class TypeAction(models.Model):
    name = models.CharField(
                max_length=100, verbose_name='Тип', unique=True,
                error_messages={
                    'unique': 'Тип с таким именем уже существует',
                    })

    class Meta:
        verbose_name = 'Тип транзакций'
        verbose_name_plural = 'Типы транзакций'

    def __str__(self):
        return self.name


class CategoryAction(models.Model):
    name = models.CharField(
                max_length=100, verbose_name='Категория',
                error_messages={
                    'unique': 'Категория с таким именем уже существует',
                    })
    type_act = models.ForeignKey('TypeAction', 
                                 on_delete=models.CASCADE, 
                                 verbose_name='Тип',
                                 )

    class Meta:
        verbose_name = 'Категория транзакций'
        verbose_name_plural = 'Категории транзакций'

    def __str__(self):
        return self.name


class SubcategoryAction(models.Model):
    name = models.CharField(
                max_length=100, verbose_name='Подкатегория',
                error_messages={
                    'unique': 'Подкатегория с таким именем уже существует',
                    })
    category_act = models.ForeignKey('CategoryAction', 
                                     on_delete=models.CASCADE, 
                                     verbose_name='Категория',
                                     )

    class Meta:
        verbose_name = 'Подкатегория транзакций'
        verbose_name_plural = 'Подкатегории транзакций'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date_created = models.DateField(default=date.today,
                                    null=True,
                                    verbose_name='Дата создания записи',
                                    )
    status_act = models.ForeignKey('StatusAction',
                                   blank=True,
                                   null=True,
                                   on_delete=models.SET_NULL, 
                                   verbose_name='Статус',
                                   )
    type_act = models.ForeignKey('TypeAction', 
                                 null=True,
                                 on_delete=models.SET_NULL, 
                                 verbose_name='Тип',
                                 )
    category_act = ChainedForeignKey('CategoryAction',
                                     chained_field='type_act',
                                     chained_model_field='type_act',
                                     show_all=False,
                                     auto_choose=False,

                                     null=True,
                                     on_delete=models.SET_NULL, 
                                     verbose_name='Категория',
                                     )
    subcategory_act = ChainedForeignKey('SubcategoryAction',
                                        chained_field='category_act',
                                        chained_model_field='category_act',
                                        show_all=False,
                                        auto_choose=False,
                                        
                                        null=True,
                                        on_delete=models.SET_NULL, 
                                        verbose_name='Подкатегория',
                                        )
    amount = models.PositiveIntegerField(verbose_name='Сумма')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        
    def __str__(self):
        return (f'Запись от {self.date_created}, ' 
                f'статус - {self.status_act}, ' 
                f'сумма - {self.amount}')
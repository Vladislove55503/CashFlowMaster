# Generated by Django 4.2 on 2025-06-13 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0004_alter_categoryaction_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status_act',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashflow.statusaction', verbose_name='Статус'),
        ),
    ]

# Generated by Django 2.2 on 2019-04-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20190403_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Pres', 'Presentation'), ('Con', 'Conference'), ('Sem', 'Seminar')], max_length=4),
        ),
    ]

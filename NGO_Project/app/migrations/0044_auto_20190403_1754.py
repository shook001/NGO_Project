# Generated by Django 2.2 on 2019-04-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20190403_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Pres', 'Presentation'), ('Sem', 'Seminar'), ('Con', 'Conference')], max_length=4),
        ),
    ]

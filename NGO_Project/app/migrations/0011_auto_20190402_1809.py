# Generated by Django 2.1.7 on 2019-04-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190402_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Sem', 'Seminar'), ('Con', 'Conference'), ('Pres', 'Presentation')], max_length=4),
        ),
    ]

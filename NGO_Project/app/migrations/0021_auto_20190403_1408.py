# Generated by Django 2.2 on 2019-04-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20190402_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Pres', 'Presentation'), ('Sem', 'Seminar'), ('Con', 'Conference')], max_length=4),
        ),
    ]
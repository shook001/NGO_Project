# Generated by Django 2.2 on 2019-04-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190402_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Pres', 'Presentation'), ('Sem', 'Seminar'), ('Con', 'Conference')], max_length=4),
        ),
    ]
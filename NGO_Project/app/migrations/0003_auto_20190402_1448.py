# Generated by Django 2.2 on 2019-04-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190402_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Pres', 'Presentation'), ('Con', 'Conference'), ('Sem', 'Seminar')], max_length=4),
        ),
    ]

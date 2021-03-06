# Generated by Django 2.1.7 on 2019-04-02 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(blank=True, choices=[('U', 'User'), ('A', 'Admin')], max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Sem', 'Seminar'), ('Pres', 'Presentation'), ('Con', 'Conference')], max_length=4),
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('precio', models.FloatField(max_length=40)),
            ],
        ),
    ]

# Generated by Django 5.2.3 on 2025-06-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]

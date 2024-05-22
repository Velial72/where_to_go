# Generated by Django 5.0.6 on 2024-05-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('lng', models.FloatField(max_length=200)),
                ('lat', models.FloatField(max_length=200)),
            ],
        ),
    ]

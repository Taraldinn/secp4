# Generated by Django 3.2 on 2021-04-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='media/album/photo')),
                ('creation', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
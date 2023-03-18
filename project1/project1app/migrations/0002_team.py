# Generated by Django 4.1.6 on 2023-02-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]

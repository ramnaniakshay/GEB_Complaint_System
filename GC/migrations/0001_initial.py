# Generated by Django 3.2.5 on 2021-08-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('birthdate', models.CharField(max_length=20)),
                ('aadharno', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
    ]
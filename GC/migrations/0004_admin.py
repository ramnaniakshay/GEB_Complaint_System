# Generated by Django 3.2.5 on 2021-08-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GC', '0003_auto_20210811_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('exp', models.CharField(max_length=255)),
                ('quote', models.TextField()),
            ],
        ),
    ]

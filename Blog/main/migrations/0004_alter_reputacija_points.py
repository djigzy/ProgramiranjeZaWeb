# Generated by Django 4.1.4 on 2022-12-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_reputacija_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reputacija',
            name='points',
            field=models.IntegerField(),
        ),
    ]

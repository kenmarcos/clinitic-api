# Generated by Django 4.0.4 on 2022-04-13 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='cpf',
            field=models.CharField(default=12345678901, max_length=11),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-01 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_articul'),
    ]

    operations = [
        migrations.AddField(
            model_name='articul',
            name='unidad',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]

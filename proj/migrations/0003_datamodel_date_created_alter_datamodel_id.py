# Generated by Django 4.0.3 on 2022-04-17 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_alter_datamodel_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodel',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donateur',
            name='user',
        ),
        migrations.AddField(
            model_name='donateur',
            name='code',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Code_Patient',
        ),
    ]

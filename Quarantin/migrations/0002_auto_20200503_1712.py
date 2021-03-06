# Generated by Django 3.0.3 on 2020-05-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quarantin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='pseudo',
            new_name='nom',
        ),
        migrations.AddField(
            model_name='client',
            name='adresse',
            field=models.CharField(default='@yahoo.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(default='@yahoo.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='foyer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='tel',
            field=models.CharField(default='0000000000', max_length=10),
            preserve_default=False,
        ),
    ]

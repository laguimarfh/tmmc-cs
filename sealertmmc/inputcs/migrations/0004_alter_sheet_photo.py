# Generated by Django 4.1.2 on 2022-10-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputcs', '0003_alter_sheet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 2.2.2 on 2019-07-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('number', '0007_auto_20190715_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Email_Address',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]

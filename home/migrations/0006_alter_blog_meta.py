# Generated by Django 4.1.4 on 2023-10-30 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blog_thumbnail_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='meta',
            field=models.CharField(max_length=400),
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]

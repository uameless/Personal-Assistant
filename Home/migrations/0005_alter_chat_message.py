# Generated by Django 4.0.2 on 2022-03-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_chat_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.TextField(max_length=500000),
        ),
    ]

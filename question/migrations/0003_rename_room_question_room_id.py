# Generated by Django 4.0.4 on 2022-05-17 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_question_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='room',
            new_name='room_id',
        ),
    ]
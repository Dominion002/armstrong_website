# Generated by Django 4.2.5 on 2024-04-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armstrong', '0004_alter_feedback_timestamp_alter_history_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='result',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

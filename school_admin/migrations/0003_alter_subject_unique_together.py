# Generated by Django 4.1 on 2022-08-20 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_admin', '0002_subject'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subject',
            unique_together={('subject', 'teacher')},
        ),
    ]

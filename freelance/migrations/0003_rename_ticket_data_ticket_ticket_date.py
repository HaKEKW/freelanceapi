# Generated by Django 4.1.7 on 2023-03-29 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0002_remove_ticket_ordering_remove_ticket_service_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket_data',
            new_name='ticket_date',
        ),
    ]

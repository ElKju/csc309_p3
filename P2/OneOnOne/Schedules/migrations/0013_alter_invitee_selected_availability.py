# Generated by Django 5.0.3 on 2024-03-31 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Schedules", "0012_alter_invitee_selected_availability"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invitee",
            name="selected_availability",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"calendar": False},
                to="Schedules.availability",
            ),
        ),
    ]

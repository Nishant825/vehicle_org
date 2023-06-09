# Generated by Django 4.1.7 on 2023-04-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veh_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='percentage_operations_processed',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='percentage_ticketed_matches',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ticketed_matches_identified',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='wanted_matches_identified',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='suborganisation',
            name='percentage_operations_processed',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='suborganisation',
            name='percentage_ticketed_matches',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='suborganisation',
            name='ticketed_matches_identified',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='suborganisation',
            name='wanted_matches_identified',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='suborganisationdata',
            name='percentage_operations_processed',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='suborganisationdata',
            name='percentage_ticketed_matches',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='suborganisationdata',
            name='ticketed_matches_identified',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='suborganisationdata',
            name='wanted_matches_identified',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

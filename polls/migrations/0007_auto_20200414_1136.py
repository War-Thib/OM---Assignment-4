# Generated by Django 3.0.5 on 2020-04-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200412_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacie',
            name='pharmacie_ville',
            field=models.CharField(blank=True, default='Bruxelles', max_length=30, null=True),
        ),
    ]
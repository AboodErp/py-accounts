# Generated by Django 5.1.2 on 2024-11-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_journalvoucheraccount_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalvoucher',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

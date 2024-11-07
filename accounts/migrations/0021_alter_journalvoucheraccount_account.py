# Generated by Django 5.1.2 on 2024-11-04 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_journalvoucheraccount_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalvoucheraccount',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='journal_voucher_accounts_set', to='accounts.account'),
        ),
    ]
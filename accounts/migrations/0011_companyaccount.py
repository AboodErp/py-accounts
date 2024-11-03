# Generated by Django 5.1.2 on 2024-11-01 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_journalvoucher_transaction_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('SALES_ACCOUNT', 'Sales Account'), ('COST_OF_GOODS_SOLD', 'Cost of Goods Sold'), ('STORE_ACCOUNT', 'Store Account'), ('DISCOUNT_ALLOWED_ACCOUNT', 'Discount Allowed Account'), ('STOCK_ADJUSTMENT_ACCOUNT', 'Stock Adjustment Account'), ('ROUND_OFF_ACCOUNT', 'Round Off Account'), ('DISCOUNT_RECEIVED_ACCOUNT', 'Discount Received Account'), ('WRITE_OFF_ACCOUNT', 'Write Off Account'), ('EMPLOYEE_ADVANCE_ACCOUNT', 'Employee Advance Account'), ('DEFERRED_REVEUE_ACCOUNT', 'Deferred Revenue Account'), ('DEFERRED_EXPENSE_ACCOUNT', 'Deferred Expense Account'), ('STOCK_RECEIVED_BUT_NOT_BILLED', 'Stock Received But Not Billed'), ('EXPENSES_INCLUDED_IN_VALUATION', 'Expenses Included in Valuation'), ('VAT_ACCOUNT', 'VAT Account')], default='SALES_ACCOUNT', max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_accounts_set', to='accounts.account')),
            ],
            options={
                'verbose_name_plural': 'Company Accounts',
                'db_table': 'company_accounts',
            },
        ),
    ]
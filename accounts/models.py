from django.db import models
from django.utils import timezone


class AccountGroup(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "account_groups"


class SubAccount(models.Model):
    account_group = models.ForeignKey(
        AccountGroup, on_delete=models.PROTECT, related_name="sub_accounts_groups_set"
    )
    name = models.CharField(max_length=100)
    is_defined = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = "sub_accounts"


class Account(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ("ONE_TIME", "One Time"),
        ("PERIODIC", "Periodic"),
    ]

    sub_account = models.ForeignKey(
        SubAccount, on_delete=models.PROTECT, related_name="accounts_set"
    )
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=11, blank=True, null=True)
    is_default = models.BooleanField(default=False)
    payment_type = models.CharField(
        max_length=20, choices=PAYMENT_TYPE_CHOICES, blank=True, null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "accounts"


class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    create_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Currencies"
        db_table = "currencies"

    def __str__(self):
        return self.name


class JournalVoucher(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("SALES_INVOICE", "Sales Invoice"),
        ("RECEIPT", "Receipt"),
    ]

    user = models.ForeignKey(
        "auth.User", on_delete=models.PROTECT, related_name="created_by"
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, related_name="currency_used_set", null=True
    )
    date = models.DateTimeField()
    reference_number = models.CharField(max_length=100, default="NULL", blank=True)
    exchange_rate = models.FloatField()
    transaction_type = models.CharField(
        max_length=20, choices=TRANSACTION_TYPE_CHOICES, default="SALES_INVOICE"
    )
    transaction_id = models.BigIntegerField(blank=True, null=True)
    cheque_number = models.CharField(max_length=20, blank=True, null=True)
    control_number = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "journal_vouchers"


class JournalVoucherAccount(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("CR", "Credit"),
        ("DR", "Debit"),
    ]

    journal_voucher = models.ForeignKey(
        JournalVoucher, on_delete=models.PROTECT, related_name="accounts_set"
    )
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="account_used_set"
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, blank=True, null=True
    )
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICES)
    narration = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "journal_voucher_accounts"


class JournalVoucherAccountEntity(models.Model):
    id = models.BigAutoField(primary_key=True)
    journal_voucher_account = models.ForeignKey(
        JournalVoucherAccount, on_delete=models.PROTECT, related_name="entities_set", null=True
    )
    accountable_id = models.BigIntegerField()
    accountable_type_id = models.BigIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "journal_voucher_account_entities"
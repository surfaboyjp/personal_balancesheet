from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import get_user_model


ASSET_CATEGORIES = (
    ("L", "流動資産"),
    ("F", "固定資産"),
    ("D", "繰越資産"),
)

LIABILITY_CATEGORIES = (
    ("L", "流動負債"),
    ("F", "固定負債"),
)

INCOME_CATEGORIES = (
    ("M", "メイン収入"),
    ("S", "サブ収入"),
)

COST_CATEGORIES = (
    ("L", "流動支出"),
    ("F", "固定支出"),
)


User = get_user_model()


class Journal(models.Model):
    name = models.CharField("帳簿名", max_length=64)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return str(self.name)


class JournalRecord(models.Model):
    name = models.CharField("帳簿名", max_length=64)
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT)
    closed_at = models.DateField("決算日")
    data_json = models.TextField("帳簿データのJSON")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return str(self.name)


class Asset(models.Model):
    name = models.CharField("資産名", max_length=64)
    user = models.ManyToManyField(User)
    value = models.IntegerField("残額")
    category = models.CharField("カテゴリー", choices=ASSET_CATEGORIES, max_length=2)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)


class Liability(models.Model):
    name = models.CharField("負債名", max_length=64)
    user = models.ManyToManyField(User)
    value = models.IntegerField("残額")
    category = models.CharField("カテゴリー", choices=LIABILITY_CATEGORIES, max_length=2)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)


class Income(models.Model):
    name = models.CharField("収入名", max_length=64)
    user = models.ManyToManyField(User)
    value = models.IntegerField("残額")
    category = models.CharField("カテゴリー", choices=INCOME_CATEGORIES, max_length=2)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)


class Cost(models.Model):
    name = models.CharField("支出名", max_length=64)
    user = models.ManyToManyField(User)
    value = models.IntegerField("残額")
    category = models.CharField("カテゴリー", choices=COST_CATEGORIES, max_length=2)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

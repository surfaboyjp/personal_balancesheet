# Generated by Django 3.2 on 2021-06-18 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='帳簿名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Liability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='負債名')),
                ('value', models.IntegerField(verbose_name='残額')),
                ('category', models.CharField(choices=[('L', '流動負債'), ('F', '固定負債')], max_length=2, verbose_name='カテゴリー')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.journal')),
            ],
        ),
        migrations.CreateModel(
            name='JournalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='帳簿名')),
                ('closed_at', models.DateField(auto_now_add=True, verbose_name='決算日')),
                ('asset_sum', models.IntegerField(default=0, verbose_name='資産合計')),
                ('liquid_asset_sum', models.IntegerField(default=0, verbose_name='流動資産合計')),
                ('liquid_asset_list', models.TextField(default=0, verbose_name='流動資産リスト')),
                ('fixed_asset_sum', models.IntegerField(default=0, verbose_name='固定資産合計')),
                ('fixed_asset_list', models.TextField(default=0, verbose_name='固定資産リスト')),
                ('deferred_asset_sum', models.IntegerField(default=0, verbose_name='繰越資産合計')),
                ('deferred_asset_list', models.TextField(default=0, verbose_name='繰越資産リスト')),
                ('liability_sum', models.IntegerField(default=0, verbose_name='負債合計')),
                ('liquid_liability_sum', models.IntegerField(default=0, verbose_name='流動負債合計')),
                ('liquid_liability_list', models.TextField(default=0, verbose_name='流動負債リスト')),
                ('fixed_liability_sum', models.IntegerField(default=0, verbose_name='固定負債合計')),
                ('fixed_liability_list', models.TextField(default=0, verbose_name='固定負債リスト')),
                ('capital', models.IntegerField(default=0, verbose_name='総資産')),
                ('liability_capital_sum', models.IntegerField(default=0, verbose_name='負債・純資産合計')),
                ('income_sum', models.IntegerField(default=0, verbose_name='収入合計')),
                ('main_income_sum', models.IntegerField(default=0, verbose_name='メイン収入合計')),
                ('main_income_list', models.TextField(default=0, verbose_name='メイン収入リスト')),
                ('sub_income_sum', models.IntegerField(default=0, verbose_name='サブ収入合計')),
                ('sub_income_list', models.TextField(default=0, verbose_name='サブ収入リスト')),
                ('cost_sum', models.IntegerField(default=0, verbose_name='支出合計')),
                ('liquid_cost_sum', models.IntegerField(default=0, verbose_name='流動支出合計')),
                ('liquid_cost_list', models.TextField(default=0, verbose_name='流動支出リスト')),
                ('fixed_cost_sum', models.IntegerField(default=0, verbose_name='固定支出合計')),
                ('fixed_cost_list', models.TextField(default=0, verbose_name='固定支出リスト')),
                ('saving', models.IntegerField(default=0, verbose_name='繰越資産')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.journal')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='収入名')),
                ('value', models.IntegerField(verbose_name='残額')),
                ('category', models.CharField(choices=[('M', 'メイン収入'), ('S', 'サブ収入')], max_length=2, verbose_name='カテゴリー')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.journal')),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='支出名')),
                ('value', models.IntegerField(verbose_name='残額')),
                ('category', models.CharField(choices=[('L', '流動支出'), ('F', '固定支出')], max_length=2, verbose_name='カテゴリー')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.journal')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='資産名')),
                ('value', models.IntegerField(verbose_name='残額')),
                ('category', models.CharField(choices=[('L', '流動資産'), ('F', '固定資産'), ('D', '繰越資産')], max_length=2, verbose_name='カテゴリー')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.journal')),
            ],
        ),
    ]

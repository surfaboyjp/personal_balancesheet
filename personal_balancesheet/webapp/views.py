from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from .models import *
from django.views.generic.list import MultipleObjectMixin  # この行を追加
from django.contrib.auth.views import LoginView, LogoutView
import numpy
from .Form import *
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'webapp/index.html'

    def get_context_data(self, **kwargs):
        journal_list = Journal.objects.all().order_by('-created_at')
        params = {
            'journal_list': journal_list,
        }
        return params


class JournalDetailView(DetailView, MultipleObjectMixin):
    model = Journal
    template_name = 'webapp/journal_detail.html'

    def get_context_data(self, **kwargs):
        context = {
            'bs': self.get_bs_dict(),
            'pl': self.get_pl_dict(),
        }
        print(self.get_bs_dict()["fixed_asset_list"])
        return context

    def get_bs_dict(self):
        assets = list(Asset.objects.all().values())
        liabilities = list(Liability.objects.all().values())
        liquid_assets = [x for x in assets if x['category'] == 'L']
        la_sum = get_value_sum(liquid_assets)
        fixed_assets = [x for x in assets if x['category'] == 'F']
        fa_sum = get_value_sum(fixed_assets)
        deferred_assets = [x for x in assets if x['category'] == 'D']
        da_sum = get_value_sum(deferred_assets)

        liquid_liabilities = [y for y in liabilities if y['category'] == 'L']
        ll_sum = get_value_sum(liquid_liabilities)
        fixed_liabilities = [y for y in liabilities if y['category'] == 'F']
        fl_sum = get_value_sum(fixed_liabilities)

        asset_sum = la_sum + fa_sum + da_sum
        liability_sum = ll_sum + fl_sum
        capital = asset_sum - liability_sum
        liability_capital_sum = liability_sum + capital

        get_rate_in_list(liquid_assets, asset_sum)
        get_rate_in_list(fixed_assets, asset_sum)
        get_rate_in_list(deferred_assets, asset_sum)
        get_rate_in_list(liquid_liabilities, asset_sum)
        get_rate_in_list(fixed_liabilities, asset_sum)

        liquid_asset_rate = numpy.float64(la_sum) / asset_sum * 100
        fixed_asset_rate = numpy.float64(fa_sum) / asset_sum * 100
        deferred_asset_rate = numpy.float64(da_sum) / asset_sum * 100
        liquid_liability_rate = numpy.float64(ll_sum) / liability_sum * 100
        fixed_liability_rate = numpy.float64(fl_sum) / liability_sum * 100
        capital_rate = numpy.float64(capital) / liability_capital_sum * 100

        bs = {
            'asset': asset_sum,
            'liquid_assets': la_sum,
            'liquid_asset_rate': liquid_asset_rate,
            'liquid_asset_list': liquid_assets,
            'fixed_assets': fa_sum,
            'fixed_asset_rate': fixed_asset_rate,
            'fixed_asset_list': fixed_assets,
            'deferred_assets': da_sum,
            'deferred_asset_rate': deferred_asset_rate,
            'deferred_asset_list': deferred_assets,
            'liability': liability_sum,
            'liquid_liability': ll_sum,
            'liquid_liability_rate': liquid_liability_rate,
            'liquid_liability_list': liquid_liabilities,
            'fixed_liability': fl_sum,
            'fixed_liability_rate': fixed_liability_rate,
            'fixed_liability_list': fixed_liabilities,
            'capital': capital,
            'capital_rate': capital_rate,
            'liability_capital_sum': liability_capital_sum ,
        }
        return bs

    def get_pl_dict(self):
        incomes = list(Income.objects.all().values())
        costs = list(Cost.objects.all().values())
        main_incomes = [y for y in incomes if y['category'] == 'M']
        mi_sum = get_value_sum(main_incomes)
        sub_incomes = [y for y in incomes if y['category'] == 'S']
        si_sum = get_value_sum(sub_incomes)

        liquid_costs = [y for y in costs if y['category'] == 'L']
        lc_sum = get_value_sum(liquid_costs)
        fixed_costs = [y for y in costs if y['category'] == 'F']
        fc_sum = get_value_sum(fixed_costs)

        income_sum = mi_sum + si_sum
        cost_sum = lc_sum + fc_sum
        saving = income_sum - cost_sum
        pl = {
            'income': income_sum,
            'main_incomes': mi_sum,
            'main_income_list': main_incomes,
            'sub_incomes': si_sum,
            'sub_income_list': sub_incomes,
            'cost': cost_sum,
            'liquid_costs': lc_sum,
            'liquid_cost_list': liquid_costs,
            'fixed_costs': fc_sum,
            'fixed_cost_list': fixed_costs,
            'saving': saving
        }
        return pl


class RecordView(ListView):
    model = JournalRecord


class RecordDetailView(DetailView):
    model = JournalRecord


# class FstatementView(DetailView):
#     model = Fstatement

class CreateUserView(CreateView):
    form_class = SignUpForm
    template_name = 'webapp/signup.html'
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        messages.info(self.request, 'ユーザー登録をしました。')
        return HttpResponseRedirect(self.get_success_url())


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'webapp/login.html'


def get_value_sum(dict_list):
    result = 0
    for dict in dict_list:
        result += dict['value']
    return result


def get_rate_in_list(dict_list, sum_person):
    for item in dict_list:
        item_rate = numpy.float64(item['value']) / sum_person * 100
        item['rate'] = item_rate
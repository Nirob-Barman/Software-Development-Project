from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID, TRANSFER, RECEIVED
from datetime import datetime
from django.db.models import Sum
from transactions.forms import (
    DepositForm,
    WithdrawForm,
    LoanRequestForm,
    TransferMoneyForm
)
from transactions.models import Transaction
from accounts.models import UserBankAccount


from core.models import BankSettings

# Create your views here.


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        # passing title to template
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'


    def get_initial(self):
        # bank_settings = BankSettings.objects.get()
        # is_bankrupt = bank_settings.is_bankrupt
        # print(f"Bank is bankrupt: {is_bankrupt}")

        # Get the BankSettings object with is_bankrupt=True
        bank_settings = BankSettings.objects.filter(is_bankrupt=True).first()


        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        # bank_settings = BankSettings.objects.filter(is_bankrupt=True).first()
        # Get the BankSettings object with is_bankrupt=True
        bank_settings = BankSettings.objects.filter(is_bankrupt=True).first()

        if bank_settings and bank_settings.is_bankrupt:
            print("Bank is bankrupt")
            messages.error(
                self.request,
                'Withdrawal is not allowed. The bank is bankrupt.'
            )
            return redirect(reverse_lazy('withdraw_money'))

        amount = form.cleaned_data.get('amount')

        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )

        return super().form_valid(form)


class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'

    def get_initial(self):
        initial = {'transaction_type': LOAN}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(
            account=self.request.user.account, transaction_type=3, loan_approve=True).count()

        if current_loan_count >= 3:
            return HttpResponse("You have cross the loan limits")

        messages.success(
            self.request,
            f'Loan request for {"{:,.2f}".format(float(amount))}$ submitted successfully'
        )

        return super().form_valid(form)


class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            queryset = queryset.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        # must return unique queryset
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context


class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        print(loan)
        if loan.loan_approve:
            user_account = loan.account
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.loan_approved = True
                loan.transaction_type = LOAN_PAID
                loan.save()
                # return redirect('transactions:loan_list')
                return redirect('loan_list')
            else:
                messages.error(
                    self.request,
                    f'Loan amount is greater than available balance'
                )

        return redirect('loan_list')


class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans'

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(
            account=user_account, transaction_type=3)
        print(queryset)
        return queryset


class TransferMoneyView(View):
    template_name = 'transactions/transfer_money.html'

    def get(self, request):
        form = TransferMoneyForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TransferMoneyForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            to_user_id = form.cleaned_data['to_user_id']
            
            current_user = request.user.account
            # print("Current User Balance Before Transfer:", current_user.balance)

            try:
                to_user = UserBankAccount.objects.get(
                    account_number=to_user_id)
                print(to_user)
                min_balance_to_transfer = 100
                max_balance_to_transfer = 20000

                
                # if amount < min_balance_to_transfer:
                #     messages.error(
                #         request,
                #         f'You need to transfer at least {min_balance_to_transfer} $'
                #     )
                #     return render(request, self.template_name, {'form': form, 'title': 'Transfer Money'})

                # if amount > max_balance_to_transfer and amount <= current_user.balance:
                #     messages.error(
                #         request,
                #         f'You can transfer at most {max_balance_to_transfer} $'
                #     )
                #     return render(request, self.template_name, {'form': form, 'title': 'Transfer Money'})
                
                # if amount > current_user.balance:
                #     messages.error(
                #         request,
                #         f'You have {current_user.balance} $ in your account. '
                #         'You can not transfer more than your account balance'
                #     )
                #     return render(request, self.template_name, {'form': form, 'title': 'Transfer Money'})
                
                # Deduct the amount from current user's balance
                current_user.balance -= amount
                current_user.save()

                transaction_from = Transaction.objects.create(
                    account=current_user,
                    amount=amount,
                    balance_after_transaction=current_user.balance,
                    transaction_type=TRANSFER,  # Set the correct value
                    # loan_approve=False  # Set the correct value
                )
                transaction_to = Transaction.objects.create(
                    account=to_user,
                    amount=amount,
                    balance_after_transaction=to_user.balance,
                    transaction_type=RECEIVED,  # Set the correct value
                    # loan_approve=False  # Set the correct value
                )

                # print(
                #     f"Balance After Transaction: {transaction.balance_after_transaction}")


                to_user.balance += amount
                to_user.save()

                messages.success(
                    request,
                    f'Transfer of {"{:,.2f}".format(float(amount))}$ successful'
                )

            except UserBankAccount.DoesNotExist:
                messages.error(
                    request, 'User account not found. Please check the account number.')

            return render(request, 'transactions/transfer_money.html', {'form': form, 'title': 'Transfer Money'})
        return render(request, self.template_name, {'form': form, 'title': 'Transfer Money'})

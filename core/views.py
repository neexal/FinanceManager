from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, Saving, FuturePlan
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm,LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # replace 'home' with your desired URL or view
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# @login_required
def home(request):
    user = request.user
    incomes = Income.objects.filter(user=user)
    expenses = Expense.objects.filter(user=user)
    savings = Saving.objects.filter(user=user)
    future_plans = FuturePlan.objects.filter(user=user)

    if request.method == 'POST':
        # Check if the user clicked the delete button for an income, expense, or future plan entry
        delete_id = request.POST.get('delete_id')
        delete_type = request.POST.get('delete_type')
        messages= ""

        if delete_id and delete_type:
            try:
                if delete_type == 'income':
                    income = Income.objects.get(pk=delete_id, user=user)
                    income.delete()
                    messages.success(request, 'Income entry deleted successfully.')
                elif delete_type == 'expense':
                    expense = Expense.objects.get(pk=delete_id, user=user)
                    expense.delete()
                    messages.success(request, 'Expense entry deleted successfully.')
                elif delete_type == 'future_plan':
                    future_plan = FuturePlan.objects.get(pk=delete_id, user=user)
                    future_plan.delete()
                    messages.success(request, 'Future plan entry deleted successfully.')
            except:
                messages.error(request, 'An error occurred while deleting the entry. Please try again later.')

        # Check if the user clicked the mark as completed button for a future plan entry
        complete_id = request.POST.get('complete_id')
        if complete_id:
            try:
                future_plan = FuturePlan.objects.get(pk=complete_id, user=user)
                expense = Expense(user=user, amount=future_plan.estimated_cost, description=future_plan.description, category='Future Plan')
                expense.save()
                future_plan.delete()
                messages.success(request, 'Future plan completed successfully and added as an expense.')
            except:
                messages.error(request, 'An error occurred while completing the future plan. Please try again later.')

    context = {
        'incomes': incomes,
        'expenses': expenses,
        'savings': savings,
        'future_plans': future_plans,
    }
    return render(request, 'home.html', context)

# @login_required
def add_income(request):
    income = request.POST.get('income')
    user = request.user
    try:
        income = Income(user=user, amount=income)
        income.save()
        # messages.success(request, 'Income entry added successfully.')
        return redirect('home')
    except:
        # messages.error(request, 'An error occurred while adding the entry. Please try again later.')
        return redirect('home')
    return render(request, 'add_income.html')

# @login_required
def add_expense(request):
    # Add code here to allow the user to add a new expense entry
    return render(request, 'add_expense.html')

# @login_required
def add_saving(request):
    # Add code here to allow the user to add a new saving goal
    return render(request, 'add_saving.html')

# @login_required
def add_future_plan(request):
    # Add code here to allow the user to add a new future plan
    return render(request, 'add_future_plan.html')

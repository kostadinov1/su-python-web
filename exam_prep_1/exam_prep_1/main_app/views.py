from django.shortcuts import render, redirect
from exam_prep_1.main_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateExpenseForm, \
    EditExpenseForm, DeleteExpenseForm
from exam_prep_1.main_app.models import Profile, Expenses


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    expenses = Expenses.objects.all()

    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'budget_left': budget_left,
        'expenses': expenses,

    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form
    }

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expenses.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,
        'pk': pk,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expenses.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
        'pk': pk
    }

    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    expenses = Expenses.objects.all()
    expenses_count = len(expenses)

    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'budget_left': budget_left,
        'expenses_count': expenses_count,
        'expenses': expenses,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'profile-delete.html', context)

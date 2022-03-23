from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, Record
from .forms import HabitForm, RecordForm
from django.contrib.auth.decorators import login_required, user_passes_test


def base_login(request):
    if request.user.is_authenticated:
        return redirect("homepage")

    return render(request, "base.html")


@login_required(login_url="auth_login")
def homepage(
    request,
):
    habits = Habit.objects.all()
    records = Record.objects.all()
    return render(request, "homepage.html", {"habits": habits, "records": records})


@login_required
def habit_detail(request, slug):
    habit = get_object_or_404(Habit, slug=slug)
    records = Record.objects.all().filter(habit_id=habit.id)
    return render(request, "habit_detail.html", {"habit": habit, "records": records})


@login_required
def add_habit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user_id = user.id
            habit.save()
            return redirect(to="homepage")

    return render(request, "add_habit.html", {"form": form, "user": user})


@login_required
def add_record(request, slug):
    habit = get_object_or_404(Habit, slug=slug)
    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit_id = habit.id
            record.save()
            return redirect(to="habit_detail")

    return render(request, "add_record.html", {"form": form, "habit": habit})

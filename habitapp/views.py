from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, Record

# from .forms import DeckForm, FlashCardForm
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

    return render(request, "habit_detail.html", {"habit": habit})

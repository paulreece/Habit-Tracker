from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, Record

# from .forms import DeckForm, FlashCardForm
from django.contrib.auth.decorators import login_required, user_passes_test


def homepage(request):
    if request.user.is_authenticated:
        return redirect("habit_list")

    return render(request, "base.html")


@login_required(login_url="auth_login")
def deck_list(
    request,
):
    habits = Habit.objects.all()
    records = Record.objects.all()
    return render(request, "habit_list.html", {"habits": habits, "recods": records})

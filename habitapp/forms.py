from django import forms
from .models import User, Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ["name", "description", "goal"]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["goal_number"]

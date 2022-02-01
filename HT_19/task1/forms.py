from django import forms

class CategoryDropdown(forms.Form):
    category = (('newstories', 'newstories'),('jobstories', 'jobstories'),('askstories', 'askstories'),('showstories', 'showstories'),)
    blank_choice = (('', '-------------------'),)
    choices_category = forms.ChoiceField(choices= blank_choice + category)
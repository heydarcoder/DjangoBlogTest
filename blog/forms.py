from random import choices

from django import forms

from blog.models import Comment


class TikcetForm(forms.Form):
    SUBJECT_CHOICES = (
    ("پیشنهاد","پیشنهاد"),
    ("انتقاد","انتقاد"),
    ("گزارش", "گزارش")
    )
    massage = forms.CharField(widget=forms.Textarea , required=True , label="پیام")
    email = forms.EmailField(max_length=250 , required=True , label="ایمیل")
    phone = forms.CharField(max_length=11 , required=True , label="تلفن")
    name = forms.CharField(max_length=250 , required=True , label="نام")
    subject = forms.ChoiceField(choices = SUBJECT_CHOICES , label="موضوع")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name" , 'massage' , "email"]

class SearchForm(forms.Form):
    query = forms.CharField(required=False)
"""
Definition of forms.
"""
from django.db import models
from .models import Comment
from .models import Blog

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class CommentForm(forms.ModelForm):
    class Meta:
        model =  Comment
        fields = ('text',)
        labels = {'text':"Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'title', 'description', 'content', 'image',}
        labels = {'title': "Заголовок",'description':"Краткое содержание", 'content':"Полное содержание", 'image':"Картинка"}

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

   
class PoolForm(forms.Form):
   
   name = forms.CharField(label='Тема отзыва', min_length=2, max_length=100)

   '''список'''
   internet = forms.ChoiceField(label='Как давно вы пользуетесь нашим сайтом?',
                                choices=(('1','Меньше месяца'),
                                         ('2','Месяц и больше'),
                                         ('3','Пол года и больше'),
                                         ('4', 'Год и больше')), initial=1)
   '''блок ввода'''
   
   job =  forms.CharField(label='Положительные моменты', widget=forms.Textarea(attrs={'rows':6, 'cols':400}))
  
   message = forms.CharField(label='Отрицательные моменты', widget=forms.Textarea(attrs={'rows':6, 'cols':400}))
   
   predlogenie = forms.CharField(label='Предложения по развитию сайта', widget=forms.Textarea(attrs={'rows':6, 'cols':400})) 
   '''радиокнопка '''
   gender = forms.ChoiceField(label='Вы бы предложили наш сайт своим знакомым?',
                   choices=[('1','Да'),('2','нет')],
                   widget=forms.RadioSelect, initial=1)
   '''флажок '''
   notice = forms.BooleanField(label='Хотите получить дубликат ответа на почту?', required=False)
   
   email = forms.EmailField(label='Ваша почта', min_length=7,required=False )
  
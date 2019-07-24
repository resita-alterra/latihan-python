from django import forms
from .models import Mentor, Mentee, Blog

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('nama', 'exp','quote','nama_file_image')

class MenteeForm(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = ('nama', 'quote','nama_file_image')
    
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'tanggal_dipost','komen','isi','nama_file_image')



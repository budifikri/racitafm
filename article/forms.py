from django import forms
from .models import Article,Song,Medsos
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["nomer","judul","penyanyi"]



class MedsosForm(forms.ModelForm):
    class Meta:
        model = Medsos
        fields = ["nomer","name","link"]   

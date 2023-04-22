from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 200,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Tambahkan Foto ke Artikel")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

class Song(models.Model):
    penyanyi = models.CharField(max_length = 100,verbose_name = "Penyanyi")
    judul = models.CharField(max_length = 100,verbose_name = "Judul")
    tipe = models.CharField(max_length = 100,verbose_name = "Tipe")    
    tglupdate = models.DateTimeField(auto_now_add=True,verbose_name="Tgl Update")
    nomer = models.IntegerField(verbose_name="Nomer")
    def __str__(self):
        return self.judul

    class Meta: 
        ordering = ['nomer']


class Medsos(models.Model):
    name = models.CharField(max_length = 50,verbose_name = "Nama")
    link = models.CharField(max_length = 200,verbose_name = "Link")
    nomer = models.IntegerField(verbose_name="Nomer")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['nomer']

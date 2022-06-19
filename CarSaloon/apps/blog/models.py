from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200,verbose_name='Title of our Article')
    description=models.TextField(verbose_name='Text of our Article')
    is_active=models.BooleanField(default=False,verbose_name='active/unactive')
    main_img=models.ImageField(upload_to='images/blogimg',verbose_name='Final picture') #our file name main_img
    #if instead of  ImageField use fileField we should manage but imagefield doesnt need it . cuz filefiled is any files , text or etc  files !
    #if imageUpload.content_type=="image/jpeg" or imageUpload.content_type=="image/png":
    
    def __str__(self) :
        return self.title+"\n"+self.description+"\n"+self.is_active
 
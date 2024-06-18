from django.db import models
from django.core.exceptions import ValidationError


class LogoModel(models.Model):
    logo = models.ImageField(upload_to='website/logo')

    def save(self, *args, **kwargs):
        if not self.pk and LogoModel.objects.exists():
            raise ValidationError('There is already an instance of LogoModel.')
        return super(LogoModel, self).save(*args, **kwargs)
    
class ContactUsModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField()
    phone_number = models.CharField(max_length=255,null=True,blank=True)

    subject = models.CharField(max_length=255)
    description = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.email} , {self.first_name},{self.last_name}'




# class AboutUsModel(models.Model):
#     title_brief_description = models.CharField(max_length=255)
#     brief_description = models.TextField()
#     title_description = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return 'about page model'
    
#     def save(self, *args, **kwargs):
#         if not self.pk and LogoModel.objects.exists():
#             raise ValidationError('There is already an instance of LogoModel.')
#         return super(LogoModel, self).save(*args, **kwargs)




# class ProductImages(models.Model):
#     product = models.ForeignKey(AboutUsModel,on_delete=models.CASCADE,related_name='images')
#     file = models.ImageField(upload_to='website/aboutus//')

#     datetime_created = models.DateTimeField(auto_now_add=True)
#     datetime_update = models.DateTimeField(auto_now=True)

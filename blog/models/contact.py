from django.db import models

class ContactModel(models.Model):

    email = models.EmailField(max_length=250, blank= False)
    name_surname = models.CharField(max_length= 150)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact'
        verbose_name = ('iletişim')
        verbose_name_plural = ('iletişim')

    def __str__(self):
        return self.email
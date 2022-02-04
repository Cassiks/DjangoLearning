from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from blog.abstract_models import DateAbstractModel

class WritingModel(DateAbstractModel):
    image = models.ImageField(upload_to= 'writing_images')
    title = models.CharField(max_length=30)
    contents = models.TextField()
    slug = AutoSlugField(populate_from ='title', unique=True)
    categorys = models.ManyToManyField(CategoryModel, related_name='writing')
    writer = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='writings')

    class Meta:
        verbose_name = 'Yazı'
        verbose_name_plural = 'Yazı'
        db_table = "writings"

    def __str__(self):
        return self.title
from django.db import models
from blog.models import WritingModel
from blog.abstract_models import DateAbstractModel

class CommentModel(DateAbstractModel):

    writer = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name="comment")
    writing = models.ForeignKey(WritingModel, on_delete=models.CASCADE, related_name = "comments")
    comment = models.TextField()

    class Meta:
        db_table = 'comment'
        verbose_name = ('Yorum')
        verbose_name_plural = ('Yorum')

    def __str__(self):
        return self.writer.username


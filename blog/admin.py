from django.contrib import admin
from blog.models import CategoryModel , WritingModel , CommentModel, ContactModel

admin.site.register(CategoryModel)

@admin.register(WritingModel)
class WritingAdmin(admin.ModelAdmin):
    search_fields = ('title', 'contents')
    list_display = (
        'title', 'creation_date', 'arrangement_date'
    )

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', 'creation_date', 'arrangement_date')
    search_fields = ('writer_username',)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'creation_date')
    search_fields = ('email',)


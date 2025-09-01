from django.contrib import admin

from blog.models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title' ,'author' , 'publish' , 'created' , 'status']
    ordering = ('author' , 'publish')
    list_filter =['author' , 'status']
    search_fields = ['discription' , 'title']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {"slug" : ['title']}
    list_editable = ['status' ,]
    list_display_links =['title' , 'author' , 'publish']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["name" , "subject" , "email"]

    class Meta:

        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"
    def __str__(self):
        return self.subject
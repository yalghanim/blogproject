from django.contrib import admin

from .models import Post
		
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	search_fields = ['title', 'content']
	list_filter = ["timestamp"]
	list_display_links = ["timestamp"]
	class Meta: #meta creates associations, django module
		model = Post


			



admin.site.register(Post, PostModelAdmin)


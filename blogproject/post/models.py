from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
# from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Post(models.Model):
	author = models.ForeignKey(User, default=1)
	title = models.CharField(max_length=140)
	content = models.TextField()
	image = models.ImageField(upload_to="blog_images", null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	def absurl(self):
		return reverse("posts:id", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug)
	exists = qs.exists()
	if exists: #this will make it loop until we create a unique ID
		new_slug = "%s-%s" % (slug, instance.id)
		return create_slug(instance, new_slug=new_slug) 
	return slug

# def post_receiver(sender,instance, *args, **kwargs):
# 	if not instance.slug:
# 		slug=slugify(instance.title)
# 		qs = Post.objects.filter(slug=slug).order_by("-id")
# 		exists = qs.exists()
# 		if exists:
# 			slug = "%s-%s"%(slug, instance.id)
# 		instance.slug = slug
# 		instance.save()
#this is if I want to trigger post save


#look up the parameters
def post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance) # we did this in case post titles have the same title


pre_save.connect(post_receiver, sender=Post)





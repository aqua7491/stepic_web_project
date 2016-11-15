from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
class QuestionManager(models.Manager):                        
    def new(self):                                                              
        return self.order_by('-added_at')                                                                
    def populr(self):                                                          
        return self.order_by('-rating')

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name='question_author')
	likes = models.ManyToManyField(User, related_name='likes_set', blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('question', kwargs={'id': self.id})

#	class Meta:
#	    ordering = ('-added_at',)

#-----------------------------------------------------
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
	
	def __str__(self):
		return self.text
#	class Meta:
#       ordering = ('added_at',)

#------------------------------------------------------

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10

	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404

	paginator = Paginator(qs, limit)

	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page, paginator

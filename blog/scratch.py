from blog.models import Blog, BlogForm 
from django import forms
from django.shortcuts import *
blog = get_object_or_404(Blog, pk=3)                                                                                                             
form = BlogForm(instance=blog)
print form



Tasks
=====

Get 'new' save working
fix layout of buttons
	1) Right aligned
	2) Same vertical align
Deploy app and test
Load data (for Graham)
?Load other data
?Post to github


Write email
	List some outstanding problems
	List next issues I would have tackled
Email Ben with link and zip


?Pagining




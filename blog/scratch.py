from blog.models import Blog, BlogForm 
from django import forms
from django.shortcuts import *
blog = get_object_or_404(Blog, pk=3)                                                                                                             
form = BlogForm(instance=blog)
print form



submit - Save
Cancel
New
Publish
Delete

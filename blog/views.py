from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from blog.models import Post
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-date_published').all()
    return render(request, 'blog/index.html', {"posts": posts})

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("index-blog")
    template_name = "registration/signup.html"

class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("index-blog")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

class ListPost(ListView):
    paginate_by = 2
    model = Post
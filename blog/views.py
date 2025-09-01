from django.shortcuts import render , redirect
from django.http import HttpResponse , Http404
from django.views.generic import DetailView , ListView
from blog.forms import *

from blog.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.view.generic import

from .forms import TikcetForm


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def post_list(request):
#     posts = Post.published.all()
#     paginator =  Paginator(posts, 2)
#     page_number = request.GET.get('page', 1)
#
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#
#     context = {"posts":posts}
#     return render(request , "blog/list.html" ,context )
#
class PostListView(ListView):
    queryset = Post.published.all()
    paginate_by = 2
    template_name = "blog/list.html"

# def post_detail(request , id):
#     try:
#         post = Post.published.get(id=id)
#     except :
#         raise ("post not found")
#     context = {
#         "post": post,
#     }
#     return render(request , "blog/detail.html" ,context)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"

def TicketView(request):
    if request.method == "POST":
        form =TikcetForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create()
            cd = form.cleaned_data
            ticket_obj.massage = cd["massage"]
            ticket_obj.email = cd["email"]
            ticket_obj.name = cd["name"]
            ticket_obj.phone = cd["phone"]
            ticket_obj.subject = cd["subject"]
            ticket_obj.save()
            return redirect("blog:post-list")
    else :
        form = TikcetForm()
    return render(request , "forms/ticket.html" , {"form":form})
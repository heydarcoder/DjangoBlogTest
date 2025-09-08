from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse , Http404
from django.views.generic import DetailView , ListView
from blog.forms import *
from django.views.decorators.http import require_POST
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
    context_object_name = "posts"

def post_detail(request , pk):

    post = Post.published.get(id=pk)
    form = CommentForm()
    comment = post.comments.filter(active=True)
    context = {
        "post": post,
        "form": form,
        "comment": comment,
    }
    return render(request , "blog/detail.html" ,context)

# class PostDetailView(DetailView):
#     model = Post
#     template_name = "blog/detail.html"
#     context_object_name = "post"
#
def TicketView(request):
    if request.method == "POST":
        form =TikcetForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Ticket.objects.create(massage=cd['massage'] , email=cd['email'] , phone=cd['phone'] , subject=cd['subject'])
            # ticket_obj.massage = cd["massage"]
            # ticket_obj.email = cd["email"]
            # ticket_obj.name = cd["name"]
            # ticket_obj.phone = cd["phone"]
            # ticket_obj.subject = cd["subject"]
            # ticket_obj.save()
            return redirect("blog:post-list")
    else :
        form = TikcetForm()
    return render(request , "forms/ticket.html" , {"form":form})


@require_POST
def commentviwe(request , id):
    post = get_object_or_404(Post, id=id , status = Post.published.all())
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request , "forms/comment.html" , {"post" : post , "form":form, "comment":comment})

# def search(request):
#     query = None
#     result =None
#     if "query" in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             result = Post.published.filter(description__icontains=query)
#
#     context = {
#         "query": query ,
#         "result" : result ,
#     }
#     return render(request , "blog/searchform.html" , context)
# views.py
def search(request):
    print("ویو search اجرا شد")
    print(f"اطلاعات GET: {request.GET}")

    query = None
    results = None

    if "query" in request.GET:
        print("query در request.GET وجود دارد")
        form = SearchForm(request.GET)
        print(f"فرم ساخته شد: {form}")
        if form.is_valid():
            print("فرم معتبر است")
            query = form.cleaned_data['query']
            results = Post.published.filter(discription__icontains=query)
            print(f"نتایج یافت شده: {results.count()} مورد")
        else:
            print("فرم نامعتبر است")
            print(f"خطاهای فرم: {form.errors}")
    else:
        print("query در request.GET وجود ندارد")

    context = {
        "query": query,
        "results": results,
    }
    return render(request, "blog/searchform.html", context)
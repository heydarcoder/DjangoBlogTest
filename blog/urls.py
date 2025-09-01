from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # URL For index page

    # URL For Post-Detail
    # path('post-list/', views.post_list, name='post_list'),
    path('post-list/', views.PostListView.as_view(), name='post_list'),

    # URL For Post-Detail
    path('post-detail/<pk>', views.PostDetailView.as_view(), name="post_detail"),
    path("ticket/" , views.TicketView , name="ticket")
]


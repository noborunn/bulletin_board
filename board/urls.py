from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.RoomListView.as_view(), name='index'),
    path('thread-board/<int:pk>/', views.MessageListView.as_view(), name="thread_board"),
    path('thread-create/', views.thread_create, name='thread_create'),
    #path('my-thred/', views.MylistView.as_view(), name="my_thred")
    path('my-thread/', views.my_list, name="my_thread"),
    path('search-thread/', views.SearchView.as_view(), name="search_thread")
]
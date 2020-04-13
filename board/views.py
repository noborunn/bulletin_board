from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Q

# from .forms import MessageCreateForm
from .models import Room, Message


# Create your views here.

#多分使わなくなったview
#class IndexView(generic.TemplateView):
 #   template_name = "index.html"


class RoomListView(generic.ListView):
    model = Room
    template_name = 'index.html'

    def get_queryset(self):
        rooms = Room.objects.order_by('-created_at')
        return rooms


class MessageListView(generic.ListView):
    model = Message
    template_name = 'thread.html'

    def get_context_data(self):
        pk = self.kwargs['pk']
        room = Room.objects.get(id=pk)
        message_list = Message.objects.filter(room_id=pk).order_by('created_at')
        context = {'room': room, 'message_list': message_list}
        return context

    #def get_queryset(self):
     #   pk = self.kwargs['pk']
      #  messages = Message.objects.filter(room_id=pk)
        #追加
       # rooms = Room.objects.get(id=pk)
        #return messages

    @method_decorator(login_required)
    # @login_required
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        room = Room.objects.get(id=pk)
        if request.method == 'POST':
            sent_content = request.POST.get('content')

            if len(sent_content) == 0 or ' ' in sent_content or '　' in sent_content:
                return redirect('./')

            message = Message(
                room_id=pk,
                user=self.request.user,
                content=sent_content,
                # user_id = self.request.user(pk)
            )
            message.save()
        context = {
            'message_list': Message.objects.filter(room_id=pk).order_by('created_at'),
            'room': room
        }
        return render(request, 'thread.html', context)


def thread_create(request):
    if request.method == 'POST':
        sent_title = request.POST.get('title')

        if len(sent_title) == 0 or ' ' in sent_title or '　' in sent_title:
            return redirect('./')
        room = Room(
            title=sent_title
        )
        room.save()

        return redirect('/thread-board/' + str(room.pk))
    return render(request, 'thread_create.html')


# class MylistView(LoginRequiredMixin, generic.ListView):
#   model = Room
#  template_name = 'my_thred.html'

# def get_queryset(self):
#    messages = Message.objects.filter(user=self.request.user)
# messagesのroom_idを獲得してそれをRoomのpkに置き換える

#   for message in messages:
#      number = message.room_id
#     rooms = Room.objects.get(pk=number)

# return rooms

def my_list(request):
    messages = Message.objects.filter(user=request.user).order_by('-created_at')
    rooms = []

    # messagesのroom_idを獲得してそれをRoomのpkに置き換える
    for message in messages:
        number = message.room_id
        room = Room.objects.get(pk=number)

        if not room in rooms:
            rooms.append(room)

    data = {'rooms': rooms}

    return render(request, 'my_thread.html', data)


class SearchView(generic.ListView):
    model = Room
    template_name = 'search_thread.html'

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            room_list = Room.objects.filter(
                Q(title__icontains=q_word)).order_by('-created_at')
        else:
            room_list = []

        return room_list

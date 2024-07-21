from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class ChatPage(View):
    def get(self, request):
        return render(request, "chat/chat_page.html")

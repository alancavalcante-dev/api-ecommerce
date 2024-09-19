from django.shortcuts import render
from django.views import View


class LogsView(View):

    def get(self, request):
        return render(
            request,
            'logs/ok.html'
        )
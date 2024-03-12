from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CodeForm
from .models import Team, Winner


def index(request):
    form = CodeForm()
    return render(request, "code.html", {"form": form})


def check_code(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                team = Team.objects.get(code=data["code"])
            except Team.DoesNotExist:
                return HttpResponse(
                    '<h1>The code is incorrect!<h1><h1><a href="/">Try again!</a><h1>'
                )
            else:
                try:
                    win = Winner.objects.get(team=team)
                except Winner.DoesNotExist:
                    win = Winner.objects.create(team=team)
                return HttpResponse(
                    f'<marquee direction="right"><h1>Well done!</h1></marquee><h2>Congrats team "{team.name}"</h2><h2>You ended in {win.id} place!</h2>'
                )

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse("")

from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.views.generic import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from .mixins import OnlyYouMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserForm, ListForm, CardForm, CardCreateFromHomeForm
from .models import List, Card
from .models import *




# Create your views here.
class TopPage(TemplateView):
    template_name = 'kanban/top.html'

class HomeView(LoginRequiredMixin, ListView):
    model = List
    template_name = "kanban/home.html"

class SignUp(View):
    template_name = 'kanban/signup.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user_instance = form.save()
                login(request, user_instance)
                return redirect('kanban:home')
            else:
                context = {
                    'form': form
                }
                return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


# LoginRequiredMixinで、ログイン者しか見れない(自分以外のも見れる)
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "kanban/users/detail.html"

# OnlyYouMixinで自身しかアクセスできない
class UserUpdateView(OnlyYouMixin, UpdateView):
    model = User
    template_name = "kanban/users/update.html"
    form_class = UserForm
    def get_success_url(self):
        return resolve_url('kanban:users_detail', pk=self.kwargs['pk'])




class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = "kanban/lists/create.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:lists_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListListView(LoginRequiredMixin, ListView):
    model = List
    template_name = "kanban/lists/list.html"


class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = "kanban/lists/detail.html"

class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    template_name = "kanban/lists/update.html"
    form_class = ListForm
    def get_success_url(self):
        return resolve_url("kanban:lists_detail", pk=self.kwargs['pk'])

class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = "kanban/lists/delete.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:lists_list")




class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "kanban/cards/create.html"
    form_class = CardForm
    success_url = reverse_lazy("kanban:cards_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardCreateFromHomeView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "kanban/cards/create.html"
    form_class = CardCreateFromHomeForm
    success_url = reverse_lazy("kanban:home")
    def form_valid(self, form):
        list_pk = self.kwargs['list_pk']
        list_instance = get_object_or_404(List, pk=list_pk)
        form.instance.list = list_instance
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = "kanban/cards/list.html"


class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = "kanban/cards/detail.html"

class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    template_name = "kanban/cards/update.html"
    form_class = CardForm

    def get_success_url(self):
        return resolve_url('kanban:cards_detail', pk=self.kwargs['pk'])

class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = "kanban/cards/delete.html"
    form_class = CardForm
    success_url = reverse_lazy("kanban:cards_list")




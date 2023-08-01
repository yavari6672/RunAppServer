from django.shortcuts import render
from django.views import generic
from .env import BTN, TBL
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    return render(request, 'index.html', {'title': 'RunAppServer'})


@login_required
def main_index(request):
    return render(request, 'main/index.html', {'title': 'RunAppServer-main'})


class CustomListView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    paginate_by = 10
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["BTN"] = BTN()
        context["TBL"] = TBL()
        return context


class CustomCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["BTN"] = BTN()
        return context


class CustomUpdateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["BTN"] = BTN()
        return context


class CustomFormView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, generic.FormView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["BTN"] = BTN()
        return context


class CustomDeleteView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["BTN"] = BTN()
        return context


class CustomDetailView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, generic.DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["BTN"] = BTN()
        context["TBL"] = TBL()
        return context

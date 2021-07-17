from django.http import HttpResponseRedirect
from django.shortcuts import render
from productin.models import prodcutin
from .models import loss
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class NewLoss(LoginRequiredMixin,CreateView):
    model = loss
    fields = '__all__'


class ViewLoss(LoginRequiredMixin,ListView):
    model = loss
    context_object_name = 'losses'


class UpdateLoss(LoginRequiredMixin,UpdateView):
    model = loss
    fields = '__all__'


class DeleteLoss(LoginRequiredMixin,DeleteView):
    model = loss
    success_url = '/loss/view'
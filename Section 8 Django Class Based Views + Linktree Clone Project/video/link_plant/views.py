from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Link
from django.shortcuts import get_object_or_404

class LinkListView(ListView):
    model = Link  # Specify the model you want to use

    def get_queryset(self):
        # Define the queryset for the ListView
        return Link.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Define the context data
        context['extra_variable'] = 'Some value'
        return context

class LinkCreateView(CreateView):
    # create forms. py file & form
    # check if this was a post or get request
    # return an empty form or or save the form data
    # template model_form -> link_form.html
    model = Link
    fields = "__all__"
    # look up url to redirect on success
    success_url = reverse_lazy('link-list')

class LinkUpdateView(UpdateView):
    # create a form
    # check for get or put request
    # either render or update and save the form in our db
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')

class LinkDeleteView(DeleteView) :
    model = Link
    success_url = reverse_lazy('link-list')

def profile_view(request, profile_slug):
    profile = get_object_or_404(profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links
    }
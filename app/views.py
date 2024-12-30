from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

# Simply LoginRequiredMixin is used to restrict the access to the views to only authenticated users.
# UserPassesTestMixin is used to restrict the access to the views to only the creator of the article.

class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "app/home.html"
    model =  Article
    context_object_name = "articles"
    paginate_by = 5
    
    def get_queryset(self):
        search = self.request.GET.get("search")
        queryset = super().get_queryset().filter(creator=self.request.user)
        if search:
            queryset = queryset.filter(title__search=search)
        return queryset.order_by("-created_at")

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'app/article_create.html'
    model = Article
    fields = ['title', 'status', 'content', 'twitter_post']
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        messages.success(request, "Article created successfully")
        return super().post(request, *args, **kwargs)
    

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'app/article_update.html'
    model = Article
    fields = ['title', 'status', 'content', 'twitter_post']
    success_url = reverse_lazy("home")
    context_object_name = "article"
    
    def test_func(self):
        return self.request.user == self.get_object().creator

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'app/article_delete.html'
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"
    
    def test_func(self):
        return self.request.user == self.get_object().creator

    def post(self, request, *args, **kwargs):
        # short hand way to add messages
        messages.error(request, "Article deleted successfully")
        # we can add extra tags like this
        # messages.error(request, "Article deleted successfully", extra_tags="delete-success")
        # altertive long way is this
        # messages.add_message(request, messages.ERROR, "Article deleted successfully", extra_tags="delete-success")
        return super().post(request, *args, **kwargs)
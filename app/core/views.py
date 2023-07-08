from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from .models import TodoItem


class Index(View):
    template_name = "index.html"

    def get(self, req):
        """Get all todos"""
        todos = TodoItem.objects.all()

        """Make the context"""
        context = {"todos": todos}

        """Render template and pass context"""
        return render(req, self.template_name, context)

    def post(self, req):
        """Get new todo"""
        newTodo = req.POST.get("todo-item")

        """Save new todo in db"""
        TodoItem.objects.create(title=newTodo)

        """Redirect to /"""
        return redirect(reverse("home"))


class EditTodo(View):
    def post(self, req):
        """Edit todo"""
        todoId = req.POST.get("todo-id")
        newTodo = req.POST.get("updated-todo")

        TodoItem.objects.filter(id=todoId).update(title=newTodo)

        """Redirect to /"""
        return redirect(reverse("home"))


class DeleteTodo(View):
    def get(self, req, id):
        """Delete todo"""
        TodoItem.objects.filter(id=id).delete()

        """Redirect to /"""
        return redirect(reverse("home"))

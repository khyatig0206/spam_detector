from django.shortcuts import redirect, render,get_object_or_404
from spamfilter.models import Comment
from spamfilter.spam import predict_spam
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,CommentForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('comments')  # Redirect to the comments page after registration
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('comments')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comments')
    else:
        form = CommentForm()
    
    return render(request, 'create_comment.html', {'form': form})




def comments(request):
    comments=Comment.objects.all()
    context={"comments":comments}
    return render(request,"comments.html",context)

def check_spam(request):
    comments=Comment.objects.all()
    predictions = predict_spam(comments.values_list('text',flat=True)) #flat transform the list of tuples from the query set to list of values
    print(predictions)

    context={"comments":zip(comments,predictions)}
    return render(request,"partials/comments_spam.html",context)



def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_staff:
        comment.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)
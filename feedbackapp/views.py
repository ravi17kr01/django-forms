from django.shortcuts import render
from . import forms


def thankyou_view(request):
    return render(request,'feedbackapp/thankyou.html')

def feedback_view(request):
    if request.method == 'GET':
        form = forms.FeedBackForm()

    if request.method == 'POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printing feedback info')
            print('Student Name:', form.cleaned_data['name'])
            print('Student Roll No:',form.cleaned_data['rollno'])
            print('Student Mail Id:', form.cleaned_data['email'])
            print('Student Password:', form.cleaned_data['password'])
            print('Student Re-Password:', form.cleaned_data['rpassword'])
            print('Student Feedback:', form.cleaned_data['feedback'])
    return render(request, 'feedbackapp/feedback.html', {'form': form})

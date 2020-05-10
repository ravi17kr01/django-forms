from django import forms
from django.core import validators

# def starts_with_d(value):
#     if value[0] != 'd':
#     # if value.isalpha() != True
#         raise forms.ValidationError('Your name should start with d')
#
# def gmail_verification(value):
#     if value[len(value)-9:] != 'gmail.com':
#         raise forms.ValidationError('gmail should be there')

class FeedBackForm(forms.Form):
    name = forms.CharField()
    # name = forms.CharField(validators=[starts_with_d(value)])
    rollno = forms.IntegerField()
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Enter Password again', widget=forms.PasswordInput)
    # email = forms.EmailField(validators=[gmail_verification(value)])
    bot_handler=forms.CharField(required=False, widget=forms.HiddenInput)
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])

    def clean(self):
        print('Total Form Validation')
        cleaned_data=super().clean()
        inputbot_handler=cleaned_data['bot_handler']
        if len(inputbot_handler)>0:
            raise forms.ValidationError('You are caught BOT!!!!! ')

        inputpassword=cleaned_data['password']
        inputrpassword=cleaned_data['rpassword']
        if inputpassword != inputrpassword:
            raise forms.ValidationError('passwrd isnt matching')

        inputname=cleaned_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError('>10 should be there')
        inputrollno=cleaned_data['rollno']
        if len(str(inputrollno)) != 3:
            raise forms.ValidationError('must be 3 digits')




    # def clean_name(self):
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<4:
    #         raise forms.ValidationError('length>=4')
    #     return inputname






# def clean_rollno(self):
#     inputrollno=self.cleaned_data['rollno']
#     print('validating rollno')
#     return inputrollno
#
# def clean_email(self):
#     inputemail=self.cleaned_data['email']
#     print('validating email')
#     return email
#
# def clean_feedback(self):
#     inputfeedback=self.cleaned_data['feedback']
#     print('validating feedback')
#     return inputfeedback

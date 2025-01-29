from django.shortcuts import render
from .forms import MedicalQueryForm
from .models import MedicalQuery
from .ai_handler import get_medical_response

def home(request):
    if request.method == 'POST':
        form = MedicalQueryForm(request.POST)
        if form.is_valid():
            # Save user input
            user_input = form.cleaned_data['user_input']
            
            # Get AI response
            ai_response = get_medical_response(user_input)
            
            # Save to database
            MedicalQuery.objects.create(
                user_input=user_input,
                ai_response=ai_response
            )
            
            return render(request, 'result.html', {
                'user_input': user_input,
                'ai_response': ai_response
            })
    else:
        form = MedicalQueryForm()
    
    return render(request, 'home.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_us')  # Redirect to the same page after successful submission
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

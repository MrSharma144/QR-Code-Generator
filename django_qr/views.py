from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
        # Generate QR code
        qr = qrcode.make(url)
        qr_filename = restaurant_name.replace(" ", "_").lower() + '_qr.png'
        qr_filepath = os.path.join(settings.MEDIA_ROOT, qr_filename) #media/filename
        qr.save(qr_filepath)

        # create Image URL
        qr_url = os.path.join(settings.MEDIA_URL, qr_filename)
        context = {
            'res_name': restaurant_name,
            'qr_code_url': qr_filename,
            'qr_code_path': qr_url,
        }
        return render(request, 'qr_code_result.html', context)
    else:
        form = QRCodeForm()
        context = {
            'form': form,
            }
        return render(request, 'generate_qr_code.html', context)

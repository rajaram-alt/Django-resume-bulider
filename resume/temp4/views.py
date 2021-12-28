from django.shortcuts import render,redirect,get_object_or_404
from temp4.models import *
from temp4.forms import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def show(request):
    datas=temp4model.objects.all()
    return render(request,'temp4.html',{'datas':datas})

def temp4post(request):
    datas=temp4model.objects.all()
    form=temp4Form
    if request.method == 'POST':
        form=temp4Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/temp4/get4')
    return render(request,'post4.html',{'form':form,'datas':datas})

def temp4get(request):
    datas=temp4model.objects.all()
    return render(request,'get4.html',{'datas':datas})

def temp4update(request,pk):
    dataupdate=temp4model.objects.get(id=pk)
    form=temp4Form(instance=dataupdate)
    if request.method == 'POST':
        form=temp4Form(request.POST,request.FILES,instance=dataupdate)
        if form.is_valid():
             form.save()
             return redirect('/temp4/get4')
    return render(request,'temp4upd.html',{'datas':dataupdate,'form':form})

# Create your views here.

def pdf_download4(request,*args,**kwargs):
    pk = kwargs.get('pk')
    pdfModel=get_object_or_404(temp4model,pk=pk)
    template_path = 'pdftemp4.html'
    context = {'data': pdfModel}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="resume.pdf"'
    #if download
    # response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

from django.shortcuts import render,redirect,get_object_or_404
from temp1.models import *
from temp1.forms import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def show(request):
    datas=temp1model.objects.all()
    return render(request,'temp1.html',{'datas':datas})
    
def main(request):
    return render(request,'main.html')

def temp1post(request):
    datas=temp1model.objects.all()
    form=temp1Form
    if request.method == 'POST':
        form=temp1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/temp1/get1')
    return render(request,'post1.html',{'form':form,'datas':datas})

def temp1get(request):
    datas=temp1model.objects.all()
    return render(request,'get1.html',{'datas':datas})

def temp1update(request,pk):
    dataupdate=temp1model.objects.get(id=pk)
    form=temp1Form(instance=dataupdate)
    if request.method == 'POST':
        form=temp1Form(request.POST,request.FILES,instance=dataupdate)
        if form.is_valid():
             form.save()
             return redirect('/temp1/get1')
    return render(request,'temp1upd.html',{'datas':dataupdate,'form':form})

# Create your views here.

def pdf_download(request,*args,**kwargs):
    pk = kwargs.get('pk')
    pdfModel=get_object_or_404(temp1model,pk=pk)
    template_path = 'pdftemp1.html'
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

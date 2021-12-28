from django.shortcuts import render,redirect,get_object_or_404
from temp2.models import *
from temp2.forms import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def show(request):
    datas=temp2model.objects.all()
    return render(request,'temp2.html',{'datas':datas})

def temp2post(request):
    datas=temp2model.objects.all()
    form=temp2Form
    if request.method == 'POST':
        form=temp2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/temp2/get2')
    return render(request,'post2.html',{'form':form,'datas':datas})

def temp2get(request):
    datas=temp2model.objects.all()
    return render(request,'get2.html',{'datas':datas})

def temp2update(request,pk):
    dataupdate=temp2model.objects.get(id=pk)
    form=temp2Form(instance=dataupdate)
    if request.method == 'POST':
        form=temp2Form(request.POST,request.FILES,instance=dataupdate)
        if form.is_valid():
             form.save()
             return redirect('/temp2/get2')
    return render(request,'temp2upd.html',{'datas':dataupdate,'form':form})

# Create your views here.

def pdf_download2(request,*args,**kwargs):
    pk = kwargs.get('pk')
    pdfModel=get_object_or_404(temp2model,pk=pk)
    template_path = 'pdftemp2.html'
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
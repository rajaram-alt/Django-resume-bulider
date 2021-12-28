from django.shortcuts import render,redirect,get_object_or_404
from temp3.models import *
from temp3.forms import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def show(request):
    datas=temp3model.objects.all()
    return render(request,'temp3.html',{'datas':datas})

def temp3post(request):
    datas=temp3model.objects.all()
    form=temp3Form
    if request.method == 'POST':
        form=temp3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/temp3/get3')
    return render(request,'post3.html',{'form':form,'datas':datas})

def temp3get(request):
    datas=temp3model.objects.all()
    return render(request,'get3.html',{'datas':datas})

def temp3update(request,pk):
    dataupdate=temp3model.objects.get(id=pk)
    form=temp3Form(instance=dataupdate)
    if request.method == 'POST':
        form=temp3Form(request.POST,request.FILES,instance=dataupdate)
        if form.is_valid():
             form.save()
             return redirect('/temp3/get3')
    return render(request,'temp3upd.html',{'datas':dataupdate,'form':form})

# Create your views here.

def pdf_download3(request,*args,**kwargs):
    pk = kwargs.get('pk')
    pdfModel=get_object_or_404(temp3model,pk=pk)
    template_path = 'pdftemp3.html'
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
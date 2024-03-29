from django.shortcuts import render,redirect
from batch.forms import BatchForm

def createBatch(request):
    if request.method == "GET":
        form = BatchForm()
        return render(request,'batch/batchCreate.html',{'form':form})
    elif request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('batch:list_batch')
        return render(request,'batch/batchCreate.html',{'form':form})
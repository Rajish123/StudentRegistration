from batch.models import Batch
from batch.forms import BatchForm
from django.shortcuts import render,redirect

def updateBatch(request, id):
    context = {}
    batch = Batch.get_batch_by_id(id)
    if request.method == "POST":
        form = BatchForm(request.POST, instance = batch)
        if form.is_valid():
            form.save()
            # return redirect('batch:detail_batch' batch.id)
    else:
        form = BatchForm(instance=batch)
        context = {'form':form}
    return render(request,'batchCreate.html',context)
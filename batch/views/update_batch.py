from batch.models import Batch
from batch.forms import BatchForm
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect


def updateBatch(request, id):
    context = {}
    batch = Batch.get_batch_by_id(id)
    if batch:
        if request.method == "POST":
            form = BatchForm(request.POST, instance = batch)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('batch:detail_batch', args = [batch.id]))
        else:
            form = BatchForm(instance=batch)
            context = {'batch':batch, 'form':form}
        return render(request,'batchCreate.html',context)
    else:
        raise Http404()
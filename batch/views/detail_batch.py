from django.http import Http404
from django.shortcuts import render
from batch.models import Batch
from django.http import Http404

def detailBatch(request,id):
    context = {}
    batch = Batch.get_batch_by_id(id)
    if batch:
        context['batch'] = batch
        return render(request, 'batch/batchDetail.html',context)
    else:
        raise Http404()
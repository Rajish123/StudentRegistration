from django.shortcuts import render
from batch.models import Batch
from batch.forms import BatchForm

def detailBatch(request,id):
    context = {}
    batch = Batch.get_batch_by_id(id)
    context['batch'] = batch
    return render(request, 'batchDetail.html',context)
from batch.models import Batch
from django.shortcuts import render


def listBatch(request):
    context = {}
    batches = Batch.get_all_batch()
    context ={'batches':batches} 
    return render(request, 'batchList.html', context)

from django.http import Http404
from django.shortcuts import redirect
from batch.models import Batch
from django.shortcuts import redirect, render
from django.http import Http404


def deleteBatch(request,id):
    batch = Batch.get_batch_by_id(id)
    if batch:
        if request.method == "POST":
            batch.delete()
            return redirect('batch:list_batch')
        return render(request,'batch/batchDelete.html')
    else:
        raise Http404()
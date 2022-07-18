from django.shortcuts import redirect
from batch.models import Batch
from django.shortcuts import redirect, render

def deleteBatch(request,id):
    context = {}
    batch = Batch.get_batch_by_id(id)
    if request.method == "POST":
        batch.delete()
        return redirect('batch:list_batch')
    return render(request,'batchDelete.html')
from django.urls import path
from batch.views import create_batch, update_batch, detail_batch, list_batch, delete_batch

app_name = 'batch'

urlpatterns = [
    path('create_batch',create_batch.createBatch, name = 'create_batch'),
    path('update_batch/<str:id>',update_batch.updateBatch, name = 'update_batch'),
    path('detail_batch/<str:id>',detail_batch.detailBatch, name = 'detail_batch'),
    path('list_batch',list_batch.listBatch, name = 'list_batch'),
    path('delete_batch/<str:id>',delete_batch.deleteBatch,name = 'delete_batch')



    
]

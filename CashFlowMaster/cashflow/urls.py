from django.contrib import admin
from django.urls import path, include

from cashflow import views


app_name = 'cashflow'


urlpatterns = [
     path('', views.MainView.as_view(), name='main'),
     
     path('reference_manage/', 
          views.ReferenceManage.as_view(), 
          name='reference_manage'),


     # Transaction

     path('create_transact/', 
          views.TransactCreateView.as_view(), 
          name='create_transact'),

     path('detail_transact/<int:pk>', 
          views.TransactDetailView.as_view(), 
          name='detail_transact'),

     path('update_transact/<int:pk>', 
          views.TransactUpdateView.as_view(), 
          name='update_transact'),

     path('delete_transact/<int:pk>', 
          views.TransactDeleteView.as_view(), 
          name='delete_transact'),


     # StatusAction

     path('create_status_action/', 
          views.StatusActionCreateView.as_view(), 
          name='create_status_action'),

     path('update_status_action/<int:pk>', 
          views.StatusActionUpdateView.as_view(), 
          name='update_status_action'),

     path('delete_status_action/<int:pk>', 
          views.StatusActionDeleteView.as_view(), 
          name='delete_status_action'),


     # TypeAction

     path('create_type_action/', 
          views.TypeActionCreateView.as_view(), 
          name='create_type_action'),

     path('update_type_action/<int:pk>', 
          views.TypeActionUpdateView.as_view(), 
          name='update_type_action'),

     path('delete_type_action/<int:pk>', 
          views.TypeActionDeleteView.as_view(), 
          name='delete_type_action'),


     # CategoryAction

     path('create_category_action/', 
          views.CategoryActionCreateView.as_view(), 
          name='create_category_action'),

     path('update_category_action/<int:pk>', 
          views.CategoryActionUpdateView.as_view(), 
          name='update_category_action'),

     path('delete_category_action/<int:pk>', 
          views.CategoryActionDeleteView.as_view(), 
          name='delete_category_action'),


     # SubcategoryAction

     path('create_subcategory_action/', 
          views.SubcategoryActionCreateView.as_view(), 
          name='create_subcategory_action'),

     path('update_subcategory_action/<int:pk>', 
          views.SubcategoryActionUpdateView.as_view(), 
          name='update_subcategory_action'),

     path('delete_subcategory_action/<int:pk>', 
          views.SubcategoryActionDeleteView.as_view(), 
          name='delete_subcategory_action'),
]
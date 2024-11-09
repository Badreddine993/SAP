from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="income"),
    path('add-Income', views.add_Income, name="add-Income"),
    path('edit-Income/<int:id>', views.edit_Income, name="edit-Income"),
    path('delete-Income/<int:id>', views.delete_Income, name="delete-Income"),
    path('search-Income', views.search_expenses, name="search-Income"),
    path('export/income/csv/', views.export_income_csv, name='export_income_csv'),
    path('export/income/pdf/', views.export_income_pdf, name='export_income_pdf'),
    path('export/income/excel/', views.export_income_excel, name='export_income_excel'),
    path('stat', views.stats_view, name="stat"),
    path('income-source-summary', views.income_source_summary, name="income-source-summary"),

]
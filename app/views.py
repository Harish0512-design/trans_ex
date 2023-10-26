from django.shortcuts import render, redirect

from django.http import HttpResponse
import pandas as pd

from app.forms import FilterForm
from app.models import Transactions


# Create your views here.
def home(request):
    form = FilterForm()
    if request.POST:
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        print(from_date)
        print(type(from_date))
        transactions = Transactions.objects.filter(trans_date__range=(from_date, to_date))
        print(transactions)
        return render(request, "base.html", {'form': form, 'transactions': transactions})

    return render(request, "base.html", {'form': form})


def export_to_csv(request):
    data = Transactions.objects.all()
    df = pd.DataFrame(list(data.values()))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    df.to_csv(response, index=False)
    return response


def export_to_xlsx(request):
    # Query your data
    data = Transactions.objects.all()

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(list(data.values()))

    # Create an XLSX response
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(response, engine='openpyxl')
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Save the writer to the response and return it.
    writer.close()
    return response
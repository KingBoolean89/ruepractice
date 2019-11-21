from django.shortcuts import render
from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        product_resource = PersonResource()
        dataset = Dataset()
        new_product = request.FILES['myfile']

        imported_data = dataset.load(new_product.read())
        result = product_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            product_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')



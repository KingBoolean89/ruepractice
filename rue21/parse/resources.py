from import_export import resources, fields
from .models import Product

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ('po',)
        fields = ('po', 'item', 'color', 'size', 'description', 'qty')
        skip_unchanged = True
        
        
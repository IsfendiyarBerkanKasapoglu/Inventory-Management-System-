from django.forms import ModelForm
from .models import Inventory

class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = [ 'name', 'cost_per_item', 'quantity_in_stock']


class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = [ 'name', 'cost_per_item', 'quantity_in_stock']
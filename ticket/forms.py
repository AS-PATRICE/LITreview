from django.forms import ModelForm, fields
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')
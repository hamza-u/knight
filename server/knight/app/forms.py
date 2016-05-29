from app import models
from django.forms import ModelForm

class ClientForm(ModelForm):
	class Meta:
		model = models.Client
		fields = [ "client_id", "client", "partner", "handler", "email", "phone" ]
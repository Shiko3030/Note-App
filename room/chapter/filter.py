import django_filters

from .models import *




class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Students
        fields = '__all__'

class TechersFilter(django_filters.FilterSet):
    class Meta:
        model = Techers
        fields = '__all__'
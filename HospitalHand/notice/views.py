from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from hospital.models import Hospital
from .models import notice_model
from .serializers import notice_serializers


class notice_view(CreateAPIView):
    serializer_class = notice_serializers


class notice_list_view(ListAPIView):
    serializer_class = notice_serializers
    queryset = notice_model.objects.all()


class notice_delete_view(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = notice_serializers
    queryset = notice_model.objects.all()

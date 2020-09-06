
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from .forms import notice_form
from .models import notice_model
from .serializers import notice_serializers
from .task import sleepy


class notice_view(CreateAPIView):
    serializer_class = notice_serializers


class notice_list_view(ListAPIView):
    serializer_class = notice_serializers
    queryset = notice_model.objects.all()


class notice_delete_view(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = notice_serializers
    queryset = notice_model.objects.all()

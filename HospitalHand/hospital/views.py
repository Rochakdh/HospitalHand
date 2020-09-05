from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import HospitalModelSerializer
from .models import Hospital


class HospitalModelListAPIView(ListAPIView):
    serializer_class = HospitalModelSerializer
    queryset = Hospital.objects.all()

    def get_queryset(self):
        super(HospitalModelListAPIView, self).get_queryset()
        return self.queryset.filter(name_id=self.request.user.id)

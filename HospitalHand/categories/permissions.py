from rest_framework.permissions import IsAuthenticated


class HospitalIsAuthenticated(IsAuthenticated):
    message = 'Access Denied'

    def has_permission(self, request, view):
        if request.user.is_hospital:
            return super(HospitalIsAuthenticated, self).has_permission(request, view)
            print(request.user)
        else:
            return False


class HospitalIsObjectAuthenticated(IsAuthenticated):
    message = 'Access Denied'

    def has_object_permission(self, request, view, obj):
        print(f'Request->>{request}')
        print(f'object->>{obj}')
        return request.user == obj

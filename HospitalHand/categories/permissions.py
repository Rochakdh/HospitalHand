from rest_framework.permissions import IsAuthenticated


class HospitalIsAuthenticated(IsAuthenticated):
    message = 'Access Denied'
    def has_permission(self, request, view):
        if request.user.is_hospital:
            return super(HospitalIsAuthenticated, self).has_permission( request, view)
        else:
            return False
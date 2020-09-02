from rest_framework.permissions import IsAuthenticated


class CustomIsAuthenticated(IsAuthenticated):
    message = 'Access Denied'

    def has_object_permission(self, request, view, obj):
        # print(request.user)
        return request.user == obj

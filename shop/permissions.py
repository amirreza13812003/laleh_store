from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user and request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user and request.user.is_staff
    

class IsAdminUserOrCustomerOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.role == 'customer')
    
    def has_object_permission(self, request, view, obj):
        return request.user and (request.user.is_staff or request.user == obj.user)

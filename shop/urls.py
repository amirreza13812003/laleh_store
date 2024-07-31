from rest_framework_nested import routers
from .views import ProductViewSet, CartViewSet, CartItemViewSet, CustomerViewSet, OrderViewSet, ProductImageViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product') 
router.register('carts', CartViewSet, basename='cart')
router.register('customers', CustomerViewSet, basename='customer')
router.register('orders', OrderViewSet, basename='order')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('images', ProductImageViewSet, basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + carts_router.urls + product_router.urls
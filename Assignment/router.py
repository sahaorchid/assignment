

from REST_Assignment.projectapp.viewsets import CustomersViewset


from rest_framework import routers

router =routers.SimpleRouter()
router.register('Customers' ,CustomersViewset)
urlpatterns = router.urls

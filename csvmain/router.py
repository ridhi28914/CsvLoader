from rest_framework import routers

from csvapp.views import CSVview




router = routers.SimpleRouter()

router.register(r'',CSVview)

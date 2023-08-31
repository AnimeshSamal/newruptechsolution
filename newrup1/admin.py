from django.contrib import admin
from .models import Contact,Services,Partner,Testimonial,Photo,Product,Achivement,About,Link,Track
# Register your models here.
admin.site.register(Track)
admin.site.register(Link)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Partner)
admin.site.register(Services)
admin.site.register(Testimonial)
admin.site.register(Photo)
admin.site.register(Product)
admin.site.register(Achivement)

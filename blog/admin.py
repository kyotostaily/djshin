from django.contrib import admin
from .models import Post, Category #199 Category추가

admin.site.register(Post)


class CategoryAdmin(admin.ModelAdmin): #200. admin의 modelAdmin
    prepopulated_fields = {'slug': ('name', )} #202.slug를 name으로 만들었으면 좋겠다는 뜻


admin.site.register(Category, CategoryAdmin) #203.레지스터에 Category와 CategoryAdmin을 입력한다. 이렇게 하면 admin의 cateories에서 Name을 입력시 자동으로 Slug에도 입력이 된다. 이제 models.py 13째 줄로 간다.

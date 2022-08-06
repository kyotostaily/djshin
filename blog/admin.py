from django.contrib import admin
from .models import Post, Category, Tag, Comment #489. Comment를 임포트 하고, 5줄로 이동한다.

admin.site.register(Post)
admin.site.register(Comment) #490. Comment사용을 위해 이와같이 입력한다. 이제 tests.py의 4째 줄로 이동한다.


class CategoryAdmin(admin.ModelAdmin): #200. admin의 modelAdmin
    prepopulated_fields = {'slug': ('name', )} #202.slug를 name으로 만들었으면 좋겠다는 뜻


class TagAdmin(admin.ModelAdmin): #302. 위의것을 붙여넣고 TagAdmin이라 변경한다.
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin) #203.레지스터에 Category와 CategoryAdmin을 입력한다. 이렇게 하면 admin의 cateories에서 Name을 입력시 자동으로 Slug에도 입력이 된다. 이제 models.py 13째 줄로 간다.
admin.site.register(Tag, TagAdmin) #303. 위의것 복사한 후 이와같이 이름을 변경한 후 304. 젤 위에 Tag를 임포트한다. 이제 tests.py의 26째줄로 이동한다.

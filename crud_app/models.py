from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, is_deleted=True, *args, **kwargs):
        if is_deleted:
            self.is_deleted = True
            self.is_active = False
            self.save()
        else:
            super().delete(*args, **kwargs)

class Category(BaseModel):
    name = models.TextField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = "category"

    def __str__(self):
        return self.name

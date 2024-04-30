from tortoise.models import Model
from tortoise.fields import (CharField, UUIDField, BooleanField, DatetimeField)
from uuid import uuid4

class Todo(Model):
    id = UUIDField(pk=True, default=uuid4)
    title = CharField(max_length=100, null=False)
    done = BooleanField(null=False, default=False)
    create_at = DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Meta:
    table = 'todos'
    ordering = ['-created_at']
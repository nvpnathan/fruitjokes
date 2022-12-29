from tortoise import fields, models


class Jokes(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    author = fields.ForeignKeyField("models.Users", related_name="joke")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author} on {self.created_at}"

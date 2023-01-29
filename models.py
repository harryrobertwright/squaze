import orm_sqlite


class Score(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    value = orm_sqlite.IntegerField()

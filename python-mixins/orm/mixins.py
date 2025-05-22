import logging
import time
from dataclasses import field

from orm.core import ActiveRecordMeta

CREATED_AT_COLUMN = "created_at"
UPDATED_AT_COLUMN = "updated_at"

logger = logging.getLogger(__name__)


class SQLMixin:
    @classmethod
    def find_all(cls):
        logger.debug(cls.__table__.sql.select_all)
        return super().find_all()

    @classmethod
    def find_by(cls, **parameters):
        logger.debug(cls.__table__.sql.select_where(**parameters))
        return super().find_by(**parameters)

    def save(self):
        if self.pk is None:
            logger.debug(self.__table__.sql.insert(self))
        else:
            logger.debug(self.__table__.sql.update(self))
        super().save()

    def delete(self):
        logger.debug(self.__table__.sql.delete(self))
        return super().delete()


class TimestampMixinMeta(ActiveRecordMeta):
    def __call__(cls, *args, **kwargs):
        created_at = kwargs.pop(CREATED_AT_COLUMN, None)
        updated_at = kwargs.pop(UPDATED_AT_COLUMN, None)
        instance = super().__call__(*args, **kwargs)
        instance.created_at = created_at
        instance.updated_at = updated_at
        return instance


class TimestampMixin(metaclass=TimestampMixinMeta):
    created_at: int = field(init=False, repr=False)
    updated_at: int = field(init=False, repr=False)

    def save(self) -> None:
        current_time = int(time.time())
        if self.pk is None:
            self.created_at = current_time
            self.updated_at = current_time
        else:
            self.updated_at = current_time
        super().save()

# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from amundsen_rds.models.base import (
    INDEX_KEY_COLLATION_ARGS, KEY_LEN, PUBLISHED_TAG_LEN, Base
)


class TableColumn(Base):
    """
    Column model.
    """
    __tablename__ = 'column_metadata'

    rk = Column(String(1536, **INDEX_KEY_COLLATION_ARGS), primary_key=True)
    name = Column(String(768), nullable=False)
    type = Column(String(32), nullable=False)
    sort_order = Column(Integer, nullable=False)
    table_rk = Column(String(KEY_LEN, **INDEX_KEY_COLLATION_ARGS),
                      ForeignKey('table_metadata.rk', ondelete='cascade'),
                      nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

    description = relationship('ColumnDescription', uselist=False)
    badges = relationship('Badge', order_by='Badge.rk', secondary='column_badge', backref='columns')
    stats = relationship('ColumnStat', order_by='ColumnStat.rk')


class ColumnDescription(Base):
    """
    Description model for column.
    """
    __tablename__ = 'column_description'

    rk = Column(String(1536, **INDEX_KEY_COLLATION_ARGS), primary_key=True)
    description_source = Column(String(32), nullable=False)
    description = Column(Text)
    column_rk = Column(String(KEY_LEN, **INDEX_KEY_COLLATION_ARGS),
                       ForeignKey('column_metadata.rk', ondelete='cascade'),
                       nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class ColumnBadge(Base):
    """
    Association model for column-badge.
    """
    __tablename__ = 'column_badge'

    column_rk = Column(String(1536, **INDEX_KEY_COLLATION_ARGS),
                       ForeignKey('column_metadata.rk', ondelete='cascade'),
                       primary_key=True)
    badge_rk = Column(String(128, **INDEX_KEY_COLLATION_ARGS),
                      ForeignKey('badge.rk', ondelete='cascade'),
                      primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class ColumnStat(Base):
    """
    Stat model for column.
    """
    __tablename__ = 'column_stat'

    rk = Column(String(1536, **INDEX_KEY_COLLATION_ARGS), primary_key=True)
    stat_type = Column(String(256), nullable=False)
    stat_val = Column(String(128), nullable=False)
    start_epoch = Column(String(16), nullable=False)
    end_epoch = Column(String(16), nullable=False)
    column_rk = Column(String(1536, **INDEX_KEY_COLLATION_ARGS),
                       ForeignKey('column_metadata.rk', ondelete='cascade'),
                       nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

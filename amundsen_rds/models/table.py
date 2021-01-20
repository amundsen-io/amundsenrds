# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import (
    BigInteger, Boolean, Column, ForeignKey, Integer, String, Text
)
from sqlalchemy.orm import relationship

from amundsen_rds.models.base import (
    KEY_LEN, NAME_LEN, PUBLISHED_TAG_LEN, URL_LEN, Base
)


class Table(Base):
    """
    Table model.
    """
    __tablename__ = 'table_metadata'

    rk = Column(String(KEY_LEN), primary_key=True)
    name = Column(String(NAME_LEN), nullable=False)
    is_view = Column(Boolean, nullable=False)
    schema_rk = Column(String(KEY_LEN), ForeignKey('schema_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger)

    schema = relationship('Schema')
    application = relationship('Application', uselist=False, secondary='application_table')
    columns = relationship('TableColumn', order_by='TableColumn.sort_order')
    description = relationship('TableDescription', uselist=False)
    programmatic_descriptions = relationship('TableProgrammaticDescription', order_by='TableProgrammaticDescription.rk')
    tags = relationship('Tag', order_by='Tag.rk', secondary='table_tag')
    badges = relationship('Badge', order_by='Badge.rk', secondary='table_badge')
    timestamp = relationship('TableTimestamp', uselist=False)
    watermarks = relationship('TableWatermark', order_by='TableWatermark.rk')
    source = relationship('TableSource', uselist=False)
    usage = relationship('TableUsage', order_by='TableUsage.user_rk', backref='table')
    readers = relationship('User', order_by='User.rk', secondary='table_usage', backref='tables_read')
    owners = relationship('User', order_by='User.rk', secondary='table_owner', backref='tables_owned')
    followers = relationship('User', order_by='User.rk', secondary='table_follower', backref='tables_followed')


class TableDescription(Base):
    """
    Description model for table.
    """
    __tablename__ = 'table_description'

    rk = Column(String(KEY_LEN), primary_key=True)
    description_source = Column(String(32), nullable=False)
    description = Column(Text)
    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class TableProgrammaticDescription(Base):
    """
    Programmatic description model for table.
    """
    __tablename__ = 'table_programmatic_description'

    rk = Column(String(KEY_LEN), primary_key=True)
    description_source = Column(String(32), nullable=False)
    description = Column(Text)
    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class TableUsage(Base):
    """
    Association model for table-reader.
    """
    __tablename__ = 'table_usage'

    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), primary_key=True)
    user_rk = Column(String(KEY_LEN), ForeignKey('users.rk', ondelete='cascade'), primary_key=True)
    read_count = Column(Integer, nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class TableOwner(Base):
    """
    Association model for table-owner.
    """
    __tablename__ = 'table_owner'

    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), primary_key=True)
    user_rk = Column(String(KEY_LEN), ForeignKey('users.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class TableFollower(Base):
    """
    Association model for table-follower.
    """
    __tablename__ = 'table_follower'

    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), primary_key=True)
    user_rk = Column(String(KEY_LEN), ForeignKey('users.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class TableTag(Base):
    """
    Association model for table-tag.
    """
    __tablename__ = 'table_tag'

    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), primary_key=True)
    tag_rk = Column(String(KEY_LEN), ForeignKey('tag.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class TableBadge(Base):
    """
    Association model for table-badge.
    """
    __tablename__ = 'table_badge'

    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), primary_key=True)
    badge_rk = Column(String(KEY_LEN), ForeignKey('badge.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class TableSource(Base):
    """
    Source model for table.
    """
    __tablename__ = 'table_source'

    rk = Column(String(KEY_LEN), primary_key=True)
    source = Column(String(URL_LEN), nullable=False)
    source_type = Column(String(32), nullable=False)
    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class TableTimestamp(Base):
    """
    Last_updated_timestamp model for table.
    """
    __tablename__ = 'table_timestamp'

    rk = Column(String(KEY_LEN), primary_key=True)
    last_updated_timestamp = Column(Integer, nullable=False)
    timestamp = Column(Integer, nullable=False)
    name = Column(String(NAME_LEN), nullable=False)
    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class TableWatermark(Base):
    """
    Watermark model for table.
    """
    __tablename__ = 'table_watermark'

    rk = Column(String(KEY_LEN), primary_key=True)
    partition_key = Column(String(32), nullable=False)
    partition_value = Column(String(32), nullable=False)
    create_time = Column(String(32), nullable=False)
    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

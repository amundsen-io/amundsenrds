# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, ForeignKey, String, Text

from amundsen_rds.models.base import (
    INDEX_KEY_COLLATION_ARGS, KEY_LEN, NAME_LEN, PUBLISHED_TAG_LEN, URL_LEN,
    Base
)


class Application(Base):
    """
    Application model
    """
    __tablename__ = 'application'

    rk = Column(String(KEY_LEN, **INDEX_KEY_COLLATION_ARGS), primary_key=True)
    application_url = Column(String(URL_LEN), nullable=False)
    name = Column(String(NAME_LEN), nullable=False)
    id = Column(String(128), nullable=False)
    description = Column(Text, nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class ApplicationTable(Base):
    """
    Model for tables derived from applications
    """
    __tablename__ = 'application_table'

    rk = Column(String(KEY_LEN, **INDEX_KEY_COLLATION_ARGS),
                ForeignKey('table_metadata.rk', ondelete='cascade'),
                primary_key=True)
    application_rk = Column(String(KEY_LEN, **INDEX_KEY_COLLATION_ARGS),
                            ForeignKey('application.rk', ondelete='cascade'),
                            nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

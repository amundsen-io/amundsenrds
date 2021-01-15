# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, ForeignKey, String, Text

from amundsen_rds.models.base import (
    KEY_LEN, NAME_LEN, PUBLISHED_TAG_LEN, URL_LEN, Base
)


class Application(Base):
    """
    Application model
    """
    __tablename__ = 'application'

    rk = Column(String(KEY_LEN), primary_key=True)
    application_url = Column(String(URL_LEN), nullable=False)
    name = Column(String(NAME_LEN), nullable=False)
    id = Column(String(128), nullable=False)
    description = Column(Text, nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class ApplicationTable(Base):
    """
    Association model for application-table.
    """
    __tablename__ = 'application_table'

    application_rk = Column(String(KEY_LEN), ForeignKey('application.rk', ondelete='cascade'), primary_key=True)
    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

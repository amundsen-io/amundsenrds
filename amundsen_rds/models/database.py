# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, String

from amundsen_rds.models.base import KEY_LEN, NAME_LEN, PUBLISHED_TAG_LEN, Base


class Database(Base):
    """
    Database model.
    """
    __tablename__ = 'database_metadata'

    rk = Column(String(KEY_LEN), primary_key=True)
    name = Column(String(NAME_LEN), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

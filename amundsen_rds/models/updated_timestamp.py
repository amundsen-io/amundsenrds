# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, Integer, String

from amundsen_rds.models.base import KEY_LEN, PUBLISHED_TAG_LEN, Base


class UpdatedTimestamp(Base):
    """
    Model to keep track the last updated timestamp for mysql and es.
    """
    __tablename__ = 'updated_timestamp'

    rk = Column(String(KEY_LEN), primary_key=True)
    last_timestamp = Column(Integer, nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

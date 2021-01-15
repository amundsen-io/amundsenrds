# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, String

from amundsen_rds.models.base import KEY_LEN, PUBLISHED_TAG_LEN, Base


class Badge(Base):
    """
    Badge model.
    """
    __tablename__ = 'badge'

    rk = Column(String(KEY_LEN), primary_key=True)
    category = Column(String(32), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)

# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from amundsen_rds.models.base import KEY_LEN, NAME_LEN, PUBLISHED_TAG_LEN, Base


class Cluster(Base):
    """
    Cluster model.
    """
    __tablename__ = 'cluster_metadata'

    rk = Column(String(KEY_LEN), primary_key=True)
    name = Column(String(NAME_LEN), nullable=False)
    database_rk = Column(String(KEY_LEN), ForeignKey('database_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

    database = relationship('Database')

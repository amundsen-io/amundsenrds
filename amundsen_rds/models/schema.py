# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from amundsen_rds.models.base import KEY_LEN, NAME_LEN, PUBLISHED_TAG_LEN, Base


class Schema(Base):
    """
    Schema model.
    """
    __tablename__ = 'schema_metadata'

    rk = Column(String(KEY_LEN), primary_key=True)
    name = Column(String(NAME_LEN), nullable=False)
    cluster_rk = Column(String(KEY_LEN), ForeignKey('cluster_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

    cluster = relationship('Cluster')
    description = relationship('SchemaDescription', uselist=False)


class SchemaDescription(Base):
    """
    Description model for schema.
    """
    __tablename__ = 'schema_description'

    rk = Column(String(KEY_LEN), primary_key=True)
    description_source = Column(String(32), nullable=False)
    description = Column(Text)
    schema_rk = Column(String(KEY_LEN), ForeignKey('schema_metadata.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

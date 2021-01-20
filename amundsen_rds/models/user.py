# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from amundsen_rds.models.base import KEY_LEN, PUBLISHED_TAG_LEN, Base


class User(Base):
    """
    User model.
    """
    __tablename__ = 'users'

    rk = Column(String(KEY_LEN), primary_key=True)
    email = Column(String(320), nullable=False)
    is_active = Column(Boolean)
    first_name = Column(String(64))
    last_name = Column(String(64))
    full_name = Column(String(256))
    github_username = Column(String(128))
    team_name = Column(String(128))
    employee_type = Column(String(32))
    slack_id = Column(String(32))
    role_name = Column(String(32))
    updated_at = Column(Integer)
    manager_rk = Column(String(KEY_LEN))
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)

    manager = relationship('User', uselist=False, primaryjoin='foreign(User.rk) == User.manager_rk')
    table_usage = relationship('TableUsage', order_by='TableUsage.table_rk', backref='reader')
    dashboard_usage = relationship('DashboardUsage', order_by='DashboardUsage.dashboard_rk', backref='reader')

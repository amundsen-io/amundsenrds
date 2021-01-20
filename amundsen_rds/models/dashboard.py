# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from amundsen_rds.models.base import (
    KEY_LEN, NAME_LEN, PUBLISHED_TAG_LEN, URL_LEN, Base
)


class Dashboard(Base):
    """
    Dashboard model.
    """
    __tablename__ = 'dashboard'

    rk = Column(String(KEY_LEN), primary_key=True)
    name = Column(String(NAME_LEN), nullable=False)
    created_timestamp = Column(Integer)
    dashboard_url = Column(String(URL_LEN))
    dashboard_group_rk = Column(String(KEY_LEN), ForeignKey('dashboard_group.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

    group = relationship('DashboardGroup')
    description = relationship('DashboardDescription', uselist=False)
    timestamp = relationship('DashboardTimestamp', uselist=False)
    execution = relationship('DashboardExecution', uselist=False)
    usage = relationship('DashboardUsage', order_by='DashboardUsage.user_rk', backref='dashboard')
    readers = relationship('User', order_by='User.rk', secondary='dashboard_usage', backref='dashboards_read')
    owners = relationship('User', order_by='User.rk', secondary='dashboard_owner', backref='dashboards_owned')
    followers = relationship('User', order_by='User.rk', secondary='dashboard_follower', backref='dashboards_followed')
    tables = relationship('Table', order_by='Table.rk', secondary='dashboard_table', backref='dashboards')
    tags = relationship('Tag', order_by='Tag.rk', secondary='dashboard_tag')
    badges = relationship('Badge', order_by='Badge.rk', secondary='dashboard_badge')
    queries = relationship('DashboardQuery', order_by='DashboardQuery.rk')


class DashboardDescription(Base):
    """
    Description model for dashboard.
    """
    __tablename__ = 'dashboard_description'

    rk = Column(String(KEY_LEN), primary_key=True)
    description = Column(Text)
    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class DashboardBadge(Base):
    """
    Association model for dashboard-badge.
    """
    __tablename__ = 'dashboard_badge'

    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), primary_key=True)
    badge_rk = Column(String(KEY_LEN), ForeignKey('badge.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class DashboardUsage(Base):
    """
    Association model for dashboard-reader.
    """
    __tablename__ = 'dashboard_usage'

    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), primary_key=True)
    user_rk = Column(String(KEY_LEN), ForeignKey('users.rk', ondelete='cascade'), primary_key=True)
    read_count = Column(Integer, nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class DashboardOwner(Base):
    """
    Association model for dashboard-owner.
    """
    __tablename__ = 'dashboard_owner'

    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), primary_key=True)
    user_rk = Column(String(KEY_LEN), ForeignKey('users.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class DashboardFollower(Base):
    """
    Association model for dashboard-follower.
    """
    __tablename__ = 'dashboard_follower'

    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), primary_key=True)
    user_rk = Column(String(KEY_LEN), ForeignKey('users.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class DashboardTable(Base):
    """
    Association model for dashboard-table.
    """
    __tablename__ = 'dashboard_table'

    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), primary_key=True)
    table_rk = Column(String(KEY_LEN), ForeignKey('table_metadata.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class DashboardTag(Base):
    """
    Association model for dashboard-tag
    """
    __tablename__ = 'dashboard_tag'

    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), primary_key=True)
    tag_rk = Column(String(KEY_LEN), ForeignKey('tag.rk', ondelete='cascade'), primary_key=True)
    published_tag = Column(String(PUBLISHED_TAG_LEN))
    publisher_last_updated_epoch_ms = Column(BigInteger)


class DashboardTimestamp(Base):
    """
    Last_updated_timestamp model for dashboard.
    """
    __tablename__ = 'dashboard_timestamp'

    rk = Column(String(KEY_LEN), primary_key=True)
    timestamp = Column(Integer, nullable=False)
    name = Column(String(NAME_LEN), nullable=False)
    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class DashboardCluster(Base):
    """
    Cluster model for dashboard.
    """
    __tablename__ = 'dashboard_cluster'

    rk = Column(String(KEY_LEN), primary_key=True)
    name = Column(String(NAME_LEN), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class DashboardGroup(Base):
    """
    Dashboard_group model.
    """
    __tablename__ = 'dashboard_group'

    rk = Column(String(KEY_LEN), primary_key=True)
    name = Column(String(NAME_LEN), nullable=False)
    dashboard_group_url = Column(String(URL_LEN))
    cluster_rk = Column(String(KEY_LEN), ForeignKey('dashboard_cluster.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

    cluster = relationship('DashboardCluster')
    description = relationship('DashboardGroupDescription', uselist=False)


class DashboardGroupDescription(Base):
    """
    Description model for dashboard group.
    """
    __tablename__ = 'dashboard_group_description'

    rk = Column(String(KEY_LEN), primary_key=True)
    description = Column(Text)
    dashboard_group_rk = Column(String(KEY_LEN), ForeignKey('dashboard_group.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class DashboardExecution(Base):
    """
    Dashboard execution model.
    """
    __tablename__ = 'dashboard_execution'

    rk = Column(String(KEY_LEN), primary_key=True)
    timestamp = Column(Integer, nullable=False)
    state = Column(String(16), nullable=False)
    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)


class DashboardQuery(Base):
    """
    Dashboard query model.
    """
    __tablename__ = 'dashboard_query'

    rk = Column(String(KEY_LEN), primary_key=True)
    id = Column(String(32), nullable=False)
    name = Column(String(NAME_LEN), nullable=False)
    url = Column(String(URL_LEN))
    query_text = Column(Text)
    dashboard_rk = Column(String(KEY_LEN), ForeignKey('dashboard.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

    charts = relationship('DashboardChart', order_by='DashboardChart.rk')


class DashboardChart(Base):
    """
    Dashboard chart model.
    """
    __tablename__ = 'dashboard_chart'

    rk = Column(String(KEY_LEN), primary_key=True)
    id = Column(String(32), nullable=False)
    name = Column(String(NAME_LEN))
    type = Column(String(32))
    url = Column(String(URL_LEN))
    query_rk = Column(String(KEY_LEN), ForeignKey('dashboard_query.rk', ondelete='cascade'), nullable=False)
    published_tag = Column(String(PUBLISHED_TAG_LEN), nullable=False)
    publisher_last_updated_epoch_ms = Column(BigInteger, nullable=False)

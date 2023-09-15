# amundsenrds
[![PyPI version](https://badge.fury.io/py/amundsen-rds.svg)](https://badge.fury.io/py/amundsen-rds)
[![License](https://img.shields.io/:license-Apache%202-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://join.slack.com/t/amundsenworkspace/shared_invite/zt-s8f3srsx-_0b6_WA5~eYGrv_g63L2ng)

Amundsenrds contains ORM models to support relational database as metadata backend store in Amundsen.
The schema in ORM models follows the logic of [databuilder models](https://github.com/amundsen-io/amundsen/tree/main/databuilder/databuilder/models).
Amundsenrds will be used in [databuilder](https://github.com/amundsen-io/amundsen/tree/main/databuilder) and [metadata](https://github.com/amundsen-io/amundsen/tree/main/metadata) for metadata storage and retrieval with relational databases.

## Model overview
```mermaid
erDiagram  
Database ||--o{ Cluster : "" 
Cluster ||--o{ Schema : "" 
Schema ||--o{ Table : ""
Schema ||--o| SchemaDescription : ""
Schema ||--o{ SchemaProgrammaticDescription : ""
Table ||--o| ApplicationTable : ""
Application ||--o{ ApplicationTable : ""
Table ||--o{ TableLineage : ""
TableLineage ||--|{ Table : ""
Table ||--o| TableDescription : ""
Table ||--o{ TableProgrammaticDescription : ""
Table ||--o| TableTimestamp : ""
Table ||--o{ TableTag : ""
Table ||--o{ TableBadge : ""
Badge ||--o{ TableBadge : ""
Table ||--o{ TableOwner : ""
Table ||--o{ TableFollower : ""
Table ||--o{ TableWatermark : ""
Table ||--o| TableSource : ""
Table ||--o{ TableUsage : ""
Table ||--|{ TableColumn : ""
TableColumn ||--o| ColumnDescription : ""
TableColumn ||--o{ ColumnStat : ""
TableColumn ||--o{ ColumnLineage : ""
ColumnLineage ||--|{ TableColumn : ""
TableColumn ||--o{ ColumnBadge : ""
Badge ||--o{ ColumnBadge : ""
DashboardCluster ||--o{ DashboardGroup : ""
DashboardGroup ||--o{ Dashboard : ""
Dashboard ||--o{ DashboardBadge : ""
Badge ||--o{ DashboardBadge : ""
Dashboard ||--o| DashboardDescription : ""
Dashboard ||--o| DashboardTimestamp : ""
Dashboard ||--o{ DashboardTag : ""
Dashboard ||--o{ DashboardOwner : ""
Dashboard ||--o{ DashboardFollower : ""
Dashboard ||--o{ DashboardUsage : ""
Dashboard ||--o{ DashboardTable : ""
Table ||--o{ DashboardTable : ""
Dashboard ||--o{ DashboardExecution : ""
Dashboard ||--o{ DashboardQuery : ""
DashboardQuery ||--o{ DashboardChart : ""
Tag ||--o{ DashboardTag : ""
DashboardGroup ||--o| DashboardGroupDescription : ""
User ||--o{ TableOwner : ""
User ||--o{ TableFollower : ""
User ||--o{ TableUsage : ""
User ||--o{ DashboardOwner : ""
User ||--o{ DashboardFollower : ""
User ||--o{ DashboardUsage : ""
UpdatedTimestamp
```

## Requirements
- Python: >= 3.6
- MySQL: 5.7, 8
  
**Note**: amundsen-rds(version >= 0.0.8) comes with SQLAlchemy ORM features supported only in MySQL 8 in the correlated amundsen [metadata](https://github.com/amundsen-io/amundsen/tree/main/metadata).
## Instructions to configure venv
- In the terminal window, change directory to [amundsenrds](https://github.com/amundsen-io/amundsenrds).
```
$ python3 -m venv venv
$ source venv/bin/activate  
$ pip3 install -r requirements.txt
$ python3 setup.py install
```

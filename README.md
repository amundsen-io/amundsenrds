# amundsenrds
[![PyPI version](https://badge.fury.io/py/amundsen-rds.svg)](https://badge.fury.io/py/amundsen-rds)
[![License](https://img.shields.io/:license-Apache%202-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://amundsenworkspace.slack.com/join/shared_invite/enQtNTk2ODQ1NDU1NDI0LTc3MzQyZmM0ZGFjNzg5MzY1MzJlZTg4YjQ4YTU0ZmMxYWU2MmVlMzhhY2MzMTc1MDg0MzRjNTA4MzRkMGE0Nzk)

Amundsenrds contains ORM models to support relational database as metadata backend store in Amundsen.
The schema in ORM models follows the logic of [databuilder models](https://github.com/amundsen-io/amundsendatabuilder/tree/master/databuilder/models).
Amundsenrds will be used in [databuilder](https://github.com/amundsen-io/amundsendatabuilder) and [metadatalibrary](https://github.com/amundsen-io/amundsenmetadatalibrary) for metadata storage and retrieval with relational databases.

## Requirements
- Python: >= 3.6
- MySQL: 5.7, 8
  
**Note**: amundsen-rds(version >= 0.0.8) comes with SQLAlchemy ORM features supported only in MySQL 8 in the correlated amundsen [metadata-service](https://github.com/amundsen-io/amundsen/tree/main/metadata).
## Instructions to configure venv
- In the terminal window, change directory to [amundsen-rds](https://github.com/amundsen-io/amundsenrds]).
```
$ python3 -m venv venv
$ source venv/bin/activate  
$ pip3 install -r requirements.txt
$ python3 setup.py install
```

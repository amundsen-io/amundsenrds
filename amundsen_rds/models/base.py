# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

KEY_LEN = 1024
NAME_LEN = 256
URL_LEN = 2048
PUBLISHED_TAG_LEN = 128

INDEX_KEY_COLLATION_ARGS = {
    'collation': 'latin1_general_cs'
}

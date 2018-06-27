# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# KPIit is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Common pytest fixtures and plugins."""

import json

import pytest

from kpiit.metrics.records import RecordsMetric
from kpiit.metrics.zenodo import ZenodoRecordsMetric
from kpiit.models import MetricInstance
from kpiit.providers import URLProvider


@pytest.fixture
def records_metric():
    """Fixture for records metric."""
    return RecordsMetric()


@pytest.fixture
def url_provider(records_metric):
    """URL provider fixture."""
    return URLProvider(records_metric, ZenodoRecordsMetric.URL)


@pytest.fixture
def zenodo_records():
    """Fixture for Zenodo records metric instance."""
    return ZenodoRecordsMetric()


@pytest.fixture
def zenodo_records_json():
    """Load JSON content from Zenodo records file."""
    data = None
    with open('tests/data/zenodo_records.json', 'r') as f:
        data = f.read()
    return data

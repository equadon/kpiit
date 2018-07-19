# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# KPIit is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

FROM cern/cc7-base:20180516

RUN yum update -y && yum upgrade -y
RUN yum install -y git curl python34-pip cern-get-sso-cookie
RUN pip3 install --upgrade setuptools wheel pip

# Install KPIit
ENV WORKING_DIR=/opt/kpiit

# copy everything inside /src
RUN mkdir -p ${WORKING_DIR}/src
COPY ./ ${WORKING_DIR}/src
WORKDIR ${WORKING_DIR}/src

# Install
RUN ./scripts/bootstrap

# Set folder permissions
RUN chgrp -R 0 ${WORKING_DIR} && \
    chmod -R g=u ${WORKING_DIR}

RUN useradd kpiit --uid 1000 --gid 0 && \
    chown -R kpiit:root ${WORKING_DIR}
USER 1000

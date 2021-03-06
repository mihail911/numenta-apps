# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2015, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)


import os
from pkg_resources import get_distribution

from nta.utils import logging_support_raw



logging_support = logging_support_raw

distribution = get_distribution(__name__)
TAURUS_MONITORS_HOME = os.path.abspath(distribution.location)

CONF_DIR = os.environ.get("TAURUS_MONITORS_DB_CONFIG_PATH")
if CONF_DIR is None:
  CONF_DIR = os.path.join(TAURUS_MONITORS_HOME, "conf")

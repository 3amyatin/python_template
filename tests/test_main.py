# import pytest # no need if pytest defined in PyCharm project, no need if in conftest.py

from zielezin import ExasolConnection
from config import _config as config

# global fixtures are automatically read from conftest.py

# local fixtures 
@pytest.fixture
def exasol():
  return ExasolConnection(**config.connect['dev-sqlalchemy'])


def test_1(exasol):
  stmt = exasol.execute_lua_script('dwh_out.DWH_UTILITY_COPYZUSATZINFOMONAT', -1, 'FAKT_ZUSATZINFO_AGT', dryrun=True)
  assert stmt == "execute script dwh_out.DWH_UTILITY_COPYZUSATZINFOMONAT (-1, 'FAKT_ZUSATZINFO_AGT') with output;"


def test_dva(exasol):
  stmt = exasol.execute_lua_script('dwh_out.DWH_UTILITY_COPYDWTZUSATZINFOMONAT','-1', dryrun=True)
  assert stmt == "execute script dwh_out.DWH_UTILITY_COPYDWTZUSATZINFOMONAT ('-1') with output;"

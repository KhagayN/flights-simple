# Databricks notebook source
# MAGIC %pip install pytest
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import pytest
import os
import sys

def run_pytest(pytest_path):
  # Skip writing pyc files on a readonly filesystem.
  sys.dont_write_bytecode = True

  retcode = pytest.main([pytest_path, "-p", "no:cacheprovider", "-p", "no:warnings"])

  # Fail the cell execution if we have any test failures.
  assert retcode == 0, 'The pytest invocation failed. See the log above for details.'

# COMMAND ----------

run_pytest("unit_transforms/test_flight_transforms.py")

# COMMAND ----------

run_pytest("unit_utils/test_flight_utils.py")

# COMMAND ----------

# sys.path

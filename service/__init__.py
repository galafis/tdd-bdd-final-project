######################################################################
# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

"""
Package: service

Package for the application models and service routes
This module creates and configures the Flask app and sets up the logging
and SQL database
"""
import sys
import os # Added for checking environment variables
from flask import Flask
from service import config
from service.common import log_handlers

# NOTE: Do not change the order of this code
# The Flask app must be created
# BEFORE you import modules that depend on it !!!

# Create the Flask aoo
app = Flask(__name__)  # pylint: disable=invalid-name

# Load Configurations
app.config.from_object(config)

# Dependencies require we import the routes AFTER the Flask app is created
# pylint: disable=wrong-import-position, wrong-import-order, cyclic-import
from service import routes, models        # noqa: F401, E402
from service.common import error_handlers, cli_commands  # noqa: F401, E402

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  P R O D U C T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

# Conditional DB initialization to prevent issues during test collection
# The `app.config['TESTING']` might not be set yet when pytest imports __init__.py
# Tests should handle their own DB setup via app.config["TESTING"] = True and calling init_db.

# We check if the execution is part of a test run by looking for pytest specific env vars
# or if FLASK_ENV is set to 'test'. This is a heuristic.
# A more robust solution might involve a create_app() factory pattern.

is_testing_environment = app.config.get("TESTING", False) or \
                         os.environ.get("PYTEST_CURRENT_TEST") is not None or \
                         os.environ.get("FLASK_ENV") == "test"

if not is_testing_environment:
    app.logger.info("Attempting to initialize DB for non-testing environment.")
    try:
        models.init_db(app)  # make our sqlalchemy tables
        app.logger.info("Database initialized successfully for non-testing environment.")
    except Exception as error:  # pylint: disable=broad-except
        app.logger.critical("DB Init Error in non-testing env: %s. Application might not function correctly.", error)
        # The sys.exit(4) is problematic for test collection. Gunicorn should handle worker death.
        # If running under Gunicorn (common for production), it expects exit code 4 to stop spawning.
        # We only exit if we are reasonably sure it's a Gunicorn-like environment and not a test/dev run.
        if "gunicorn" in sys.argv[0] or os.environ.get("SERVER_SOFTWARE", "").startswith("gunicorn"):
            app.logger.info("Exiting due to DB init error in Gunicorn environment.")
            sys.exit(4)
else:
    app.logger.info("Skipping global DB initialization in testing environment.")

app.logger.info("Service initialized!")


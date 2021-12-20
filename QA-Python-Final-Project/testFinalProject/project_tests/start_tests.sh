#!/bin/bash

cd myapp_test/tests

pytest -s -l -v "${TESTS_PATH}" -n "${THREADS:-2}" --alluredir /tmp/allure
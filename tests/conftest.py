import os
import typing

import pytest
from dotenv import load_dotenv

TEST_ENV_FILE = ".env.test"

load_dotenv(TEST_ENV_FILE)


@typing.no_type_check
@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return [
        os.path.join(str(pytestconfig.rootdir), "docker-compose.yaml"),
        os.path.join(str(pytestconfig.rootdir), "docker-compose.test.yaml"),
    ]


@typing.no_type_check
@pytest.fixture(scope="session")
def docker_compose_command(pytestconfig):
    return f"docker compose --env-file {TEST_ENV_FILE}"

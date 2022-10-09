import os
import typing

import pytest


@typing.no_type_check
@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "docker-compose.dev.yaml")

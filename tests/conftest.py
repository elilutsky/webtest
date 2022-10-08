import os
import typing

import pytest


def get_free_port() -> int:
    import socket

    sock = socket.socket()
    sock.bind(("", 0))
    return int(sock.getsockname()[1])


@typing.no_type_check
@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "docker-compose.dev.yaml")


@typing.no_type_check
@pytest.fixture(scope="session")
def docker_compose_command(pytestconfig):
    """
    Prepend environment variables for docker-compose
    """
    return f"MONGODB_DEV_PORT={get_free_port()} docker-compose"

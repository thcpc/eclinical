import pytest
from eclinical import Environment
from service.ffe_ddd_service import FfeDddService


@pytest.fixture 
def ffe_ddd_service(ef, st):
	return FfeDddService(Environment(envir=st, file_path=ef))


from service.rr_rr_service import RrRrService


@pytest.fixture 
def rr_rr_service(ef, st):
	return RrRrService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.test_service_service import TestServiceService


@pytest.fixture
def test_service_service(ef, st):
	return TestServiceService(Environment(envir=st, file_path=ef))


from .services.tt_service import TtService


@pytest.fixture
def tt_service(ef, st):
	return TtService(Environment(envir=st, file_path=ef))



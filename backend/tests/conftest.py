import os, tempfile
_db_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False); _db_file.close()
os.environ["DATABASE_URL"] = f"sqlite:///{_db_file.name}"
os.environ["CORS_ORIGINS"] = "http://testserver"
import pytest
from fastapi.testclient import TestClient
from app.db.session import Base, engine
from app.main import app
@pytest.fixture()
def client():
    Base.metadata.drop_all(bind=engine); Base.metadata.create_all(bind=engine)
    with TestClient(app) as test_client: yield test_client

from httpx import AsyncClient
import pytest
from bin.main import app  # Убедитесь, что main указывает на файл, где находится ваш FastAPI приложение

@pytest.mark.asyncio
async def test_add():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/add/", json={"number1": 5, "number2": 3})
        assert response.status_code == 200
        assert response.json() == {"result": 8}

@pytest.mark.asyncio
async def test_subtract():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/subtract/", json={"number1": 10, "number2": 5})
        assert response.status_code == 200
        assert response.json() == {"result": 5}

@pytest.mark.asyncio
async def test_multiply():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/multiply/", json={"number1": 4, "number2": 2})
        assert response.status_code == 200
        assert response.json() == {"result": 8}

@pytest.mark.asyncio
async def test_divide():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/divide/", json={"number1": 10, "number2": 2})
        assert response.status_code == 200
        assert response.json() == {"result": 5}

@pytest.mark.asyncio
async def test_divide_by_zero():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/divide/", json={"number1": 10, "number2": 0})
        assert response.status_code == 200
        assert response.json() == {"error": "Division by zero is not allowed"}

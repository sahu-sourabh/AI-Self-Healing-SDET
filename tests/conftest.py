import pytest
import asyncio
import os

@pytest.fixture(scope="session")
def event_loop():
    """Overrides pytest-asyncio's loop to be Windows-friendly."""
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
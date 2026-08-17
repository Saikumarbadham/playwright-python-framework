import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_patch_user():

    async with async_playwright() as playwright:

        request = await playwright.request.new_context(
            base_url="https://jsonplaceholder.typicode.com"
        )

        response = await request.patch(
            "/users/1",
            data={
                "name": "Saik",
                "role": "QA Engineers"
            }
        )

        assert response.status == 200

        response_body = await response.json()

        print(response_body)

        await request.dispose()
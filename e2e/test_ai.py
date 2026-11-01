
from playwright.async_api import Playwright


def test_url(playwright:Playwright):
    base ="url"
    request =playwright.request.new_context
    response = request.post(base,data={
        "name":"sai",
        "id":23
    })
    res=response
    data=response.json
    response.stausOk()
    assert(res).to_be(200)
    assert data["name"]=="sai"
    dat=response.json
    assert dat["id"]==23
    request.dispose()


    request =playwright.request.new_context
    respose = request.delete("")
    


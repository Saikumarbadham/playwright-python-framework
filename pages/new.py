from playwright.sync_api import Page

class dude:
    def __init__(self,page:Page):
        self.page = page

        self.df=page.locator("")
        self.hk=page.locator("huh")

    def testlo(self,name):
        self.df(name)



class BaseController:
    def __init__(self):
        self.session = session

    async def __aenter__(self):
        await self.session.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.commit()

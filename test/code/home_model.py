from BDD_Approach_Learning.test.code.base_model import BaseModel


class HomeModel(BaseModel):
    def __init__(self, context):
        BaseModel.__init__(self, context.browser)
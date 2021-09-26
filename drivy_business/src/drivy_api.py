from pydantic import BaseModel


class DrivyAPI(BaseModel):
    def get_estimated_earning(self, brand, model, year, km):
        pass

    def get_models(self, brand):
        pass


    pass

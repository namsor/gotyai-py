from pydantic import BaseModel, Field


class CreateClassifierRequest(BaseModel):
    classifier_name: str = Field(alias='classifierName')
    categories: list[str]


class FitModelByOneRequest(BaseModel):
    x: dict
    y: str


class FitModelByManyRequest(BaseModel):
    rows: list[FitModelByOneRequest]


class PredictByOneRequest(BaseModel):
    x: dict


class PredictByManyRequest(BaseModel):
    rows: list[PredictByOneRequest]

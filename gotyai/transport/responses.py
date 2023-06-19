from pydantic import BaseModel, Field


class CreateClassifierResponse(BaseModel):
    categories: list[str]
    classifier_name: str = Field(alias='classifierName')
    uuid: str
    user_id: str = Field(alias='userId')
    created_date_time: int = Field(alias='createdDateTime')


class PredictResponse(BaseModel):
    x: dict
    y: str
    score: float
    proba: float

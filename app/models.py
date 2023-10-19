import uuid
from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel

class BaseModel(SQLModel):
    def fill(self, params=[]):
        for item, key in params:
            self[key] = item

class Operation(BaseModel, table=True):
    id: Optional[str] = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str

    def __init__():
        pass

class Asset(BaseModel, table=True):
    id: Optional[str] = Field(default_factory=uuid.uuid4, primary_key=True)
    operation_id: int = Field(foreign_key='operation.id')
    name: str
    bot: List['Bot'] = Relationship(back_populates='asset')


    def __init__():
        pass

class Bot(BaseModel, table=True):
    id: Optional[str] = Field(default_factory=uuid.uuid4, primary_key=True)
    config: str
    status: bool = False
    asset_id: int = Field(foreign_key='asset.id')
    asset: Optional[Asset] = Relationship(back_populates='bot')




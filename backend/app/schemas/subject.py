from pydantic import BaseModel

class subjectResponse(BaseModel):
    id:int
    name:str
    Description:str


from pydantic import BaseModel 

class FiltersResponse(BaseModel):

    markets: dict[int,str]
    channels: dict[int,str]
    subchannel: dict[int,str]
    units: dict[str,str]

    
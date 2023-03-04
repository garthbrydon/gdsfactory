from pydantic import BaseModel

###### Reticle start


class ReticleBase(BaseModel):
    name: str
    description: str
    position: str
    size: str


class ReticleCreate(ReticleBase):
    name: str
    description: str
    position: str
    size: str
    wafer_id: int


class ReticleUpdate(ReticleBase):
    name: str
    description: str


# Properties shared by models stored in DB
class ReticleInDBBase(ReticleBase):
    id: int
    wafer_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Reticle(ReticleInDBBase):
    pass


# Properties properties stored in DB
class ReticleInDB(ReticleInDBBase):
    pass


###### Reticle end

###### Wafer start


class WaferBase(BaseModel):
    name: str
    serial_number: str
    description: str


# Properties to receive via API on creation
class WaferCreate(WaferBase):
    ...


# Properties to receive via API on update
class WaferUpdate(WaferBase):
    ...


class WaferInDBBase(WaferBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Wafer(WaferInDBBase):
    reticles: List[Reticle]


###### Reticle end

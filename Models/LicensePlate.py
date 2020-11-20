from pydantic import BaseModel
from typing import Optional
from typing import List
from fastapi import FastAPI


class LicensePlate(BaseModel):
    camera_id: Optional[str] = None
    filename: Optional[str] = None
    timestamp: Optional[str] = None
    plate: Optional[str] = None

from pydantic import BaseModel
from typing import Optional
from typing import List
from fastapi import FastAPI


class LicensePlate(BaseModel):
    inserted_id: Optional[str] = None
    camera_id: Optional[str] = None
    filename: Optional[str] = None
    timestamp: Optional[str] = None
    plate: Optional[str] = None
    dscore: Optional[float] = None
    score: Optional[float] = None
    vehicle_type: Optional[str] = None
    vehicle_type_score: Optional[float] = None


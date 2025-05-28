
from matplotlib.pyplot import cla
from numpy import average
from pydantic import BaseModel, Field, field_validator, HttpUrl
from typing import Optional


class DrugsReview(BaseModel):
    excellent: float = Field(..., ge=0, le=100, description="Ti le danh gia xuat sac")
    average: float = Field(..., ge=0, le=100, description="Ti le danh gia trung binh")
    poor: float = Field(..., ge=0, le=100, description="Ti le danh gia kem")

    def __init__(self, **data):
        super().__init__(**data)
        
        self.rating = round(
            (self.excellent * 5 + self.average * 3 + self.poor * 1) / 100, 2
        )

class Drugs(BaseModel):
    id: Optional[int] = Field(None, description="ID duy nhat cua thuoc")
    
    medicine_name: str = Field(...,min_length=1, max_length=200, description="Ten thuoc")
    composition: str = Field(...,min_length=1, description="Thanh phan hoat chat")
    uses: str = Field(...,min_length=1, description="Cong dung")
    side_effect: Optional[str] = Field(None, description="Tac dung phu")
    image_url: Optional[str] = Field(None, description="URL hinh anh")
    manufacturer: Optional[str] = Field(None, description="Nha san xuat")
    
    reviews: Optional[str] = Field(None, description="Thong tin danh gia")
    
    @field_validator('medicine_name')
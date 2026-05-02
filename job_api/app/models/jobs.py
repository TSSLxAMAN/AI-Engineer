from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date


class JobPosting(BaseModel):
    id: int
    title: str = Field(..., min_length=3)
    description: str = Field(..., min_length=20)

    company_name: str
    location: str

    salary_min: Optional[float] = Field(None, ge=0)
    salary_max: Optional[float] = Field(None, ge=0)

    skills: List[str] = []
    experience_required: int = Field(..., ge=0)

    posted_date: date = Field(default_factory=date.today)

    contact_email: EmailStr
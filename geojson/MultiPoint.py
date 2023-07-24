"""Microjson. Auto-generated by datamodel-codegen"""

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Type44(Enum):
    multi_point = 'MultiPoint'


class GeojsonMultipoint(BaseModel):
    type: Type44
    coordinates: List[List[float]]
    bbox: Optional[List[float]] = Field(None, min_items=4)

"""Microjson. Auto-generated by datamodel-codegen"""

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Type42(Enum):
    polygon = 'Polygon'


class Coordinate24(BaseModel):
    __root__: List[Any]


class GeojsonPolygon(BaseModel):
    type: Type42
    coordinates: List[List[Coordinate24]]
    bbox: Optional[List[float]] = Field(None, min_items=4)

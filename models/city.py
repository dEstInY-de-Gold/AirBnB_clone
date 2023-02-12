#!/usr/bin/env python3
"""class inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class city inheriting from BaseModel
    """

    state_id = ""
    name = ""

#!/usr/bin/env python3
"""class user"""

from models.base_model import BaseModel


class User(BaseModel):
    """class user inheriting from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

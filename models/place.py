#!/usr/bin/env python3
"""class place inheriting from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """class place inheriting from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

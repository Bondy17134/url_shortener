"""
schemas.py
-> Implements "type hinting" to veriffy that the request and the response match the data types defined
"""

from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str

class URL(URLBase):
    is_active: bool
    click: int

    class Config:
        """
            ORM Stands for: 
                Object-Relational Mapping, providing the convenience of 
                interacting with database using an object-oriented approach
        """
        orm_mode = True # telling pydantic to work with a database model

class URLInfo(URL):
    url: str
    admin_url: str

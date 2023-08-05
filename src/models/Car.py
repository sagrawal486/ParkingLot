from pydantic import BaseModel, Field
from typing import Optional

class Car(BaseModel):
    registrationNumber: str
    color: str
    
    def __init__(self, registrationNumber: str, color: str):
        super().__init__(registrationNumber=registrationNumber, color=color)

    def __str__(self):
        return f"Car[" + \
        "registrationNumber='" + self.registrationNumber + '\'' + \
        ", color='" + self.color + \
        '}'

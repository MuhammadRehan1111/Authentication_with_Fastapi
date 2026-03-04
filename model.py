
from typing import Optional
from datetime import datetime

class User:
    def __init__(
        self,
        id:str,
        name:str,
        email:email,
        hasded_password:str,
        created_at:Optional[datetime]=None

    ):


        self.id=id,
        self.name=name,
        self.email=email,
        self.hasded_password=hasded_password,
        self.created_at=created_at or datetime.utcnow()



class Analysis:
    def __init__(
        self,
        id: str,
        user_id: str,
        original_text: str,
        result: dict,
        created_at: Optional[datetime] = None
    ):
        self.id = id
        self.user_id = user_id
        self.original_text = original_text
        self.result = result
        self.created_at = created_at or datetime.utcnow()
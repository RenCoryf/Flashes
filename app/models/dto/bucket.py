from typing import Annotated, Optional

from pydantic import BaseModel, Field
from sqlalchemy.dialects.postgresql.base import UUID

uni_annotated = Annotated[str, Field(min_length=2, max_length=255)]
name_annotated = Annotated[str, Field(min_length=2, max_length=100)]
theme_annotated = Annotated[str, Field(min_length=2, max_length=255)]

course_annotated = Annotated[int, Field(ge=1, le=6)]


class BucketDTO(BaseModel):
    name: name_annotated
    theme: Optional[theme_annotated] = None
    user_id: UUID
    course: int
    uni: uni_annotated
    course_amount: course_annotated

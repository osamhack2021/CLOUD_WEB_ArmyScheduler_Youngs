from typing import Optional

from pydantic import BaseModel, Field


class EventModel(BaseModel):
    event_id: int = Field(...)
    user_id: list = Field(...)
    event_title: str = Field(...)
    event_type: int = Field(...)
    work_id: int = Field(...)
    tags: list = Field(...)
    event_color: str = Field(...)
    event_start_date: dict = Field(...)
    event_start_time: str = Field(...)
    event_end_date: dict = Field(...)
    event_end_time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "event_id": 1,
                "user_id": ["1", "2"],
                "event_title": "CCTV",
                "event_type": 0,
                "work_id": 2,
                "tags": [
                {
                    "tag_title": "CCTV",        # 근무명
                    "tag_color": "green",       # green
                },
                {
                    "tag_title": "야간근무",    # 근무시간명
                    "tag_color": "orange",      # orange
                },
                {
                    "tag_title": "3명",         # 근무인원
                    "tag_color": "blue",        # blue
                }],
                "event_color": "deep-purple",
                "event_start_date" : {
                    "date": 1633046400000,
                    "date_string": "2021-10-01" ,
                    "isHoliday": True
                },
                "event_start_time" : "22:00",
                "event_end_date" : {
                    "date": 1633058200000,
                    "date_string": "2021-10-12",
                    "isHoliday": False
                },
                "event_end_time" : "24:00"
            }
        }


class UpdateEventModel(BaseModel):
    event_id: Optional[int]
    user_id: Optional[list]
    event_title: Optional[str]
    event_type: Optional[int]
    work_id: Optional[int]
    tags: Optional[list]
    event_color: Optional[str]
    event_start_date: Optional[dict]
    event_start_time: Optional[str]
    event_end_date: Optional[dict]
    event_end_time: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "event_id": 1,
                "user_id": ["1", "2"],
                "event_title": "CCTV",
                "event_type": 0,
                "work_id": 2,
                "tags": [
                {
                    "tag_title": "CCTV",        # 근무명
                    "tag_color": "green",       # green
                },
                {
                    "tag_title": "야간근무",    # 근무시간명
                    "tag_color": "orange",      # orange
                },
                {
                    "tag_title": "3명",         # 근무인원
                    "tag_color": "blue",        # blue
                }],
                "event_color": "deep-purple",
                "event_start_date" : {
                    "date": 1633046400000,
                    "date_string": "2021-10-01" ,
                    "isHoliday": True
                },
                "event_start_time" : "22:00",
                "event_end_date" : {
                    "date": 1633058200000,
                    "date_string": "2021-10-12",
                    "isHoliday": False
                },
                "event_end_time" : "24:00"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }

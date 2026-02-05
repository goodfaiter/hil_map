from typing import Literal, Union
from pydantic import BaseModel, Field

class Potato(BaseModel):
    name: Literal["potato"] = "potato"


class Knife(BaseModel):
    name: Literal["knife"] = "knife"


class Peeler(BaseModel):
    name: Literal["peeler"] = "peeler"


class Move(BaseModel):
    name: Literal["move"] = "move"
    object: Union[Potato, Knife, Peeler] = Field(description="Object to move.")


class Hold(BaseModel):
    name: Literal["hold"] = "hold"
    object: Union[Potato, Knife, Peeler] = Field(description="Object to hold.")


class Rotate(BaseModel):
    name: Literal["rotate"] = "rotate"
    object: Union[Potato, Knife, Peeler] = Field(description="Object to rotate.")


class Peel(BaseModel):
    name: Literal["peel"] = "peel"
    object: Union[Potato] = Field(description="Object to peel.")


class Cut(BaseModel):
    name: Literal["cut"] = "cut"
    object: Union[Potato] = Field(description="Object to cut.")    


class Action(BaseModel):
    description: str = Field(description="Description of the action to be performed.")
    action: Union[Move, Hold, Rotate, Peel, Cut] = Field(description="Action to perform.")


class TaskPlan(BaseModel):
    task: str
    plan: list[Action] = Field(description="Step by step plan for the robot to execute the task.")


class HighLevelPlan(BaseModel):
    task: str
    plan: list[str] = Field(description="High level step by step plan for this task.")

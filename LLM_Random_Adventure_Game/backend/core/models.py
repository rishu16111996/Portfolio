from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):
    text: str = Field(description="The text of the option presented to the player")
    nextNode: Dict[str, Any] = Field(description="The next node in the story tree")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="The content or narrative at this node in the story")
    isEnding: bool = Field(description="Indicates if this node is an ending")
    isWinningEnding: bool = Field(description="Indicates if this ending is a winning ending")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="List of options available at this node")


class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM = Field(description="The root node of the story tree")
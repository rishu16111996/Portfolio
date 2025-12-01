from sqlalchemy.orm import Session

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from core.prompts import STORY_PROMPT
from models.story import Story, StoryNode
from core.models import StoryLLMResponse, StoryNodeLLM
from dotenv import load_dotenv

load_dotenv()


class StoryGenerator:

    @classmethod
    def _get_llm(cls):
        return ChatOpenAI(model="gpt-4.1-mini")
    
    @classmethod
    def generate_story(cls, db: Session, session_id: str, theme: str = "fantasy") -> Story:
        llm = cls._get_llm()
        story_parser = PydanticOutputParser(pydantic_object=StoryLLMResponse)

        messages = [
            ("system", STORY_PROMPT),
            ("human", f"Create the story with this theme: {theme}\n\n{story_parser.get_format_instructions()}")
        ]

        raw_response = llm.invoke(messages)

        response_text = getattr(raw_response, "content", raw_response)

        story_structure = story_parser.parse(response_text)

        story_db = Story(title=story_structure.title, session_id=session_id)
        db.add(story_db)
        db.flush()

        root_node = story_structure.rootNode
        if isinstance(root_node, dict):
            root_node = StoryNodeLLM.model_validate(root_node)

        cls._process_story_node(db, story_db.id, root_node, is_root=True)

        db.commit()
        return story_db
    

    @classmethod
    def _process_story_node(cls, db: Session, story_id: int, node_data: StoryNodeLLM, is_root: bool = False) -> StoryNode:
        node = StoryNode(
            story_id=story_id,
            content=node_data.content,
            is_root=is_root,
            is_ending=node_data.isEnding,
            is_winning_ending=node_data.isWinningEnding,
            options=[]
        )
        db.add(node)
        db.flush()

        if not node.is_ending and node_data.options:
            options_list = []
            for options_data in node_data.options:
                next_node = options_data.nextNode

                if isinstance(next_node, dict):
                    next_node = StoryNodeLLM.model_validate(next_node)

                child_node = cls._process_story_node(db, story_id, next_node, is_root=False)

                options_list.append({
                    "text": options_data.text,
                    "node_id": child_node.id
                })

            node.options = options_list

        db.flush()
        return node


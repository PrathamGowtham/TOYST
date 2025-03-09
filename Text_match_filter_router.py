import re

from langflow.custom import Component
from langflow.io import MessageTextInput, MessageInput, Output
from langflow.schema.message import Message

class TextMatchFilter(Component):
    display_name = "Text Match Filter"
    description = "Passes the chat input if the text input matches the reference text."
    icon = "filter"
    name = "TextMatchFilter"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    inputs = [
        MessageTextInput(
            name="text_input",
            display_name="Text Input",
            info="The user input text to check.",
            required=True,
        ),
        MessageTextInput(
            name="reference_text",
            display_name="Reference Text",
            info="The reference text for comparison.",
            required=True,
        ),
        MessageInput(
            name="chat_input",
            display_name="Chat Input",
            info="The message to pass if the texts match.",
            required=True,
        ),
    ]

    outputs = [
        Output(display_name="Filtered Output", name="filtered_output", method="filter_message"),
    ]

    def filter_message(self) -> Message:
        """Passes the chat input if text_input matches reference_text, otherwise returns an empty message."""
        if self.text_input == self.reference_text:
            return self.chat_input
        return Message(content="")

# Register the component
component = TextMatchFilter()

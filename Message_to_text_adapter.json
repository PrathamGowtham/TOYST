from langflow.base.io.chat import ChatComponent
from langflow.schema.message import Message
from langflow.io import Output, MessageInput

class MessageToText(ChatComponent):
    display_name = "Message to Text"
    description = "Converts a message type to a simple text type."
    icon = "FileText"
    name = "MessageToText"

    inputs = [
        MessageInput(
            name="message",
            display_name="Message",
            info="Message object to extract text from."
        )
    ]
    
    outputs = [
        Output(display_name="Text", name="text", method="convert_message_to_text")
    ]
    
    async def convert_message_to_text(self, message: Message) -> str:
        return message.text if message else ""

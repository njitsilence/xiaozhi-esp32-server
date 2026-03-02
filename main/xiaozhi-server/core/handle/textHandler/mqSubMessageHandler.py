import time
from typing import Dict, Any

from core.handle.receiveAudioHandle import startToChat
from core.handle.textMessageHandler import TextMessageHandler
from core.handle.textMessageType import TextMessageType

TAG = __name__


class MqSubTextMessageHandler(TextMessageHandler):
    """MQTT文本消息处理器"""

    @property
    def message_type(self) -> TextMessageType:
        return TextMessageType.MQ_SUB

    async def handle(self, conn, msg_json: Dict[str, Any]) -> None:
        text = msg_json.get("text")
        if not text:
            conn.logger.bind(tag=TAG).error(f"MQTT文本消息缺少text字段: {msg_json}")
            return

        conn.last_activity_time = time.time() * 1000
        await startToChat(conn, text)

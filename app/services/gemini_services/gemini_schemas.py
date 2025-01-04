from google.ai.generativelanguage_v1beta.types import content

generation_config = {
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    properties = {
      "response": content.Schema(
        type = content.Type.STRING
      ),
    },
  ),
  "response_mime_type": "application/json",
}
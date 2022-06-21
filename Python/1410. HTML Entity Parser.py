class Solution:
    def entityParser(self, text: str) -> str:
        dict_ = {"&quot;": '\"', "&apos;": "\'", "&gt;": ">", "&lt;": "<", "&frasl;": "/", "&amp;": "&"}
        for i, j in dict_.items():
            text = text.replace(i, j)
        return text

from cog import BasePredictor, Input, Path, BaseModel, Secret
from markitdown import MarkItDown
from openai import OpenAI

class Predictor(BasePredictor):
    def setup(self) -> None:
        pass

    def predict(
        self,
        doc: Path = Input(
            description="Supports PDF, PPTX, DOCX, XLSX, PNG, JPG, MP3, WAV, HTML, CSV, JSON, XML, and more."
        ),
        openai_api_key: Secret = Input(
            description="(Optional) OpenAI API key",
            default=None
        ),
    ) -> Path:
        md = MarkItDown()
        if openai_api_key:
            client = OpenAI(api_key=openai_api_key)
            md = MarkItDown(mlm_client=client, mlm_model="gpt-4o")
        result = md.convert(doc)
        with open("output.md", "w") as f:
            f.write(result.text_content)
        return Path("output.md")

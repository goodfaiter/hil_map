import os
from openai import OpenAI
from pydantic import BaseModel
import instructor
from instructor import patch, Mode, from_provider


def main():
    client = patch(OpenAI(base_url="https://inference.rcp.epfl.ch/v1"), mode=Mode.JSON)

    class User(BaseModel):
        name: str
        age: int

    # Create structured output
    user = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3.2",
            response_model=User,
            messages=[
                {"role": "user", "content": "Extract: Jason is 25 years old"},
            ],
        )

    print(user)


if __name__ == "__main__":
    main()

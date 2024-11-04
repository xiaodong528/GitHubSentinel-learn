# src/llm.py

import os
from openai import OpenAI

class LLM:
    def __init__(self):
        self.client = OpenAI()

    def generate_daily_report(self, markdown_content, dry_run=False):
        system_prompt = "你是一位专业的技术报告撰写者，擅长总结项目进展。请根据提供的内容，生成一份包含：1）新增功能；2）主要改进；3）修复问题的简报。要求内容简洁明了，条理清晰。"
        user_prompt = f"以下是项目的最新进展：\n\n{markdown_content}"
        if dry_run:
            with open("daily_progress/prompt.txt", "w+") as f:
                f.write(system_prompt + "\n\n" + user_prompt)
            return "DRY RUN"

        print("Before call GPT")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        print("After call GPT")
        print(response)
        return response.choices[0].message.content

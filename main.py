import os
import typer
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_KEY")
)

app = typer.Typer()

@app.command()
def interactive_chat():
    """Interactive CLI tool to chat with ChatGPT"""
    typer.echo(
        "Starting interactive chat with ChatGPT. Type 'exit' to end the session"
    )

    while True:
        prompt = input("User: ")
        if prompt == "exit":
            typer.echo("ChatGPT: Goodbye!")
            break
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role":"user", "content":prompt}]
        )

        typer.echo(f'ChatGPT: {response.choices[0].message.content}')


if __name__ == "__main__":
    app()
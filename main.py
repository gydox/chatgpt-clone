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

    messages = []

    while True:
        prompt = input("User: ")
        messages.append({"role":"user", "content":prompt})
        if prompt == "exit":
            typer.echo("ChatGPT: Goodbye!")
            break
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=messages
        )

        typer.echo(f'ChatGPT: {response.choices[0].message.content}')
        messages.append(response.choices[0].message)



if __name__ == "__main__":
    app()
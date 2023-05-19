import openai
import config
import typer
from rich import print
from rich.table import Table

def main():
    openai.api_key = config.api_key

    print("[bold yellow]API de Chat GPT con Python[/bold yellow]")

    table_01 = Table("Comando", "Descripción")
    table_01.add_row("exit", "Salir de la aplicación")
    table_01.add_row("new", "Crear una nueva conversación")

    print(table_01)

    # Contexto del asistente
    context = {"role": "system",
                        "content": "Eres un asistente muy útil"}
    messages = [context]

    while True:
        content = __prompt()

        if content == "new":
            print("Nueva conversación")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold white]> [/bold white][green]{response_content}[green]")


def __prompt() -> str:
    prompt = typer.prompt("\n ¿Sobre qué quieres hablar?")

    if prompt == "exit":
        exit = typer.confirm("¿Estás seguro de salir?")
        if exit:
            print("Hasta Luego")
            raise typer.Abort()
        
        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)

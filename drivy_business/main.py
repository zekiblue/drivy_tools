import typer

app = typer.Typer()


@app.command()
def get_cars():
    pass


if __name__ == '__main__':
    app()

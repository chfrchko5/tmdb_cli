import requests
import typer
from typing import Annotated, Optional
from movie_data import response_json

app = typer.Typer()

def url_getter(movie_filter):
    return f"https://api.themoviedb.org/3/movie/{movie_filter}?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1OGMxNTA5OGFkN2Y5MjhlOWQ5NjczZGM2OWFm"
                     "NTI4NSIsIm5iZiI6MTc4MDkyOTk0OS4wNCwic3ViIjoiNmEyNmQ1OWQzODI0Njg2NGQyYzc3MDRl"
                     "Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.dajQqyooslnaMmSzAYHPlXDaTg6"
                     "h2lNFsgeDtIvOKDY"
}

@app.command()
def main(
        now_playing: Annotated[
            Optional[bool], typer.Option("--now-playing", help="display currently playing movies")
        ] = False,
        popular: Annotated[
            Optional[bool], typer.Option("--popular", help="display popular movies")
        ] = False,
        top_rated: Annotated[
            Optional[bool], typer.Option("--top-rated", help="display top rated movies")
        ] = False,
        upcoming: Annotated[
            Optional[bool], typer.Option("--upcoming", help="display upcoming movies")
        ] = False
):
    movie_types = ["now_playing", "popular", "top_rated", "upcoming"]

    try:
        if now_playing:
            response = requests.get(url_getter(movie_types[0]), headers=headers)
            response.raise_for_status()
            response_json(response)
        elif popular:
            response = requests.get(url_getter(movie_types[1]), headers=headers)
            response.raise_for_status()
            response_json(response)
        elif top_rated:
            response = requests.get(url_getter(movie_types[2]), headers=headers)
            response.raise_for_status()
            response_json(response)
        elif upcoming:
            response = requests.get(url_getter(movie_types[3]), headers=headers)
            response.raise_for_status()
            response_json(response)
        else:
            typer.echo("Please provide a filter to display movies", err=True)
            print("*** --now-playing")
            print("*** --popular")
            print("*** --top-rated")
            print("*** --upcoming")
            raise typer.Exit(1)
    except requests.exceptions.HTTPError as e:
        typer.echo(f"HTTP error: {e.response.status_code}", err=True)
        raise typer.Exit(1)
    except requests.exceptions.ConnectionError:
        typer.echo("Connection error: check your URL or network", err=True)
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
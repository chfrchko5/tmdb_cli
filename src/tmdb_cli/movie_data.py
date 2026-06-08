def response_json(response):
    data = response.json()

    if "dates" in data:
        print(f"Displaying now playing movies from {data["dates"]["minimum"]}"
              f" to {data["dates"]["maximum"]}")
        print(f"-----------------------------------------------------------")

    for result in data["results"]:
        print(
f"""
--------------------
Movie Title: {result["title"]}
Original Language: {result["original_language"].upper()}
Release Date: {result["release_date"]}
Average Rating: {result["vote_average"]}
Total Votes: {result["vote_count"]}
--------------------""")
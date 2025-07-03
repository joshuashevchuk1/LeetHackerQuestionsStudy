from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample movie data
movies_data = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "imdb": 8.8},
    {"id": 2, "title": "The Godfather", "genre": "Crime", "imdb": 9.2},
    {"id": 3, "title": "Pulp Fiction", "genre": "Crime", "imdb": 8.9},
    {"id": 4, "title": "Interstellar", "genre": "Sci-Fi", "imdb": 8.6},
    {"id": 5, "title": "Parasite", "genre": "Thriller", "imdb": 8.6},
    {"id": 6, "title": "The Dark Knight", "genre": "Action", "imdb": 9.0},
    {"id": 7, "title": "Avengers: Endgame", "genre": "Action", "imdb": 8.4},
]

@app.route('/movies', methods=['GET'])
def get_movies():
    genre_filter = request.args.get('genre')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 3))

    filtered = [movie for movie in movies_data if genre_filter is None or movie["genre"].lower() == genre_filter.lower()]

    # Sort by IMDb descending
    filtered.sort(key=lambda x: x["imdb"], reverse=True)

    # Pagination
    start = (page - 1) * limit
    end = start + limit
    paginated = filtered[start:end]

    return jsonify({
        "page": page,
        "limit": limit,
        "total_results": len(filtered),
        "results": paginated
    })

@app.route('/top-by-genre', methods=['GET'])
def top_movie_per_genre():
    top_movies = {}
    for movie in sorted(movies_data, key=lambda x: x["imdb"], reverse=True):
        if movie["genre"] not in top_movies:
            top_movies[movie["genre"]] = movie

    return jsonify(list(top_movies.values()))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

from flask import Flask, jsonify, request
from config import db, app
from models import Pokemon
from get_files import connect_to_server
from handle_query import get_all_answers
from handle_query import run_user_query_on_db
import os
from werkzeug.utils import secure_filename

@app.route("/pokemons", methods=["GET"])
def get_contact():
    pokemon = Pokemon.query.all()
    json_pokemons = list(map(lambda x: x.to_json(), pokemon))
    return jsonify({"Pokemons": json_pokemons})

@app.route("/create", methods=["POST"])
def create():
    try:
        data = request.get_json()
        user_url = data.get("query", "")
        return jsonify({"message": "Database is created", "data":f"{connect_to_server(151, user_url)}"})
    except Exception as e:
        return jsonify({"message": "Error", "data": f"{str(e)}"}), 500

@app.route("/generate", methods=["POST"])
def generate():
    try:
        final_answers = get_all_answers()
        return jsonify({
            "message": "Database search done",
            "data": final_answers or " No data generated."
        })
    except Exception as e:
        print("ERROR in /generate:", e)
        return jsonify({"message": "Error", "data": f"{str(e)}"}), 500
    
@app.route("/query", methods=["POST"])
def run_user_query():
    try:
        data = request.get_json()
        user_query = data.get("query", "")
        result = run_user_query_on_db(user_query)
        return jsonify({"message": "Query executed", "data": result})
    except Exception as e:
        print("ERROR in /query:", e)
        return jsonify({"message": "Error", "data": str(e)}), 500
    
@app.route("/upload", methods=["POST"])
def upload_file():
    DB_FOLDER = "instance"
    DB_FILE = os.path.join(DB_FOLDER, "mydatabase.db")
    os.makedirs(DB_FOLDER, exist_ok=True)
    if "file" not in request.files:
        return jsonify({"data": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"data": "No file selected"}), 400

    filename = secure_filename(file.filename)
    save_path = DB_FILE
    try:
        file.save(save_path)
        return jsonify({"data": f"Database file saved as {save_path}"})
    except Exception as e:
        print("Error saving file:", e)
        return jsonify({"data": "Error saving file"}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

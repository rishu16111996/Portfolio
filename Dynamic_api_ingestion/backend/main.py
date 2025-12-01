from flask import jsonify, request
from config import db, app

from get_files import connect_to_server
from handle_query import get_all_answers, run_user_query_on_db
from handleMetadata import parse_metadata_string
from models import get_output

import os


@app.route("/createMetadata", methods=["POST"])
def create_metadata():
    try:
        data = request.get_json()
        schema_str = data.get("schema", "")
        class_name = data.get("className", "DynamicModel")

        get_output(schema_str, class_name)

        with app.app_context():
            db.drop_all()
            db.create_all()

        return jsonify({
            "status": "success",
            "message": "Schema applied!",
            "fields": parse_metadata_string(schema_str)
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/create", methods=["POST"])
def create():
    try:
        data = request.get_json()
        user_url = data.get("query", "")

        msg = connect_to_server(0, user_url)
        return jsonify({"message": "Database created", "data": msg})
    except Exception as e:
        print("ERROR in /create:", e)
        return jsonify({"message": "Error", "data": str(e)}), 500


@app.route("/generate", methods=["POST"])
def generate():
    try:
        final_answers = get_all_answers()
        return jsonify({
            "message": "Database search done",
            "data": final_answers or "No data generated"
        })
    except Exception as e:
        return jsonify({"message": "Error", "data": str(e)}), 500


@app.route("/query", methods=["POST"])
def run_user_query():
    try:
        data = request.get_json()
        user_query = data.get("query", "")

        result = run_user_query_on_db(user_query)
        return jsonify({"message": "Query executed", "data": result})
    except Exception as e:
        return jsonify({"message": "Error", "data": str(e)}), 500


@app.route("/reset-db", methods=["POST"])
def reset_db():
    try:
        db.session.remove()
        db.drop_all()
        db.engine.dispose()

        uri = app.config["SQLALCHEMY_DATABASE_URI"]
        db_path = None
        if uri.startswith("sqlite:///"):
            db_path = uri.replace("sqlite:///", "", 1)

        if db_path and os.path.exists(db_path):
            os.remove(db_path)

        return jsonify({"ok": True, "message": "Database cleared."}), 200

    except Exception as e:
        return jsonify({"ok": False, "message": str(e)}), 500


@app.route("/setdefault", methods=["POST"])
def set_default():
    try:
        data = request.get_json()
        schema_str = data.get("schema", "")
        class_name = data.get("className", "DynamicModel")

        get_output(schema_str, class_name)

        with app.app_context():
            db.drop_all()
            db.create_all()

        return jsonify({
            "status": "success",
            "message": "Default schema applied!",
            "fields": parse_metadata_string(schema_str)
        }), 200

    except Exception as e:
        return jsonify({"message": "Error", "data": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

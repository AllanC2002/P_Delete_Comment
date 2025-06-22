from flask import Flask, request, jsonify
from services.functions import delete_comment
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
SECRET_KEY = os.getenv("SECRET_KEY")

@app.route("/delete-comment", methods=["PUT"])
def delete_usercomment():
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Token missing or invalid"}), 401

    token = auth_header.replace("Bearer ", "")
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = decoded.get("user_id")
        if not user_id:
            return jsonify({"error": "Invalid token"}), 401
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    body = request.json
    comment_id = body.get("comment_id")

    # 🔧 Aquí devolvemos tal cual lo que regresa la función
    return delete_comment(comment_id, user_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)

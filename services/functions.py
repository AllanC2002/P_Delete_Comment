from bson import ObjectId
from flask import jsonify
from conections.mongo import conection_mongo

def delete_comment(comment_id, user_id):
    db = conection_mongo()
    comments_collection = db["Comments"]

    try:
        # Asegurarse de que comment_id sea un ObjectId válido
        comment_obj_id = ObjectId(comment_id)
    except Exception:
        return jsonify({"error": "Invalid comment ID format"}), 400

    # Buscar el comentario por ID
    comment = comments_collection.find_one({"_id": comment_obj_id})

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    print("Id_user del comentario:", comment.get("Id_user"), type(comment.get("Id_user")))
    print("user_id del token:", user_id, type(user_id))

    # Comparar como enteros para validar propiedad
    if comment.get("Id_user") != user_id:
        return jsonify({"error": "Unauthorized to delete this comment"}), 403

    try:
        comments_collection.update_one(
            {"_id": comment_obj_id},
            {"$set": {"status": 0}}
        )
        return jsonify({"message": "Comment deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"Failed to delete comment: {str(e)}"}), 500

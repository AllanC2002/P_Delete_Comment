import pytest
from unittest.mock import patch, MagicMock
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_delete_comment_success(client):
    mock_token = "mocktoken"
    mock_user_id = 123
    mock_comment_id = "507f1f77bcf86cd799439011"

    with patch("main.jwt.decode") as mock_jwt_decode, \
         patch("services.functions.conection_mongo") as mock_conection_mongo:
        
        mock_jwt_decode.return_value = {"user_id": mock_user_id}

        mock_db = MagicMock()
        mock_comments_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_comments_collection
        mock_conection_mongo.return_value = mock_db

        mock_comments_collection.find_one.return_value = {
            "_id": mock_comment_id,
            "Id_user": mock_user_id,
            "Status": 1
        }

        mock_comments_collection.update_one.return_value.modified_count = 1

        response = client.put(
            "/delete-comment",
            headers={"Authorization": f"Bearer {mock_token}"},
            json={"comment_id": mock_comment_id}
        )

        assert response.status_code == 200
        assert response.json["message"] == "Comment deleted successfully"

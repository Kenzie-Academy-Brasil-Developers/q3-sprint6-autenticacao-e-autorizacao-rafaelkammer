from flask import jsonify, request
from app.models.user_model import UserModel
from app.configs.database import db
from secrets import token_urlsafe
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def create_user():
    data = request.get_json()

    user: UserModel = UserModel(**data)

    db.session.add(user)
    db.session.commit()

    return jsonify(user), 201

def login_user():
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

    if not user or not user.check_password(data['password']):
        return {"error": "E-mail and/or password incorrect."}, 401

    token = create_access_token(user)

    return {"access_token": token}, 200

@jwt_required()
def get_profile():
    
    user = get_jwt_identity()

    return jsonify(user), 200

@jwt_required()
def update_user():
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

    for key, value in data.items():
        setattr(user, key, value)

    db.session.add(user)
    db.session.commit()

    return jsonify(user), 200

@jwt_required()
def delete_user():
    user = get_jwt_identity()

    user: UserModel = UserModel.query.filter_by(email=user["email"]).first()

    db.session.delete(user)
    db.session.commit()

    return {"msg": f"User {user.name} has been deleted"}
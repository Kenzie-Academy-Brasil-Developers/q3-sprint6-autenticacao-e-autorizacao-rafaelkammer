from flask import jsonify, request
from app.models.user_model import UserModel
from app.configs.database import db
from secrets import token_urlsafe
from app.configs.auth import auth, verify_token

def create_user():
    data = request.get_json()
    data['api_key'] = token_urlsafe(16)

    user: UserModel = UserModel(**data)

    db.session.add(user)
    db.session.commit()

    return jsonify(user), 201

def login_user():
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

    if not user or not user.check_password(data['password']):
        return {"error": "E-mail and/or password incorrect."}, 401
    
    return {"api_key": user.api_key}, 200

@auth.login_required
def get_profile():
    
    user = auth.current_user()

    return jsonify(user), 200

@auth.login_required
def update_user():
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

    for key, value in data.items():
        setattr(user, key, value)

    db.session.add(user)
    db.session.commit()

    return jsonify(user), 200

@auth.login_required
def delete_user():
    email_to_del = auth.current_user().email

    user: UserModel = UserModel.query.filter_by(email=email_to_del).first()

    db.session.delete(user)
    db.session.commit()

    return {"msg": f"User {user.name} has been deleted"}
from flask import Flask, Blueprint
from app.controllers import user_controller

bp = Blueprint('users', __name__, url_prefix="")

bp.post('/signup')(user_controller.create_user)
bp.post('/signin')(user_controller.login_user)
bp.get('')(user_controller.get_profile)
bp.put('')(user_controller.update_user)
bp.delete('')(user_controller.delete_user)
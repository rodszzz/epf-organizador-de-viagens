import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


class User:
    def __init__(self, id, name, email, birthdate, password_hash):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.password_hash = password_hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'password_hash': self.password_hash
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            email=data.get('email'),
            birthdate=data.get('birthdate'),
            password_hash=data.get('password_hash')
        )


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [User.from_dict(item) for item in data]
        except (json.JSONDecodeError, TypeError):
            return []

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users],
                      f, indent=4, ensure_ascii=False)

    def get_all(self):
        self.users = self._load() # CORREÇÃO
        return self.users

    def get_by_id(self, user_id: int):
        self.users = self._load() # CORREÇÃO
        return next((u for u in self.users if u.id == user_id), None)
        
    def get_by_email(self, email: str):
        self.users = self._load() # CORREÇÃO
        return next((u for u in self.users if u.email.lower() == email.lower()), None)

    def add_user(self, user: User):
        self.users.append(user)
        self._save()

    def update_user(self, updated_user: User):
        self.users = self._load() # CORREÇÃO
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break

    def delete_user(self, user_id: int):
        self.users = self._load() # CORREÇÃO
        self.users = [u for u in self.users if u.id != user_id]
        self._save()
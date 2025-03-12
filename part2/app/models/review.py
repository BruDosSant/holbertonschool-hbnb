import uuid
from datetime import datetime
from app.models.base import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        """
        Crea una nueva instancia de Review.
        Descubrí que:
        text: Contenido de la reseña (string).
        rating: Puntuación entre 1 y 5 (entero).
        place: Instancia de Place asociada a la reseña.
        user: Instancia de User que escribió la reseña.
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def Text(self):
        return self._text
    @text.setter
    def validate_text(self, text):
        """Valida que el texto no esté vacío."""
        if not isinstance(text, str) or not text.strip():
            raise ValueError("El texto de la reseña no puede estar vacío.")
        return text

    @property
    def Rating(self):
        return self._rating
    @rating.setter
    def validate_rating(self, rating):
        """Valida que la calificación esté entre 1 y 5."""
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("La calificación debe estar entre 1 y 5.")
        return rating

    @property
    def Place(self):
        return self._place
    @Place.setter
    def validate_place(self, place):
        """Valida que la reseña esté asociada a un lugar válido."""
        if not isinstance(place, Place):
            raise ValueError("El objeto place debe ser una instancia de Place.")
        return place

    @property
    def User(self):
        return self._user
    @User.setter
    def validate_user(self, user):
        """Valida que la reseña tenga un usuario válido."""
        if not isinstance(user, User):
            raise ValueError("El objeto user debe ser una instancia de User.")
        return user

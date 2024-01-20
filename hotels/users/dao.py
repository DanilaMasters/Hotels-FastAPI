from hotels.dao.base import BaseDAO
from hotels.users.models import User


class UserDAO(BaseDAO):
    model = User
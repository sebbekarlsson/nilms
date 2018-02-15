from nilms.config import config
from nilms.facades.user_facade import UserFacade
from nilms.password import get_hashed_password


def add_user():
    if UserFacade.get(name=config['username']):
        return

    user = UserFacade.create(
        name=config['username'],
        password=get_hashed_password(config['password'])
    )

    print('Created user: {}'.format(str(user.id)))


def init():
    add_user()

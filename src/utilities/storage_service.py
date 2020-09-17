from . import session
from .misc import singleton
from .models import SearchHistory


@singleton
class SearchHistoryService:
    """
    Service used to deal with data of user's Search History
    """

    def __init__(self):
        self.session = session

    def insert_search_history(self, user_id, term):
        instance = SearchHistory(user_id, term)
        self.session.add(instance)
        self.session.commit()

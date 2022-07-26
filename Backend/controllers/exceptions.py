class ArticleException(Exception):
    ...

class ArtcileNotFoundError(ArticleException):
    def __init__(self) -> None:
        self.status_code = 404
        self.detail = "Article Not Found"


class ReservationException(Exception):
    ...

class ReservationNotFoundError(ReservationException):
    def __init__(self) -> None:
        self.status_code = 404
        self.detail = "Reservation Not Found"

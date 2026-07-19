import datetime

from app.main import outdated_products
from _pytest.monkeypatch import MonkeyPatch


class FakeDate(datetime.date):
    @staticmethod
    def today() -> datetime.date:
        return datetime.date(2022, 2, 2)


def test_if_data_expired(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.datetime.date", FakeDate)
    assert outdated_products(
        [
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]
    ) == ["duck"]


def test_if_data_not_expired(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.datetime.date", FakeDate)
    assert outdated_products(
        [
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 3),
                "price": 160
            }
        ]
    ) == []


def test_if_data_same_as_today(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.datetime.date", FakeDate)
    assert outdated_products(
        [
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 160
            }
        ]
    ) == []


def test_if_list_empty() -> None:
    assert outdated_products([]) == []

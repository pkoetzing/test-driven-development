import fraud_example


def the_mock(input):
    return 0.999


def test_is_credit_card_fraud_monkeypatch(monkeypatch):
    monkeypatch.setattr("fraud_example.dark_magic", the_mock)

    transaction = {"amount_usd": "9999.99", "overnight_shipping": True}
    is_fraud = fraud_example.is_credit_card_fraud(transaction)
    assert is_fraud

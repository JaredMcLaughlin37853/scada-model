from src.services.validation import validate_equipment_list

def test_validate_pass():
    payload = {"equipment": []}
    assert validate_equipment_list(payload) is True
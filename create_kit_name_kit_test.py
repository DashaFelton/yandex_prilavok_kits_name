import sender_stand_request
import data


def get_kit_body(name):
    return {'name': name}

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    auth_token = response.json()['authToken']
    return auth_token

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body['name']

def negative_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert response.status_code == 400


def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body('a')
    positive_assert(kit_body)

def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')
    positive_assert(kit_body)

def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = get_kit_body('')
    negative_assert(kit_body)

def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')
    negative_assert(kit_body)

def test_create_kit_english_letter_in_name_get_success_response():
    kit_body = get_kit_body('QWErty')
    positive_assert(kit_body)

def test_create_kit_russian_letter_in_name_get_success_response():
    kit_body = get_kit_body('Мария')
    positive_assert(kit_body)

def test_create_kit_special_symbol_in_name_get_success_response():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body)

def test_create_kit_has_space_in_name_get_success_response():
    kit_body = get_kit_body('Человек и КО')
    positive_assert(kit_body)

def test_create_kit_has_number_in_name_get_success_response():
    kit_body = get_kit_body('123')
    positive_assert(kit_body)

def test_create_kit_without_name_field_get_error_response():
    kit_body = {}
    negative_assert(kit_body)

def test_create_kit_number_type_in_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)


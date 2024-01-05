import json

def test_api_not_found(api):
    res = api.get('/abc')
    assert res.status == '404 NOT FOUND'

# def test_api_get_authors(api):
#     res = api.get('/authors')
#     assert res.json == {'data': [{'age': 20, 'genres': 'fantasy', 'id': 1, 'name': 'Britney', }, {'age': 23, 'genres': 'drama', 'id': 2, 'name': 'John'}]}
    
# def test_api_post_authors(api):
#     mock_data = json.dumps({'age': 20, 'genres': 'fantasy', 'id': 1, 'name': 'Britney'})
#     mock_headers = {'Content-Type': 'application/json'}
#     res = api.post('/authors', data=mock_data, headers=mock_headers)
#     assert res.json['data']['id'] == 1



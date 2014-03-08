#SERVER_NAME = '127.0.0.1:5000'
schema = {
    'title': {
        'type': 'string',
        'maxlength': 255,
    }
}
courses = {
    'schema': schema,
}
DOMAIN = {
    'courses': courses,
}

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

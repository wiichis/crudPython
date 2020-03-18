import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'
    },
    {
        'name': "Ricardo",
        'company': 'Facebook',
        'email': 'ricado@facebook.com',
        'position': 'Data engineer'
    },
    {
        'name': "will",
        'company': 'w',
        'email': 'w',
        'position': 'w'
    }
]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client {} already is in the client\'s list'.format(client['name']))


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        _message_client_is_not_in_list()


def delete_client(client_id):
    global clients

    if len(clients) - 1 >= client_id:
        clients.pop(client_id)
    else:
        _message_client_is_not_in_list()


def search_client(client_name):
    global clients

    for client in clients:
        for data in client.values():
            if client_name == data:
                return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))

    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _message_client_is_not_in_list():
    print('The client: {} is not in our client\'s list'.format(client_name))


def _message_client_is_in_list():
    print('The client: {} is in our client\'s list'.format(client_name))

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()

    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()

    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            _message_client_is_in_list()
        else: 
            _message_client_is_not_in_list()
        

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        list_clients()
    else:
        print('Invalid command')

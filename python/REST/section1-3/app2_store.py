from flask import Flask, jsonify, request, render_template

print('Running: ', __name__)

app = Flask(__name__)
stores = [
    {
        'name': 'First Store',
        'items': [
            {
                'name': 'Item 1',
                'price': 15.50
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['GET'])
def get_stores():
    """
    Get information about all the stores.
    :return: List of all the store dictionaries.
    """
    return jsonify({'stores': stores})


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    """
    Get the information about the store with name=name
    :param name: Name of the store to retrieve information about.
    :return: The store information if found or message that store wasn't found.
    """
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({'message': 'Store: "{}" not found.'.format(name)})


@app.route('/store', methods=['POST'])
def create_store():
    """
    Put information to create a new store.
    :return: The new store information.
    """
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    return jsonify(new_store)


@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    """
    Get information about all the items in the store.
    :param name: The name of the store to get the item information for.
    :return: The item information.
    """
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

    return jsonify({'message': 'Store: "{}" not found.'.format(name)})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    """
    Post a new item to be added to a store.
    :param name: The name of the store.
    :return: The store information.
    """
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            store['items'].append({'name': request_data['name'],
                                   'price': request_data['price']})
            return jsonify(store)

    return jsonify({'message': 'Store: "{}" not found.'.format(name)})


app.run(port=5000)

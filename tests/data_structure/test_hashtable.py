from data_structures_and_algorithms.data_structures.hashtable.hashtable import Hashtable

def test_add_key_value():
    table = Hashtable()
    table.add('omar','pizza')
    assert table.map[table.hash('omar')].head.data == ['omar','pizza']

def test_update_key_value():
    table = Hashtable()
    table.add('omar','pizza')
    table.add('omar','kfc')
    assert table.map[table.hash('omar')].head.data[1] == 'kfc'

def test_get_value_from_key():
    table = Hashtable()
    table.add('omar','pizza')
    assert table.get('omar') == 'pizza'

def test_get_value_not_in_table():
    table = Hashtable()
    assert table.get('omar') == 'key not exist'

def test_retrieve_data_with_collision():
    table = Hashtable()
    table.add('omar','pizza')
    table.add('zain','kfc')
    assert table.get('omar') == 'pizza'
    assert table.get('zain') == 'kfc'
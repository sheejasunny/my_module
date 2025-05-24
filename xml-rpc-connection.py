import xmlrpc.client

# Configuration
url = 'http://localhost:8069'  # Change this to your Odoo instance URL
username = 'sheeja836@vidyaacademy.ac.in'
password = '123'
db       = 'TESTDBODOO16'


# XML-RPC endpoints
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print("Authenticated! UID:", uid)
else:
    raise Exception("Authentication failed.")

# Accessing models
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Example: Search and Read 'estate.property' (contacts)
property_ids = models.execute_kw(db, uid, password,  'estate.property', 'search',[[]], )
print("search function ==>:", property_ids)

# Example:count function
count_property_ids = models.execute_kw(db, uid, password,  'estate.property', 'search_count',[[]], )
print("search function ==>:", count_property_ids)


# Example: Search and Read 'estate.property' (contacts)
read_property_ids = models.execute_kw(db, uid, password,  'estate.property', 'read',[property_ids],{'fields':['name']} )
print("search function ==>:", read_property_ids)

search_read_property_ids = models.execute_kw(db, uid, password,  'estate.property', 'search_read',[[]],{'fields':['name']} )
print("search function ==>:", search_read_property_ids)

create_property_ids = models.execute_kw(db, uid, password,  'estate.property', 'create',[{'name':'Property from RPC','sales_id':2}] )
print("search function ==>:", create_property_ids)

write_property_ids = models.execute_kw(db, uid, password, 'estate.property', 'write', [[8], {'name':'Property from RPC Updated'}])

print("update property ==>:", write_property_ids)





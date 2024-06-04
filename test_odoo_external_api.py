import datetime
import xmlrpc.client

url = 'http://localhost:8069'
db = 'wh'
username = 'admin'
password = 'admin'

def authenticate(url, db, username, password):
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    if uid:
        print('Authenticated as', username)
    else:
        raise Exception('Authentication failed')
    return uid

def create_partner(url, db, uid, password):
    print('aoikoawkowa')
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    partner_id = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['email', '=', 'william@gmail.comd']]], {'fields': ['id', 'name','email'], 'limit': 1})
    print(partner_id)
    if partner_id:
        id_partner = partner_id[0].get('id')
        name_partner = partner_id[0].get('name')
        email_partner = partner_id[0].get('email')
        print(partner_id[0].get('id'))
    elif not partner_id:
        partner_id = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['email', '=', 'william@gmail.comd']]], {'fields': ['id', 'name','email'], 'limit': 1})
        print("awlowkoaw")
    exit()
    time_now = datetime.datetime.now()
    partner_data = {
        'partner_id':id_partner,
        'name': "TEST APPS",
        'user_id': uid,
        'team_id':1,
        'company_id':1,
        'email_from': email_partner,
        # 'priority':3,
        'description':"TEST",
        'type':"opportunity",
        'active': True,
        # 'date_open': time_now,
        # 'date_last_stage_update': time_now,
        # 'create_date': time_now,
        # 'write_date': time_now,

    }
    
    partner_id = models.execute_kw(db, uid, password, 'crm.lead', 'create', [partner_data])
    print('Created partner with ID:', partner_id)
    return partner_id

# def create_contact(email):
#     models.execute_kw(db, uid, password, 'crm.lead', 'create', [partner_data])

def main():
    try:
        uid = authenticate(url, db, username, password)
        create_partner(url, db, uid, password)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()

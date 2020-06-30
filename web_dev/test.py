import psycopg2

src_string = 'postgresql://postgres:123456@localhost:5432/postgres'
conn = psycopg2.connect(src_string)

create_sql = '''
CREATE TABLE if not exists login_information
(
    name VARCHAR,
    password INTEGER 
);
'''
cursor = conn.cursor()

cursor.execute(create_sql)
conn.commit()

insert_sql = '''
insert into login_information (name, password) values ('postgres', 123456);
'''
cursor = conn.cursor()

cursor.execute(insert_sql)
conn.commit()
conn.close()


login_list = (
        {
            'name' : 'minh'
            'password' : '123'
        }
        {
            'name'
            'password'
        }
)
input_name = 'minhvd'
input_password = '123'
for person in login_list:
    if person['name'] == input_name
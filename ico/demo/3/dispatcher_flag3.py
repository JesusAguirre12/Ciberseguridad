from client import *
import sys
import os

FLAG3 = os.getenv('FLAG3', 'ICO{example_flag_3}')

baseurl = f"http://{sys.argv[2]}"

flag3_username = 'flag3_user'
flag3_password = randstr(random.randint(8,16))

user = User(baseurl)
user.register(flag3_username, flag3_password)
resp = user.add_note('Note for flag 3', randstr(random.randint(10,20)))
note_id = resp.text.split('Note ')[1].split(' added')[0]
user.add_comment(note_id, FLAG3)
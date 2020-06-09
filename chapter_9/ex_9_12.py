### ex 9.12 multiple modules

from chapter_9.User import User
from chapter_9.Admin import Privilege,Admin

MattD = Admin('Matt', "D'avela", 24, 'male', ['minimalist', 'good coffee', 'big biceps', 'sponsored by Audible'])

MattD.age
MattD.describe_user()
MattD.privileges.show_priviliges()
### ex 9.12 multiple modules

from User import User
from Admin import Privilege,Admin

MattD = Admin('Matt', "D'avela", 24, 'male', ['minimalist', 'good coffee', 'big biceps', 'sponsored by Audible'])

MattD.age
MattD.describe_user()
MattD.privileges.show_priviliges()
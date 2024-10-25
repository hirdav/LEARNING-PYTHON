# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from Privileges_1 import Admin as P

show=P('io','ud',p=34, p1=23)
print(f"{show.first_name},{show.last_name}")
show.privileges.privileges=['E$$','2&8']
show.privileges.show_privileges()
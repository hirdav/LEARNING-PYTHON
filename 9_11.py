# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store 
# the classes User, Privileges, and Admin in one module. Create a separate file, 
# make an Admin instance, and call show_privileges() to show that everything is 
# working correctly.

from Imported_admin import Admin

calling_admin= Admin('you','2008',more=1,less=0)
print(f" {calling_admin.first_name},{calling_admin.last_name},{calling_admin.other_attributes}")
calling_admin.privileges.privileges = ['tu',89,['4$']]
calling_admin.privileges.show_privileges()
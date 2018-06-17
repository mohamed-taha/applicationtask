import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def site_list(c):
	c.execute("SELECT * FROM sites_sites")
	result = c.fetchall()
	return result

def site_sum(c):
	c.execute("select name, (select SUM(a_value) from sites_value WHERE sites_value.site_id = sites_sites.id ) as b_value, (select SUM(a_value) from sites_value WHERE sites_value.site_id = sites_sites.id ) as b_value from sites_sites")
	result = c.fetchall()
	return result
def site_average(c):
	c.execute("select name, (select AVG(a_value) from sites_value WHERE sites_value.site_id = sites_sites.id ) as b_value, (select AVG(a_value) from sites_value WHERE sites_value.site_id = sites_sites.id ) as b_value from sites_sites")
	result = c.fetchall()
	return result

print ('List of Site:')
for row in site_list(c):
	print (row[1])
print ('-------------------------------------------------------------------------')
print ('Sum Summary of Site:')
print ('Site          A value          B value')
for row in site_sum(c):
	print (str(row[0]) + '          ' + str(row[1]) + '          ' + str(row[2]))
print ('-------------------------------------------------------------------------')
print ('Average Summary of Site:')
print ('Site          A value          B value')
for row in site_average(c):
	print (str(row[0]) + '          ' + str(row[1]) + '          ' + str(row[2]))
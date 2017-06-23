#!/usr/bin/python

import cgi,commands

print "content-type:text/html\r\n\r\n"
print ""

form=cgi.FieldStorage()
username=form.getvalue('u')
password=form.getvalue('p')

#Storing user's data in a file
#a_user=commands.getstatusoutput("sudo cat users.txt | grep "username" | awk '{print $1}'")
#a_password=commands.getstatusoutput("sudo cat users.txt | grep "password" | awk '{print $3}'")

#if a_user[1]==username and a_password[1]==password:
if username=="root" and password=="redhat":
	print "<META HTTP-EQUIV='refresh' content='0; url=/next.html'/>"
		
	
else:	
	print "<script>alert('Wrong Password')</script>" 
	print "<META HTTP-EQUIV='refresh' content='0; url=/index.html'/>"



# IMPORTING NECESSARY MODULES
import urllib, sys, hmac, random, base64, hashlib, xml.etree.ElementTree as ET

# READ THE DETAILS REQUIRED BY USER REQUIRED 
option = int(raw_input("Fetch details of:\n1. Department\n2. Ticket Statuses\n3. Ticket Priorities\n4. Ticket Types\n5. StaffID's\n"))
if option == 1:
  target = '/Base/Department'
  tag = 'department'
elif option == 2:
  target = '/Tickets/TicketStatus'
  tag = 'ticketstatus'
elif option == 3:
  target = '/Tickets/TicketPriority'
  tag = 'ticketpriority'
elif option == 4:
  target = '/Tickets/TicketType'
  tag = 'tickettype'
elif option == 5:
  target = '/Base/Staff'
  tag = 'staff'
else:
  print 'Invalid Option'
  sys.exit(0)

# AUTHENTICATION DETAILS

apikey = 'ENTER API KEY HERE'
api_url = 'ENTER YOUR API URL HERE'
secretkey = 'ENTER SECRET KEY HERE'
salt = str(random.getrandbits(32))
signature = hmac.new(secretkey, msg=salt, digestmod=hashlib.sha256).digest()
encodedSignature = base64.encodestring(signature).replace('\n', '')
encodedSignature = urllib.quote(encodedSignature)
url = '%s%s&apikey=%s&salt=%s&signature=%s' % (api_url, target, apikey, salt, encodedSignature)

# API CALL AND RESPONSE BEING read AS response
response = urllib.urlopen(url).read()

# DISPLAYING NECESSARY DATA FROM THE XML response
root = ET.fromstring(response)
for i in root.findall(tag):
 id = i.find('id').text
 if tag == 'staff':
  fullname = i.find('fullname').text
 else:
  fullname = i.find('title').text
 print id, fullname

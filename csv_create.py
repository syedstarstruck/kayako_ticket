# IMPORTING NECESSARY MODULES
import urllib, urllib2, xml.etree.ElementTree as ET, hashlib, random, base64, hmac, csv

# AUTHENTICATION DETAILS
apikey = 'ENTER API KEY HERE'
api_url = 'ENTER API URL HERE'
target = '/Tickets/Ticket'
secretkey = 'ENTER SECRET KEY HERE'
salt = str(random.getrandbits(32))
signature = hmac.new(secretkey, msg=salt, digestmod=hashlib.sha256).digest()
encodedSignature = base64.encodestring(signature).replace('\n', '')
url = '%s%s' % (api_url, target)

# IMPORTING DOMAINS and TEMPLATE 
data = list(csv.reader(open('domains.txt'), delimiter=','))
content = open('template.txt').read()

# FUNCTION FOR api CALL TO CREATE TICKET
def create_ticket(domain, email):
 dom = domain
 dest = email
 params = urllib.urlencode({
  'subject': dom + " | ENTER SUBJECT STRING HERE",
  'fullname': 'ENTER STAFF NAME HERE',
  'email': dest,
  'contents': content,
  'departmentid': 95,
  'ticketstatusid': 7,
  'ticketpriorityid': 13,
  'tickettypeid': 2,
  'staffid': 227,
  'apikey': apikey,
  'salt': salt,
  'signature': encodedSignature,
})
 try:
  response = urllib2.urlopen(url, params).read()
  root = ET.fromstring(response)
  for ticket in root.findall('ticket'):
    id = ticket.find('displayid').text
    print "\n" + id + "\t" + dom
    file = open("tickets.txt","a")
    file.write("\n" + id +"\t" + dom)
 except urllib2.HTTPError as e:
     error = e.read() # this will be your error message
     print error

print "\nTo view ticket ID creation, create a text file named tickets.txt\n"

# READING THE DOMAINS FILE FOR DOMAINS AND NOTIFICATION ADDRESS AND CALLING THE API FUNCTION
for elem in data:
 create_ticket(elem[0],elem[1])

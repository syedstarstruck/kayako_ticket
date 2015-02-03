# kayako_ticket
Python based Kayako ticket creation using Kayako API.

This script can be used to call Kayako API to automate ticket creation.

A python based script which calls Kayako (REST) API for creating tickets. Advantage is that we can track all notifications from our end with a ticket ID.

Files needed:
        domains.txt : containing csv in the format (domain.tld,email@isp.tld)
        tickets.txt : a blank file in which the details of tickets created are added.
        template.txt: a file containing the template or ticket contents.

Required details:
  1. Department
  2. Ticket Statuses
  3. Ticket Priorities
  4. Ticket Types
  5. StaffID's
All the above can be obtained by running the script (/usr/bin/python get.py)

Usage:
    Get the following details from Kayako Admin interface:
      REST API key
      REST API URL
      Secret key

1. Edit the variables(apikey, api_url, secretkey) in csv_create.py with the above details. Leave the target variable unchanged.
2. Edit the subject variable (in the example, the subject looks like domain.tld | Subject_string)
3. Populate domains.txt and template.txt file with the appropriate data.

Run the script in the python prompt (/usr/bin/python csv_create.py).

You can find the list of ticket ID's created onscreen and it gets saved in the tickets.txt file as well.
    
    

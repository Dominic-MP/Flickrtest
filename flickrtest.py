# -*- coding: utf-8 -*-
import flickrapi, json, csv

api_key = u'14b18fb30ce1bc25bad10a8f62cb491b'
api_secret = u'1ba0332d63c8e57b'

flickr = flickrapi.FlickrAPI(api_key, api_secret)
flickr.authenticate_via_browser(perms='write')

with open('/Users/Dominic/Downloads/SRL 7 item-spreadsheet (released images)-with NAIDs.tsv', 'r') as log :
	readfile = csv.reader(log, delimiter= '\t')
	for row in readfile:
		naid = row[0]
		title = row[2]
		day = row[4]
		month = row[5]
		year = row[6]
		filename = row[14]
		local_id = row[11]

		description = """<strong>These images have been released in response to a FOIA request, case number 2014-0012-F, received by the National Archives. For more information on these images, please visit<a href="http://www.archives.gov/research/vice-presidential-records/research.html"> Researching Vice Presidential Materials</a>. These photos will be available in the National Archives Catalog in July 2015.</strong>

<strong>National Archives Identifier (NAID): </strong> """ + naid + """

<strong>Local Identifier: </strong> """ + local_id + """

<strong>Created By: </strong> <a href="https://catalog.archives.gov/id/10508142">President (2001-2009 : Bush). Office of Management and Administration. Office of White House Management. Photography Office. 1/20/2001-1/20/2009</a>

<strong>From: </strong> <a href="https://catalog.archives.gov/id/https://catalog.archives.gov/id/6180352">Collection: Vice Presidential Records of the Photography Office (George W. Bush Administration), 1/20/2001 - 1/20/2009</a>

<strong>Contact: </strong> 
Presidential Materials Division (LM)
National Archives Building
7th and Pennsylvania Avenue NW
Washington, DC 20408
E-mail: <a href="mailto:presidential.materials@nara.gov">presidential.materials@nara.gov</a>
Phone: 202-357-5200
Fax: 202-357-5939

<strong>Production Date(s): </strong> """ + month + "/" + day + "/" + year + """

<strong>Persistent URL: </strong> <a href="https://catalog.archives.gov/id/""" + naid + """">catalog.archives.gov/id/""" + naid + """</a>

<strong>Access Restrictions: </strong>Unrestricted
<strong>Use Restrictions: </strong>Unrestricted"""

# 		print filename
# 		print title
# 		print description

		flickr.upload(filename = '16161882570_f94a45b8d4_c.jpg', title = title, is_public = 0, description = description)
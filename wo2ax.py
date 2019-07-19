# -*- coding: utf-8 -*-  

#----------------------------------------------------------------------------
#   wo2ax.py - WO2 thesaurus to Adlib XML 
#   
#   turns NIOD's SPARQL endpoint WO2 thesaurus into an embedded authority 
#   file within Adlib collection management software
#
#    Copyright (C) 2019 Rolf Blijleven
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    
#    Find @RolfBly on Twitter
#----------------------------------------------------------------------------
import requests
import json
import lxml.etree as ET

def WO2(searchterm, language='nl'): 

    URL = 'https://data.niod.nl/PoolParty/sparql/WO2_Thesaurus?' 

    query_blank = '''PREFIX skos: <http://www.w3.org/2004/02/skos/core#> CONSTRUCT {{ ?Concept skos:Concept ?Concept ; skos:prefLabel ?prefLabel ; skos:scopeNote ?scopeNote ; skos:altLabel ?altLabel ; skos:broaderLabel ?broaderLabel ; }} WHERE {{ ?Concept skos:prefLabel ?prefLabel ; skos:prefLabel|skos:altLabel ?label . FILTER (lang(?prefLabel)="{1}" && lang(?label)="{1}" && strstarts(LCASE(?label), LCASE("{0}")) ) OPTIONAL {{?Concept skos:altLabel ?altLabel }} OPTIONAL {{?Concept skos:scopeNote ?scopeNote FILTER(lang(?scopeNote)="{1}") }} OPTIONAL {{?Concept skos:broader ?broader . ?broader skos:prefLabel ?broaderLabel FILTER(lang(?broaderLabel)="{1}") }} }} ORDER BY ?prefLabel LIMIT 20 '''

    header = 'Content-Type: application/x-www-form-urlencoded'
    format = 'application/xml'
    query = query_blank.format(searchterm, language)
    params = {'query': query, 'format': format, 'header': header}
    r = requests.get(url=URL, params=params)
    WO2_reply_root = ET.fromstring(r.content)
    xslt = ET.parse('./static/WO2.xsl')
    transform = ET.XSLT(xslt)
    almostxml = transform(WO2_reply_root) 
    AdlibXML = ET.tostring(almostxml, xml_declaration=True, encoding='utf-8')
    return AdlibXML

def main(): 
               
    testterms = [('kindertehuis', {}), 
                  ('transport', {'language': 'en'}), 
                  ('transporten', {}), 
                  ('belasting', {}),
                  ('verzet', {}),
                  ('baros', {}), 
                  ('kamp', {})
                 ]
                
    for term, language in testterms:  
        xml = WO2(term, language.get('language', 'nl'))   
        with open('{}.xml'.format(term), 'wb') as f:
            f.write(xml)
            
if __name__ == "__main__":  
    main()                  
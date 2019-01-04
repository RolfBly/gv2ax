# -*- coding: utf-8 -*-  

import requests  
import json  
from lxml import etree as ET  
from lxml.builder import E  

def AAT(search_term, language='nl', pretty=False): 

    def fetch(field_name):
        return record[field_name]['value']
    
    URL = '''http://vocab.getty.edu/sparql.json?query=SELECT * WHERE {{?subject skos:inScheme <http://vocab.getty.edu/aat/> . ?subject luc:term "{0}*"; xl:prefLabel|xl:altLabel ?Getty_ID . ?Getty_ID dct:language gvp_lang:{1}; xl:literalForm ?term; gvp:termType ?term_type FILTER regex(?term, '^{0}', 'i') OPTIONAL {{?subject gvp:broaderPreferred ?broader_Getty_ID . ?broader_Getty_ID xl:prefLabel [dct:language gvp_lang:{1}; xl:literalForm ?broader_term]}} OPTIONAL {{?subject skos:scopeNote [dct:language gvp_lang:{1}; rdf:value ?scope_note]}} OPTIONAL {{?Getty_ID rdfs:comment ?history_note}} OPTIONAL {{?Getty_ID gvp:estStart ?est_start}} OPTIONAL {{?Getty_ID gvp:estEnd ?est_end}} }} ORDER BY ?term LIMIT 20'''  
    
    #  "vars" : [ "subject", "Getty_ID", "term, "term_type", "broader_Getty_ID", "broader_term", "scope_note", "history_note", "est_start", "est_end" ]  
    
    # 0: search_term  
    # 1: valid_languages = ['nl', 'en']  

    gvp_response = requests.get(URL.format(search_term, language)) 
    gvp_response.raise_for_status()
    # gvp_response.encoding = 'utf-8'
    gvp_json = gvp_response.json()
    # with open('{}.json'.format(search_term), 'w') as f:
        # f.write(str(gvp_json))

    xmllist = E.recordList()  
    for record in gvp_json['results']['bindings']:
        term_type_uri = fetch('term_type')
        term_type = term_type_uri.rsplit('/', 1)[1]
        subject = fetch('subject').replace('aat/', 'page/aat/')
        xmlrec = E.record(  
            E.term(fetch('term')),
            E.Getty_ID(subject),
        )
        xmlrec.append(E('source.number', subject))
        xmlrec.append(E('term.number', subject))
        xmlrec.append(E.term_type(term_type))
        xmlrec.append(E.term_type_uri(term_type_uri))
        xmlrec.append(E.source('Getty Vocabularies AAT, CC-BY license'))
        try:  
            # xmlrec.append(E.broader_url(fetch('broader_Getty_ID'))) # can't use? 
            xmlrec.append(E('broader.term', fetch('broader_term')))  # need . in tag name  
        except KeyError:  
            pass  
        try:  
            xmlrec.append(E.scope_note(fetch('scope_note')))  
        except KeyError:  
            pass  
        try:  
            history_note = fetch('history_note')
        except KeyError:  
            history_note = ''  
        try:  
            estStart = fetch('est_start')
        except KeyError:  
            estStart = ''
        try:  
            estEnd = fetch('est_end')
        except KeyError:  
            estEnd = ''

        print(history_note, estStart, estEnd)
            
        if history_note != '':
            if (
               (estStart != '' and estStart not in history_note)
                or (estEnd != '' and estEnd not in history_note)
               ):
                history_note = '{} ({} - {})'.format(history_note, estStart, estEnd)
            
            xmlrec.append(E.history_note(history_note))

        xmllist.append(xmlrec)  
        
    almostxml = (E.adlibXML())  
    almostxml.append(xmllist)
    AdlibXML = ET.tostring(almostxml, xml_declaration=True, encoding='utf-8', pretty_print=pretty)
    return AdlibXML 
    
def main(): 

    testterms = [('bicycle', {'language': 'en'}), 
                 ('fiets', {}), 
                 ('crystol', {}), 
                 ('löss', {})   
                ]   

    for term, language in testterms:  
        xml = AAT(term, language.get('language', 'nl'), pretty=True)   
        with open('{}.xml'.format(term), 'wb') as f:
            f.write(xml)
if __name__ == "__main__":  
    main()  

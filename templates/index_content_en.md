## Webservice of the Dutch Adlib User Group  

Adlib is collection management software. The Dutch Adlib User Group is een association of people and institutions that use that software.  

### Getty Vocabularies AAT in Adlib XML  

This webservice allows you to derive and/or complement thesaurus-records in your Adlib, from the Art & Architecture Thesaurus (AAT), maintained by The Getty Vocabularies Project. The fields that you can derive and/or complement are detailed below.  

The webservice is intended as an _Advanced External Source_ in Adlib. In order to use the service, you may need to upgrade your Adlib software to version 7.5, and you will need to make a few modifications to your Adlib-application. [This document][1] provides the details.  

#### Wat does it do?  

This video shows what it looks like for the Adlib user. Narration in Dutch.  
<iframe src="https://player.vimeo.com/video/314264717" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>  
#### How to modify Adlib  

[This document][1] provides full detail. You will need some skill with Adlib Designer.  

#### What's the URL format?  

The base URL for the AAT-webservice is  

    http://service.adlibug.nl/aat/search?term=  

A search is called a query-URL, it looks like this.  

[http://service.adlibug.nl/aat/search?term=bank][3]  

Try it! The default search language is **Dutch**. **English**, **French** and **German** are supported as well. You specify the language in the query-URL, like so:  

[http://service.adlibug.nl/aat/search?term=bicycle&lang=en][4]  
    
[http://service.adlibug.nl/aat/search?term=bicyclette&lang=fr][5]  
    
[http://service.adlibug.nl/aat/search?term=fahrrad&lang=de][6]  

In Adlib Designer, you specify the external source for your term(s) (e.g. Object name, Object category, or Keyword) for each field, in its tab _Linked field properties_, box _External sources_, field _Path to URL_. For Dutch, you would enter:  

    http://service.adlibug.nl/aat/search?term=%data%  
    
For German, it would be:  

    http://service.adlibug.nl/aat/search?term=%data%&lang=de  
    
Note that you don't need quotes around `%data%`, nor a '*' after it to force right-truncation. The service does that for you. So 'crystol' will get you 'crystolea', 'crystoleum' and 'crystoleums'.  
    

#### Which fields does the service provide?  
    
The answer to the query may contain any of the fields below.  

|veldnaam       |content|standard Adlib|tag|
|---------------|------|---------------|---|
|`term`         |the term found|yes|`te`|
|`source.number`|URL of the concept in Getty Vocabularies|yes, see 1a. |`tn`|
|`term.number`  |URL of the concept in Getty Vocabularies|yes, see 1b. |`tn`|
|`Getty_ID`     |URL of the concept in Getty Vocabularies|yes, see 1c. ||
|`source`       |'Getty Vocabularies AAT, CC-BY license', always|yes|`br`|
|`scope_note`   |Scope note|yes|`sn`|
|`history_note` |Historical note|yes|`hn`|
|`term_type`    |_term type_ in Getty Vocabularies|no, see 2.||
|`term_type_uri`|link to term_type in Getty Vocabularies|no, see 2.||
|`broader.term` |Getty Vocabularies' _Preferred broader term_ of the term found|yes, zie 3.|`bt`|


### notes  
1. This URL is a unique, persistent identifier in the form of a hyperlink, to the Getty ID for the term. Where do you put this?  
   a. Application version 4.5 has a field `source.number`, tag `tn` of the type _Application_.  
   b. Application version 3.4 and 4.2 have the field `term.number`, tag `tn`, data type _Text_. You'll want hyperlinks to be clickable, so you'll have to change the data type to _Application_.  
   c. Should you choose to create a separate field group for the fields you derive with this service, then you should create a field with the data dictionary name Getty_ID, of the type Application.  
   
2. Your Adlib thesaurus has a field _term type_ (`term.type`) for the term's domain (e.g. _creator_ or _material type_). In Getty Vocabularies, `term_type` is more a term _term status_, but it's values do not correspond to what's in Adlib. Hence, this field could be used for orientation, but copying it into a thesaurus record isn't very useful. Likewise for `term_type_uri`.  

3. Whether or not Getty's Broader Preferred term is suitable for your collection, your thesaurus, depends on your collection.  

<br>  

#### How does it work?  

Refer to the image below. Clockwise from top left, we start with a term that you enter into a thesaurus-validated field in Adlib. The service wraps that term in a SPARQL query url, and sends that to Getty Vocabularies AAT SPARQL endpoint. It responds in json. The service turns that answer into Adlib-XML. The fields in the response can be automatically copied ('derived') into your Adlib's thesaurus.  

![Hoe werkt de service][7]  

[1]: /static/Advanced_external_source_v_service.adlibug.nl.pdf  
[3]: http://service.adlibug.nl/aat/search?term=fiets  
[4]: http://service.adlibug.nl/aat/search?term=bicycle&lang=en  
[5]: http://service.adlibug.nl/aat/search?term=bicyclette&lang=fr  
[6]: http://service.adlibug.nl/aat/search?term=fahrrad&lang=de  
[7]: /static/gvp2ax2.jpg  "Interface between Getty Vocabularies AAT and Adlib. Clockwise from top left, a term that you enter in a catalogue record, is wrapped in a SPARQL-query and sent to Getty Vocabularies SPARQL endpoint. The response in json is turned into Adlib XML and made available in the Adlib thesaurus linked to your catalogue."  

#### Credits

Author: [Rolf Blijleven][8]
<div><small>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 		    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></small></div>

## Webservice van de Adlib Gebruikersgroep  

Adlib is software voor collectie-registratie. De Alib Gebruikersgroep is een vereniging van mensen en instellingen die gebruik maken van die software.  

### Getty Vocabularies AAT in Adlib XML  

Door middel van deze webservice kun je thesaurustermen in Adlib ontlenen en/of aanvullen met informatie uit de Art & Architecture Thesaurus.  

De service is bedoeld als een zogenaamde _Advanced External Source_ in Adlib. Om die te kunnen gebruiken, zijn aanpassingen in je Adlib-applicatie nodig. In [dit document][1] is beschreven hoe je die aanpassingen kunt maken.  

#### Wat doet het?  

Hoe het werkt voor gebruikers is te zien in deze video. 
<iframe src="https://player.vimeo.com/video/314264717" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
#### Wat moet je aanpassen in Adlib?  

In [dit document][1] (Engels) is beschreven hoe je Adlib kunt aanpassen. Enige bekendheid met de bediening van Adlib Designer is noodzakelijk.  

#### Hoe ziet een query-URL eruit?  

De basis-URL voor de AAT-webservice is  

    http://service.adlibug.nl/aat/search?term=  

Een zoekopdracht heet een query-URL, die ziet er zo uit:  

[http://service.adlibug.nl/aat/search?term=fiets][3]  

Probeer het maar! Standaard zoekt de service naar **Nederlandse** termen. **Engel"**, **Frans** en **Duits** zijn ook mogelijk. Dat kun je opgeven in de query-URL:  

[http://service.adlibug.nl/aat/search?term=bicycle&lang=en][4]  
    
[http://service.adlibug.nl/aat/search?term=bicyclette&lang=fr][5]  
    
[http://service.adlibug.nl/aat/search?term=fahrrad&lang=de][6]  

In Adlib Designer geef je de _external source_ voor je termen (bijvoorbeeld Objectnaam, Object categorie of Trefwoord) voor elk veld in tabblad _Linked field properties_, box _External sources_, veld  _Path to URL_. Voor Nederlands geef je dit:  

    http://service.adlibug.nl/aat/search?term=%data%  
    
Voor Duits zou je dit doen:  

    http://service.adlibug.nl/aat/search?term=%data%&lang=de  
    
Merk op dat er geen aanhalingstekens om `%data%` nodig zijn, en ook geen '*' erachter om rechtstruncatie af te dwingen. Dit doet de service vanzelf al. Dus als je zoekt op 'crystol' krijg je 'crystolea', 'crystoleum' en 'crystoleums'.  

#### Welke velden kan de service geven?  
    
Het antwoord op deze query kan onderstaande velden bevatten.  

|veldnaam       |inhoud|standaard Adlib|tag|
|---------------|------|---------------|---|
|`term`         |de gevonden term|ja|`te`|
|`source.number`|URL van de term in Getty Vocabularies|ja, zie 1a. |`tn`|
|`term.number`  |URL van de term in Getty Vocabularies|ja, zie 1b. |`tn`|
|`Getty_ID`     |URL van de term in Getty Vocabularies|nee, zie 1c. ||
|`source`       |'Getty Vocabularies AAT, CC-BY license', altijd|ja|`br`|
|`scope_note`   |Scope note|ja|`sn`|
|`history_note` |historische notitie|ja|`hn`|
|`term_type`    |_Soort term_ in Getty Vocabularies|nee, zie 2.||
|`term_type_uri`|link naar Soort term in Getty Vocabularies|nee, zie 2.||
|`broader.term` |_Preferred broader term_ van de _gevonden term_ in Getty Vocabularies|ja, zie 3.|`bt`|


### noten  
1. Deze URL is een unieke, persistente identifier in de vorm van een internet-link naar het Getty ID voor de term. In welk veld zet je die?  
   a. Applicatie-versie 4.5 heeft standaard een veld `source.number` met tag `tn` van het data-type _Application_.  
   b. Applicatie-versies 3.4 en 4.2 bevatten standaard het veld `term.number` met tag `tn`, van het data-type _Text_. Meestal wil je een hyperlink aanklikbaar hebben, dus dan moet het data-type van dat veld _Application_ worden.  
   c. Als je ervoor kiest om in je thesaurus een aparte veldgroep aan te maken voor deze velden, dan moet je in de data dictionary het Engelstalige URL-veld `Getty_ID` noemen in de data dictionary.  
   
2. Adlib bevat een veld _soort term_ (`term.type`) voor het domein van de term (bijvoorbeeld _vervaardiger_ of _materiaalsoort_). In Getty Vocabularies heeft `term_type` eerder de functie van _term status_, maar de waardes daarvan komen niet overeen met die in Adlib. Daarom is dit veld wel bruikbaar ter oriëntatie, maar minder geschikt om over te nemen in Adlib. Hetzelfde geldt voor `term_type_uri`.  

3. Of je Getty's Broader Preferred term al dan niet moet overnemen in je eigen thesaurus, hangt sterk af van je collectie.  

<br>  

#### Hoe werkt het?  

Zie onderstaand plaatje. Het begint met een term die je invoert in een thesaurus-veld in Adlib. De service verpakt die term in een SPARQL-query-url, en stuurt die naar de AAT van het SPARQL-endpoint van Getty Vocabularies. Die geeft antwoord in json. De service zet dat antwoord om in Adlib-XML. Daarmee zijn velden in het antwoord direct bruikbaar in Adlib.  

![Hoe werkt de service][7]  

[1]: /static/Advanced_external_source_v_service.adlibug.nl.pdf
[3]: http://service.adlibug.nl/aat/search?term=fiets  
[4]: http://service.adlibug.nl/aat/search?term=bicycle&lang=en  
[5]: http://service.adlibug.nl/aat/search?term=bicyclette&lang=fr  
[6]: http://service.adlibug.nl/aat/search?term=fahrrad&lang=de  
[7]: /static/gvp2ax2.jpg  "Interface tussen Getty Vocabularies en Adlib. Van linksboven met de klok mee: een term ingevoerd in een gevalideerd veld wordt verpakt in een query die naar het SPARQL-endpoint van Getty Vocabularies gaat. Het antwoord in json wordt verwerkt tot Adlib XML en is daarmee direct beschikbaar in de thesaurus."  

#### Colofon

- Service, documentatie en deze site gemaakt door [Rolf Blijleven][8]. Contact: [@RolfBly][9] 
- Hosting: [PythonAnywhere][10]

Met dank aan het support team van het [Getty Vocabularies Project][13] en aan de overige leden van het bestuur van de Adlib Gebruikersgroep. 

De code voor dit project is _open source_ software, beschikbaar via [Github][11] onder een [GNU General Public Licentie versie 3.0][12]. 

[8]: http://www.rolfblijleven.nl
[9]: https://twitter.com/RolfBly
[10]: https://www.pythonanywhere.com
[11]: https://github.com/RolfBly/gv2ax
[12]: https://choosealicense.com/licenses/gpl-3.0/
[13]: https://groups.google.com/forum/#!forum/gettyvocablod
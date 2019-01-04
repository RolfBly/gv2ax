## Webservices van de Adlib Gebruikersgroep  

Adlib is software voor collectie-registratie. De Alib Gebruikersgroep is een vereniging van mensen en instellingen die gebruik maken van die software.  

### Getty Vocabularies AAT in Adlib XML  

Door middel van deze webservice kun je thesaurustermen in Adlib voorzien van unieke identifiers uit de Art & Architecture Thesaurus.  

Waarom zou je dat doen? Een term als _bank_ kan van alles zijn: een financiële instelling, een bankgebouw, een strook land onder water waar mosselen groeien, en nog wel meer. De term _bank (meubilair)_ is al minder dubbelzinnig. Door nu in het thesaurusrecord voor _bank (meubilair)_ een link op te nemen naar de identifier voor dat _concept_ in de Art &amp; Architecture Thesaurus, worden records in je collectie vindbaar als _concept_, en dat is onafhankelijk van de taal waarin gezocht wordt. Op die manier kunnen geautomatiseerd verbanden worden gevonden met andere collecties die beschikbaar zijn als Linked Open Data.  

De service is bedoeld als een zogenaamde _Advanced External Source_ in Adlib. Om die te kunnen gebruiken, zijn enkele aanpassingen in je Adlib-applicatie nodig. In [dit document][1] is beschreven hoe je die aanpassingen kunt maken.  

#### Wat doet het?  

Hoe het werkt voor gebruikers is te zien in [deze video][2].  

#### Hoe werkt het?  

Zie onderstaand plaatje. Het begint met een term die je invoert in een thesaurus-veld in Adlib. De service verpakt die term in een SPARQL-query-url, en stuurt die naar de AAT van het SPARQL-endpoint van Getty Vocabularies. Die geeft antwoord in json. De service zet dat antwoord om in Adlib-XML. Daarmee zijn velden in het antwoord direct bruikbaar in Adlib.  

![Hoe werkt de service][7]  

#### Wat moet je aanpassen in Adlib?  

In [dit document][1] is beschreven hoe je Adlib kunt aanpassen. Bekendheid met Adlib Designer is noodzakelijk.  

De basis-URL voor de AAT-webservice is  

    http://services.adlibug.nl/aat/search?term=  

Een zoekopdracht heet een query-URL, die ziet er zo uit:  

[http://services.adlibug.nl/aat/search?term=fiets][3]  

Standaard zoekt de service naar Nederlandse termen. Engels, Frans en Duits zijn ook mogelijk. Dat kun je opgeven in de query-URL:  

[http://services.adlibug.nl/aat/search?term=bicycle&lang=en][4]  
    
[http://services.adlibug.nl/aat/search?term=bicyclette&lang=fr][5]  
    
[http://services.adlibug.nl/aat/search?term=fahrrad&lang=de][6]  
    
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
1.  Deze URL is de unieke identifier waar het allemaal om begonnen is. In welk veld zet je die?  
   a. Applicatie-versie 4.5 heeft standaard een veld `source.number` met tag `tn` van het data-type _Application_.  
   b. Applicatie-versies 3.4 en 4.2 bevatten standaard het veld `term.number` met tag `tn`, van het data-type _Text_. Meestal wil je een hyperlink aanklikbaar hebben, dus dan moet het data-type van dat veld _Application_ worden.  
   c. Als je ervoor kiest om in je thesaurus een aparte veldgroep aan te maken voor deze velden, dan moet je in de data dictionary het Engelstalige URL-veld `Getty_ID` noemen in de data dictionary.  
   
2. Adlib bevat een veld _soort term_ (`term.type`) voor het domein van de term (bijvoorbeeld _vervaardiger_ of _materiaalsoort_). In Getty Vocabularies heeft `term_type` eerder de functie van _term status_, maar de waardes daarvan komen niet overeen met die in Adlib. Daarom is dit veld wel bruikbaar ter oriëntatie, maar minder geschikt om over te nemen in Adlib. Hetzelfde geldt voor `term_type_uri`.  

3. Of je Getty's Broader Preferred term al dan niet moet overnemen in je eigen thesaurus, hangt sterk af van je collectie.  

<br>  


[1]: PDF howto hertaald van Erik, moet ander linkje in en ander screenshot.  
[2]: video bediening.  
[3]: http://services.adlibug.nl/aat/search?term=fiets  
[4]: http://services.adlibug.nl/aat/search?term=bicycle&lang=en  
[5]: http://services.adlibug.nl/aat/search?term=bicyclette&lang=fr  
[6]: http://services.adlibug.nl/aat/search?term=fahrrad&lang=de  
[7]: /static/gvp2ax2.jpg  "Interface tussen Getty Vocabularies en Adlib. Van linksboven met de klok mee: een term ingevoerd in een gevalideerd veld wordt verpakt in een query die naar het SPARQL-endpoint van Getty Vocabularies gaat. Het antwoord in json wordt verwerkt tot Adlib XML en is daarmee direct beschikbaar in de thesaurus."  
## WO2-thesaurus in Adlib  

De webservice van de Adlib Gebruikersgroep kan ook dienen als Advanced External Source voor de WO2-thesaurus van het Nederlands Instituut voor Oorlogsdocumentatie (NIOD). Het werkt op dezelfde manier als bij de [Getty AAT service][3]. [Dit document][1] (Engels) zet uiteen hoe je Adlib daarvoor kunt aanpassen. Enige bekendheid met de bediening van Adlib Designer is noodzakelijk.  

De WO2 thesaurus bevragen gaat met een URL. Dat kan vanuit Adlib, of rechtstreeks vanuit een browser. Probeer maar! 

[http://service.adlibug.nl/wo2/search?term=belasting][2]  

Engels (en) en Duits (de) zijn ook mogelijk:  

[http://service.adlibug.nl/wo2/search?term=transport&lang=en][4]  
   
[http://service.adlibug.nl/wo2/search?term=fahrrad&lang=de][5]  

Voor de werkwijze in Adlib zie verder de [handleiding bij de AAT-interface][3].  

[1]: /static/Advanced_external_source_v_service.adlibug.nl.pdf  
[2]: /wo2/search?term=belasting  
[3]: /  
[4]: /wo2/search?term=transport&lang=en  
[5]: /wo2/search?term=fahrrad&lang=de  


### mapping  

Onderstaande velden zijn beschikbaar. Het is technisch mogelijk om geografische coördinaten en een afbeelding op te halen uit de WO2-thesaurus. Dat is wellicht voor een toekomstige implementatie.  

| Query veldnaam | wat is het                 | Adlib XML veldnaam  | Standaard Adlib       | tag |
|----------------|----------------------------|---------------------|-----------------------|-----|
| WO2_URL        | URL voor de term           | source.number       | ja, zie 1a            | tn  |
| WO2_URL        | URL voor de term           | term.number         | ja, zie 1b            | tn  |
| WO2_URL        | URL voor de term           | WO2_URL             | nee, zie 1 c          | WU  |
| prefLabel      | de voorkeursterm           | term                | ja                    | te  |
| label          | de term waarmee gezocht is | used_for            | ja, maar zie 3        | uf  |
| altlabel       | alternatieve term          | used_for            | ja, maar zie 3        | uf  |
| scopeNote      | scope note                 | scope_note          | ja                    | sn  |
| scopeNote      | scope note                 | `WO2_scope_note`    | nee, zie 1 c          | WN  |
| broader        | URL naar de broader term   |                     | niet bruikbaar, zie 2 |     |
| broaderLabel   | broader term               | broader.term        | ja, maar zie 3        | bt  |


#### noten  

1. Deze URL is een unieke, persistente identifier in de vorm van een internet-link naar het WO2-thesaurusrecord voor de term. In welk veld zet je die?  
   a. Applicatie-versie 4.5 heeft standaard een veld `source.number` met tag `tn` van het data-type _Application_.  
   b. Applicatie-versies 3.4 en 4.2 bevatten standaard het veld `term.number` met tag `tn`, van het data-type _Text_. Meestal wil je een hyperlink aanklikbaar hebben, dus dan moet het data-type van dat veld _Application_ worden.  
   c. Als je ervoor kiest om in je thesaurus een aparte veldgroep aan te maken voor de velden die je ophaalt uit de WOII-thesaurus, dan moeten de Engelstalige data-dictionary-namen identiek zijn aan de veldnamen die de interface geeft.  

2. Via een Advanced External Source kun je alleen de velden van één enkel thesaurus-record vullen of updaten, niet de velden van een daaraan gekoppeld record (of dat te omzeilen is moet nog worden onderzocht). Daarom worden uri's van de broaders nog niet opgevraagd.  
   
3. Broaders dienen primair voor context. Of ze al dan niet kloppen in de context van een gegeven collectie, is aan de beheerders van die collectie. Termen in de WO2-thesaurus kunnen meerdere bredere (voorkeurs)termen hebben, wat in Adlib tot even zo veel gekoppelde records zou leiden. (Daarom geven we ook geen narrowers, want dat kunnen er tientallen zijn.)  
   Binnen Adlib (in het linkscherm _vindt gekoppeld record_) kun je alleen de eerste broader naast de term laten zien (bij wijze van context). Of die term al dan niet geïmporteerd wordt, staat daar los van. Maar als je broaders importeert, dan worden ze ook _allemaal_ geïmporteerd.  


## Query  

De vraag aan het SPARQL-endpoint van de WO2-thesaurus.  

### `CONSTRUCT`  

- we geven op welke velden we terug willen zien.  

  In eerste instantie zochten we behalve naar pref- en altLabels ook naar hiddenLabels (bijvoorbeeld 'negers' geeft 'Afro-Amerikanen') om zo de gebruiker naar de juiste term te leiden. Echter, 'Afro-Amerikanen' is een deelverzameling van 'negers', en _"[hiddenLabels] is niet altijd betrouwbaar ingevuld."_ aldus NIOD. Daarom is hiddenLabel toch geschrapt. Het was:  
  
        ?Concept skos:prefLabel ?prefLabel ;  
                skos:prefLabel|skos:altLabel|skos:hiddenLabel ?label .  

  het werd:  
  
        ?Concept skos:prefLabel ?prefLabel ;  
                skos:prefLabel|skos:altLabel ?label .  

- De WO2-Thesaurus staat meerdere broaders per prefLabel toe (per term is er niet slechts één enkele broaderPreferred, zoals in de Getty AAT). Bijvoorbeeld 'Baros' is prefLabel met altLabel "Baros III van velden", en het heeft 4 broaders. Als platte tabel levert elke permutatie een regel, dus een WHERE-query levert 8 regels of json- of XML-nodes in totaal. Die kun je in de interface wel weer groeperen, maar we willen zoveel mogelijk werk door SPARQL laten doen. Onderstaande query antwoordt met een Adlib-achtige datastructuur. We halen alle WO2-velden op in SKOS-xml, die we met een XSLT-transformatie omzetten naar AdlibXML. 

(Je kunt de query copy-pasten in het [SPARQL-endpoint][6] en er verder mee experimenteren.)  

[6]: https://data.niod.nl/PoolParty/sparql/WO2_Thesaurus?  

    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>  
    
    CONSTRUCT {  
        ?Concept skos:Concept ?Concept ;  
           skos:prefLabel ?prefLabel ;  
           skos:scopeNote ?scopeNote ;  
           skos:altLabel ?altLabel ;  
           skos:broaderLabel ?broaderLabel .  
    }  
    WHERE {  
        ?Concept skos:prefLabel ?prefLabel ;  
             skos:prefLabel|skos:altLabel ?label .  
        FILTER (lang(?prefLabel)="nl" &&  
                lang(?label)="nl" &&  
                strstarts(LCASE(?label), LCASE("kindertehuis"))  
                )  
        OPTIONAL {?Concept skos:altLabel ?altLabel }  
        OPTIONAL {?Concept skos:scopeNote ?scopeNote  
                   FILTER(lang(?scopeNote)="nl")  }  
        OPTIONAL {?Concept skos:broader ?broader .  
                  ?broader skos:prefLabel ?broaderLabel  
                  FILTER(lang(?broaderLabel)="nl")  }  
    } ORDER BY ?prefLabel LIMIT 20  

---  

### Colofon  

Dit gedeelte van de service.adlibug.nl is tot stand gekomen met ondersteuning van Nederlands Instituut voor OorlogsDocumentatie. Met dank aan Lizzy Jongma (NIOD) en Joop Vanderheijden (Rijksdienst Cultureel Erfgoed).  

- Project van [Rolf Blijleven][8], contact [@RolfBly][9].  
- Hosting door [PythonAnywhere][10].  

De code voor dit project is open source software, beschikbaar via [Github][11] onder een [GNU General Public Licentie versie 3.0][12].  

<br>  
<br>  

[8]: http://www.rolfblijleven.nl  
[9]: https://twitter.com/RolfBly  
[10]: https://www.pythonanywhere.com  
[11]: https://github.com/RolfBly/gv2ax  
[12]: https://choosealicense.com/licenses/gpl-3.0/  

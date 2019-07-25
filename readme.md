## gv2ax - Getty Vocabularies to Adlib XML

Gv2ax lets you use Getty Vocabularies AAT as a built-in authority file in Adlib collection management software. 

`Gv2ax.py` is a module for `service_adlibug.py`. Together they're a webservice. They're built in Python 3.7 and Flask. This repository makes it an open source project and allows for easier deployment. 

For more information, see templates/index_content_en.html (English) or templates/index_content_nl.html (Dutch)

Gv2ax can run as a local service using Flask's built in test server. Not recommended for production. You will need a virtual Python 3.7 environment with Flask, requests and lxml. See requirements.txt. 

### todo

- redo intro video, as 'portret' is a bad object name
- add video for various ways of using the service in Adlib
- research possible workarounds (using adapl) for issues. 

## wo2ax.py - WO2-thesaurus to Adlib XML

Wo2ax lets you use the WO2-thesaurus maintained by Nederlands Instituut voor Oorlogsdocumentatie (NIOD) as a built-in authority file in Adlib collection management software. WO2 stands for WereldOorlog 2, World War 2. NIOD is Dutch Institute for War Documentation, part of the Royal Dutch Academy of Sciences. 

Like `gv2ax.py`, `wo2ax.py` is a module for `service_adlibug.py. 

For more information, see templates/wo2_content_nl.html (Dutch). 


### License

Copyright 2019 Rolf Blijleven

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as published by
the Free Software Foundation. 

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
[GNU General Public License version 3][1] or the COPYING file 
in this repository for more details. 

[1]: https://choosealicense.com/licenses/gpl-3.0/

Contact [@RolfBly](https://twitter.com/RolfBly)
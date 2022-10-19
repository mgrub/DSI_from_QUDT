# SPARQL QUDT to DSI extractor test

## Disclaimer

Please be aware that the source code provided in this repository is work in progress and doesn't claim to be correct or complete by any means.

## Goal

- prototypical proof-of-concept implementation to see, whether the conversion is possible at all
- aims to provide a DSI-string for (a selected subset of) the QUDT-units, e.g. to provide this to a user / LaTeX-engine

## Known limits and issues

- only units with conversionmultiplier==1.0 and conversionoffset==0.0 considered so far (location+amount of prefixed units (e.g., mm/ms) of the prefix not clear, e.g. check m/ms = km/s )
- some units with DEG_C still show up, although offset units should be filtered?
- not considered so far: official order of quantities in DSI?
- not considered so far: dimensionless quantities like m/m 

## Links

- <https://www.qudt.org/fuseki/#/dataset/qudt/query>
- <https://www.ptb.de/empir2018/fileadmin/documents/empir/SmartCom/documents_for_download/Digital_System_of_Units_D-SI_2019-11-04_UK_NPL_SmartCom.pdf>
- <https://ctan.org/pkg/siunitx>

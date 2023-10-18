# Establishing links between (semantic) unit formats

idea collection for scidatacon

a bit more technical

## motivation

- idea of the semantic web
- connection of knowledge
- open world assumption --> possibility for overlapping / co-exist

--> links between different unit representation systems highly desirable to support interoperatbility of them
--> try to automate these links as much as possible while ensuring correctness of established links

## a case study

- from QUDT to DSI,
- prototypical proof-of-concept implementation to see, whether the conversion is possible at all
- aims to provide a DSI-string for (a selected subset of) the QUDT-units, e.g., to provide this to a user / LaTeX-engine
- use of SPARQL-request, which is launched from a Python-script

- even though DSI not semantic, can be connected due to the information amount in expressive unit represenation (as QUDT here)

## Known limits and issues

- only units with conversionmultiplier==1.0 and conversionoffset==0.0 considered so far (location+amount of prefixed units (e.g., mm/ms) of the prefix not clear, e.g. check m/ms = km/s )
- some units with DEG_C still show up, although offset units should be filtered?
- not considered so far: official order of quantities in DSI?
- not considered so far: dimensionless quantities like m/m 
- DSI unit string is not necessarily unique, only one variant is generated

## outlook

- adjust the script to create mappings between units and quantities of QUDT and the SIRP
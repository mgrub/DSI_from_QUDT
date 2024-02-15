# Linking Unit Formats - A Case Study

The semantic web toolbox enables us to operate on knowledge graphs and with that let machines have an understanding of concepts and their relations.
However, not all links can be made by machine alone, especially for so far disconnected subgraphs.
Moreover, in metrology, it is essential to mure that provided links can be trusted.

In the following proof-of-concept, it is therefore of interest to show how the information already available in the QUDT knowledge graph can be used to establish a connection to the flexible, but not semantically enabled, DSI-unit-string-format.
Of course, both are just two variants out of a large group of unit representation frameworks.
While QUDT is an advanced framework with sound semantics, the DSI is more know for its relevance in the Digital Calibration Certificate.

Providing a set of automated but curated links between the DSI and QUDT is highly desirable to:

- see if the mapping is possible at all
- support interoperability in general
- enable semantic reasoning for (a subset) of possible DSI-unit-strings.

## Approach

The general idea is to create a valid DSI string for a subset of units in the QUDT knowledge graph.
Every `qudt:unit` has properties `qudt:conversionMultiplier` and `qudt:hasDimensionVector`.
Some of these units also have a `qudt:conversionOffset`.
Each `qudt:QuantityKindDimensionVector` has properties `qudt:dimensionExponentFor<XYZ>`.[^note]
These properties can therefore be retrieved for all units of QUDT.
By filtering for coherent units (conversion factor equals one, offset equals zero), the dimension vector of the `qudt:Unit` can be used to construct a valid DSI-unit-string.
All this can be implemented in a single SPARQL query.

[^note] with `<XYZ>` as a placeholder for `AmountOfSubstance`, `ElectricCurrent`, `Length`, `LuminousIntensity`, `Mass`, `ThermodynamicTemperature`, `Time`, `dimensionlessExponent`

## Results

In total, 718 correspondences are found, for which a DSI string can be provided for the specific QUDT unit.
E.g.:

| QUDT                | DSI                                                          |
| ------------------- | ------------------------------------------------------------ |
| unit:M              | "\metre"                                                     |
| unit:KiloGM         | "\kilogram"                                                  |
| unit:N-M            | "\metre\tothe{2}\kilogram\second\tothe{-2}"                  |
| unit:OHM            | "\ampere\tothe{-2}\metre\tothe{2}\kilogram\second\tothe{-3}" |
| unit:KiloGM-PER-MOL | "\mole\tothe{-1}\kilogram"                                   |

## Limitations

The approach still has certain limitations.
Only units with "`qudt:conversionMultiplier`==1.0" and "`qudt:conversionOffset`==0.0" with respect to the SI-system (coherent units) are considered, as this avoids the issue of the location and amount of prefixed units, e.g., compare "m/ms" and "km/s".
Despite the described filtering, units that contain temperature in Celsius (`qudt:DEG_C`) are not filtered and are (erroneously) translated into Kelvin.
Dimensionless quantities are suppressed, as the dimension vector does not give any hint about the quantity quotient, e.g., "\metre\metre\tothe{-1}".
Only one DSI-string is generated, also often multiple DSI representations can exist for the same unit.

## Outlook

A potential extension would be the addition of units with a scaling factor different from one, e.g., prefixed units.
Moreover, it is of interest to link either QUDT or DSI to the upcoming SI Reference Point.

## References

QUDT
<https://www.qudt.org/>

DSI / DCC
<https://www.ptb.de/empir2018/fileadmin/documents/empir/SmartCom/documents_for_download/Digital_System_of_Units_D-SI_2019-11-04_UK_NPL_SmartCom.pdf>

SI Reference Point
<https://www.bipm.org/documents/20126/71876713/DIG-MET-2022-MILES.pdf/f0757b30-eac0-7afc-c6ec-677a5fa092f4>

Source Code
<https://github.com/mgrub/DSI_from_QUDT>

CODATA DRUM TG
<https://codata.org/initiatives/task-groups/drum/>
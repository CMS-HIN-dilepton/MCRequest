# MCRequest
The configuration files for signal generation (embedding, pp efficiency, pp acceptance) for the official MC requests made by the Dilepton group. 

## Important note for pPb
The convention is very confusing. In short all of the following correspond to the same configuration
- proton going to positive eta
- "pPb" in the usual naming convention
- second part of the 2016 8TeV run
- PbP in the vertex smearing option
- no "reverse" in the cfi name
- BetaBoost = +0.434 in the gen filter
- protonSide = 1 for PyQuen

## For updating
'Charmonium:gg2ccbar(3S1)[3S1(1)]gm = on', for prompt charm
'Bottomonium:gg2bbbar(3S1)[3S1(1)]gm = on', for upsilon
https://hypernews.cern.ch/HyperNews/CMS/get/generators/2437/1.html
http://home.thep.lu.se/Pythia/pythia82html/OniaProcesses.html

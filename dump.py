import sys

import GaudiPython as GP
from GaudiConf import IOHelper
from Configurables import DaVinci

dv = DaVinci()
dv.DataType = 'Upgrade'
dv.Simulation = True

# Pass file to open as first command line argument
inputFiles = [sys.argv[-1]]
IOHelper('ROOT').inputFiles(inputFiles)

appMgr = GP.AppMgr()
evt = appMgr.evtsvc()

appMgr.run(2)
evt.dump()


hs = evt["/Event/MC/VP/Hits"]
hits = [ (h.X(), h.Y(), h.Z()) for h in [ e.entry() for e in hs]] 

import json
with open("hits.json", "w") as f:
   json.dump(hits, f)


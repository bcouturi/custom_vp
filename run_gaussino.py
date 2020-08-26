from Gaudi.Configuration import importOptions
from Gaussino.Generation import GenPhase

from Configurables import Generation

# Beam options as in Beam6500GeV-md100-2016-nu1.6.py
importOptions("$APPCONFIGOPTS/Gauss/Beam7000GeV-mu100-nu7.6-HorExtAngle.py")

from Configurables import Gauss, CondDB

CondDB().Upgrade = True

# Add also the DDDB tag for now
from Configurables import LHCbApp
LHCbApp().DDDBtag = "dddb-20190223"
LHCbApp().CondDBtag = "sim-20180530-vc-mu100"
LHCbApp().DataType = "Upgrade"

# Configure the generation phase as usual
Generation().EventType = 30000000
GenPhase().SampleGenerationTool = "MinimumBias"
GenPhase().ProductionTool = "Pythia8ProductionMT"
GenPhase().DecayTool = "EvtGenDecay"

from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dsst_ppbarpi=TightCut.dec"
ToolSvc().EvtGenDecay.DecayFile = "$DECFILESROOT/dkfiles/DECAY.DEC"

from Configurables import Gauss, Gaussino
Gaussino().ConvertEDM = True
nthreads = 4
from Configurables import GiGaMT
GiGaMT().NumberOfWorkerThreads = nthreads
nskip = 2 + nthreads

Gauss().EvtMax = 10
Gauss().EnableHive = True
from Gaussino.Generation import GenPhase

Gauss().ThreadPoolSize = nthreads
Gauss().EventSlots = nthreads

from Configurables import GenRndInit
GenRndInit().FirstEventNumber =  3000

from Gauss.Geometry import LHCbGeo
# LHCbGeo().Debug = True  # Comment this in if you want a lot of debug output
# Set the list of detectors / detector elements
LHCbGeo().DetectorGeo = { "Detectors": ['VP', 'Magnet', 'Bls']}
LHCbGeo().DetectorSim = { "Detectors": ['VP', 'Magnet', 'Bls']}
LHCbGeo().DetectorMoni = { "Detectors": ['VP', 'Magnet', 'Bls']}
# LHCbGeo().SaveGDMLFile = "detector.gdml"
# Optional mapping of a sensitive detector factory to a G4 logical volume
# LHCbGeo().SensDetMap = {'GiGaSensDetTracker/VPSDet': ["lvDet"] }
# Activate global DD4hep flag, this results in the use of the DD4hep conversion service
# instead of GaussGeo
LHCbGeo().DD4hep = True

# Select and activate DD4hep for the subdetectors you want to
# This needs to be for the future functionalities where DetDesc and DD4hep can be mixed
# but is already needed now
from Gauss.Geometry.Helpers import getsubdetector
getsubdetector('VP').UseDD4hep = True
getsubdetector('BeamPipe').UseDD4hep = True
getsubdetector('Magnet').UseDD4hep = True
getsubdetector('Bls').UseDD4hep = True

# Comment in below to trigger a more verbose printout of the conversion service
# from Configurables import DD4hepCnvSvc
# from Gaudi.Configuration import VERBOSE
# DD4hepCnvSvc().OutputLevel = VERBOSE
# DD4hepCnvSvc().DebugMaterials = True
# DD4hepCnvSvc().DebugElements = True
# DD4hepCnvSvc().DebugShapes = True
# DD4hepCnvSvc().DebugVolumes = True
# DD4hepCnvSvc().DebugPlacements = True
# DD4hepCnvSvc().DebugRegions = True
# Gauss().DatasetName = "Gauss-DD4hep"

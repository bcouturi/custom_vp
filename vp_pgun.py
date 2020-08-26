
from Gaudi.Configuration import importOptions
from Gaussino.Generation import GenPhase
# Beam options as in Beam6500GeV-md100-2016-nu1.6.py
importOptions("$APPCONFIGOPTS/Gauss/Beam7000GeV-mu100-nu7.6-HorExtAngle.py")
from Configurables import Gauss, CondDB
CondDB().Upgrade = True
from Configurables import LHCbApp
LHCbApp().DDDBtag = "dddb-20190223"
LHCbApp().CondDBtag = "sim-20180530-vc-mu100"
LHCbApp().DataType = "Upgrade"
from Configurables import Gauss, Gaussino
Gaussino().ConvertEDM = True
nthreads = 4
# ParticleGun hack incoming
GenPhase().ParticleGun = True
def my_configure_pgun(self, seq):
    from GaudiKernel.SystemOfUnits import GeV, rad
    from Configurables import ParticleGun
    pgun = ParticleGun("ParticleGun")
    pgun.EventType = 53210205
    from Configurables import MomentumRange
    pgun.addTool(MomentumRange, name="MomentumRange")
    pgun.ParticleGunTool = "MomentumRange"
    from Configurables import FlatNParticles
    pgun.addTool(FlatNParticles, name="FlatNParticles")
    pgun.NumberOfParticlesTool = "FlatNParticles"
    pgun.FlatNParticles.MinNParticles = 1
    pgun.FlatNParticles.MaxNParticles = 1
    pgun.MomentumRange.PdgCodes = [-11]
    pgun.MomentumRange.MomentumMin = 2.0*GeV
    pgun.MomentumRange.MomentumMax = 100.0*GeV
    pgun.MomentumRange.ThetaMin = 0.015*rad
    pgun.MomentumRange.ThetaMax = 0.300*rad
    seq += [pgun]
GenPhase.configure_pgun = my_configure_pgun
from Configurables import GiGaMT
GiGaMT().NumberOfWorkerThreads = nthreads
nskip = 2 + nthreads
Gauss().EvtMax = 1000
Gauss().EnableHive = True
Gauss().ThreadPoolSize = nthreads
Gauss().EventSlots = nthreads
# from Configurables import GenReDecayInit
from Configurables import GenRndInit
GenRndInit().FirstEventNumber =  3000
from Configurables import GenRndInit
from Configurables import ReDecaySvc
from Gauss.Geometry import LHCbGeo
LHCbGeo().Debug = True
LHCbGeo().DetectorGeo = {
            "Detectors": ['VP']}
LHCbGeo().DetectorSim = {
            "Detectors": ['VP']}
LHCbGeo().DetectorMoni = {
            "Detectors": ['VP']}
LHCbGeo().DD4hep = True
from Gauss.Geometry.Helpers import getsubdetector
getsubdetector('VP').UseDD4hep = True
from Configurables import DD4hepCnvSvc
from Gaudi.Configuration import VERBOSE
DD4hepCnvSvc().OutputLevel = VERBOSE
DD4hepCnvSvc().DebugMaterials = True
DD4hepCnvSvc().DebugElements = True
DD4hepCnvSvc().DebugShapes = True
DD4hepCnvSvc().DebugVolumes = True
DD4hepCnvSvc().DebugPlacements = True
DD4hepCnvSvc().DebugRegions = True
Gauss().DatasetName = "Gauss-DD4hep"


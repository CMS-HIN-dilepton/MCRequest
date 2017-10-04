import FWCore.ParameterSet.Config as cms
generator = cms.EDFilter("Pythia8PtGun",
      PGunParameters = cms.PSet(
         MaxPt = cms.double(0.),
         MinPt = cms.double(50.),
         ParticleID = cms.vint32(443),
         MaxEta = cms.double(3),
         MaxPhi = cms.double(3.14159265359),
         MinEta = cms.double(-3),
         MinPhi = cms.double(-3.14159265359), ## in radians
         AddAntiParticle = cms.bool(False)
         ),
      Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts
      psethack = cms.string('single jpsi pt 50'),
      firstRun = cms.untracked.uint32(1),
      PythiaParameters = cms.PSet(
         jpsiDecay = cms.vstring(
            '443:onMode = off',
            '443:onIfAny = 13',
            ),
         parameterSets = cms.vstring('jpsiDecay')
         )
      )


import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("PyquenGeneratorFilter",
      PythiaParameters = cms.PSet(
         parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters'),
         processParameters = cms.vstring('MSEL      = 0      !User defined processes', 
            'MSUB(81)  = 1      ! qqbar to QQbar', 
            'MSUB(82)  = 1      ! gg to QQbar', 
            'MSTP(7)   = 6      ! flavour = top', 
            'PMAS(6,1) = 172.5  ! top quark mass', 
            'MDME(190,1) = 1    !W decay into dbar u', 
            'MDME(191,1) = 1    !W decay into dbar c', 
            'MDME(192,1) = 1    !W decay into dbar t', 
            'MDME(194,1) = 1    !W decay into sbar u', 
            'MDME(195,1) = 1    !W decay into sbar c', 
            'MDME(196,1) = 1    !W decay into sbar t', 
            'MDME(198,1) = 1    !W decay into bbar u', 
            'MDME(199,1) = 1    !W decay into bbar c', 
            'MDME(200,1) = 1    !W decay into bbar t', 
            'MDME(205,1) = 1    !W decay into bbar tp', 
            'MDME(206,1) = 1    !W decay into e+ nu_e', 
            'MDME(207,1) = 1    !W decay into mu+ nu_mu', 
            'MDME(208,1) = 1    !W decay into tau+ nu_tau'),
         pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model')
         ),
      aBeamTarget = cms.double(208.0),
      angularSpectrumSelector = cms.int32(0),
      bFixed = cms.double(0.0),
      bMax = cms.double(0.0),
      bMin = cms.double(0.0),
      backgroundLabel = cms.InputTag("generator"),
      cFlag = cms.int32(0),
      comEnergy = cms.double(8160.0),
      doCollisionalEnLoss = cms.bool(False),
      doIsospin = cms.bool(True),
      doQuench = cms.bool(False),
      doRadiativeEnLoss = cms.bool(True),
      embeddingMode = cms.bool(False),
      hadronFreezoutTemperature = cms.double(0.14),
      maxEventsToPrint = cms.untracked.int32(0),
      numQuarkFlavor = cms.int32(0),
      protonSide = cms.untracked.int32(2),
      pythiaHepMCVerbosity = cms.untracked.bool(True),
      pythiaPylistVerbosity = cms.untracked.int32(1),
      qgpInitialTemperature = cms.double(1.0),
      qgpNumQuarkFlavor = cms.int32(0),
      qgpProperTimeFormation = cms.double(0.1)
      )

ProductionFilterSequence = cms.Sequence(generator)

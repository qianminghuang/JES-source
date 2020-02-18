import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISummer16MiniAODv2/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FAA70706-CB04-E811-B995-901B0E542974.root'),
    secondaryFileNames = cms.untracked.vstring()
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
)

process.pfJetIDSelector = cms.PSet(
    quality = cms.string('LOOSE'),
    version = cms.string('WINTER16')
)

process.regressionModifier = cms.PSet(
    eOverP_ECALTRKThr = cms.double(0.025),
    ecalrechitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    ecalrechitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    electron_config = cms.PSet(
        regressionKey_ecalonly = cms.vstring('electron_eb_ECALonly_lowpt', 
            'electron_eb_ECALonly', 
            'electron_ee_ECALonly_lowpt', 
            'electron_ee_ECALonly'),
        regressionKey_ecaltrk = cms.vstring('electron_eb_ECALTRK_lowpt', 
            'electron_eb_ECALTRK', 
            'electron_ee_ECALTRK_lowpt', 
            'electron_ee_ECALTRK'),
        uncertaintyKey_ecalonly = cms.vstring('electron_eb_ECALonly_lowpt_var', 
            'electron_eb_ECALonly_var', 
            'electron_ee_ECALonly_lowpt_var', 
            'electron_ee_ECALonly_var'),
        uncertaintyKey_ecaltrk = cms.vstring('electron_eb_ECALTRK_lowpt_var', 
            'electron_eb_ECALTRK_var', 
            'electron_ee_ECALTRK_lowpt_var', 
            'electron_ee_ECALTRK_var')
    ),
    epDiffSig_ECALTRKThr = cms.double(15.0),
    epSig_ECALTRKThr = cms.double(10.0),
    highEnergy_ECALTRKThr = cms.double(200.0),
    lowEnergy_ECALTRKThr = cms.double(50.0),
    lowEnergy_ECALonlyThr = cms.double(300.0),
    modifierName = cms.string('EGExtraInfoModifierFromDBUser'),
    photon_config = cms.PSet(
        regressionKey_ecalonly = cms.vstring('photon_eb_ECALonly_lowpt', 
            'photon_eb_ECALonly', 
            'photon_ee_ECALonly_lowpt', 
            'photon_ee_ECALonly'),
        uncertaintyKey_ecalonly = cms.vstring('photon_eb_ECALonly_lowpt_var', 
            'photon_eb_ECALonly_var', 
            'photon_ee_ECALonly_lowpt_var', 
            'photon_ee_ECALonly_var')
    ),
    rhoCollection = cms.InputTag("fixedGridRhoFastjetAll"),
    useLocalFile = cms.bool(False)
)

process.egamma_modifications = cms.VPSet(cms.PSet(
    eOverP_ECALTRKThr = cms.double(0.025),
    ecalrechitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    ecalrechitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    electron_config = cms.PSet(
        regressionKey_ecalonly = cms.vstring('electron_eb_ECALonly_lowpt', 
            'electron_eb_ECALonly', 
            'electron_ee_ECALonly_lowpt', 
            'electron_ee_ECALonly'),
        regressionKey_ecaltrk = cms.vstring('electron_eb_ECALTRK_lowpt', 
            'electron_eb_ECALTRK', 
            'electron_ee_ECALTRK_lowpt', 
            'electron_ee_ECALTRK'),
        uncertaintyKey_ecalonly = cms.vstring('electron_eb_ECALonly_lowpt_var', 
            'electron_eb_ECALonly_var', 
            'electron_ee_ECALonly_lowpt_var', 
            'electron_ee_ECALonly_var'),
        uncertaintyKey_ecaltrk = cms.vstring('electron_eb_ECALTRK_lowpt_var', 
            'electron_eb_ECALTRK_var', 
            'electron_ee_ECALTRK_lowpt_var', 
            'electron_ee_ECALTRK_var')
    ),
    epDiffSig_ECALTRKThr = cms.double(15.0),
    epSig_ECALTRKThr = cms.double(10.0),
    highEnergy_ECALTRKThr = cms.double(200.0),
    lowEnergy_ECALTRKThr = cms.double(50.0),
    lowEnergy_ECALonlyThr = cms.double(300.0),
    modifierName = cms.string('EGExtraInfoModifierFromDBUser'),
    photon_config = cms.PSet(
        regressionKey_ecalonly = cms.vstring('photon_eb_ECALonly_lowpt', 
            'photon_eb_ECALonly', 
            'photon_ee_ECALonly_lowpt', 
            'photon_ee_ECALonly'),
        uncertaintyKey_ecalonly = cms.vstring('photon_eb_ECALonly_lowpt_var', 
            'photon_eb_ECALonly_var', 
            'photon_ee_ECALonly_lowpt_var', 
            'photon_ee_ECALonly_var')
    ),
    rhoCollection = cms.InputTag("fixedGridRhoFastjetAll"),
    useLocalFile = cms.bool(False)
))

process.Wtoenu = cms.EDProducer("PKUWLepProducer",
    MET = cms.InputTag("slimmedMETs"),
    cut = cms.string(''),
    leptons = cms.InputTag("goodElectrons")
)


process.Wtomunu = cms.EDProducer("PKUWLepProducer",
    MET = cms.InputTag("slimmedMETs"),
    cut = cms.string(''),
    leptons = cms.InputTag("goodMuons")
)


process.calibratedPatElectrons = cms.EDProducer("CalibratedPatElectronProducerRun2",
    autoDataType = cms.bool(True),
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Moriond17_23Jan_ele'),
    electrons = cms.InputTag("slimmedElectrons"),
    gbrForestName = cms.vstring('electron_eb_ECALTRK_lowpt', 
        'electron_eb_ECALTRK', 
        'electron_ee_ECALTRK_lowpt', 
        'electron_ee_ECALTRK', 
        'electron_eb_ECALTRK_lowpt_var', 
        'electron_eb_ECALTRK_var', 
        'electron_ee_ECALTRK_lowpt_var', 
        'electron_ee_ECALTRK_var'),
    isMC = cms.bool(True),
    isSynchronization = cms.bool(False),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits")
)


process.calibratedPatPhotons = cms.EDProducer("CalibratedPatPhotonProducerRun2",
    autoDataType = cms.bool(True),
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Moriond17_23Jan_ele'),
    isMC = cms.bool(True),
    isSynchronization = cms.bool(False),
    photons = cms.InputTag("slimmedPhotons"),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits")
)


process.cleanAK4Jets = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.4),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("goodElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.4),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("goodMuons")
        ),
        photons = cms.PSet(

        ),
        taus = cms.PSet(

        ),
        tkIsoElectrons = cms.PSet(

        )
    ),
    finalCut = cms.string('pt > 20 && abs(eta) < 4.7'),
    preselection = cms.string(''),
    src = cms.InputTag("goodAK4Jets")
)


process.goodElectrons = cms.EDProducer("PATElectronIdSelector",
    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
    idLabel = cms.string('tight'),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedElectrons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.goodMuons = cms.EDProducer("PATMuonIdSelector",
    idLabel = cms.string('tight'),
    src = cms.InputTag("slimmedMuons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.leptonicV = cms.EDProducer("CandViewMerger",
    cut = cms.string(''),
    src = cms.VInputTag("Wtoenu", "Wtomunu")
)


process.looseMuons = cms.EDProducer("PATMuonIdSelector",
    idLabel = cms.string('loose'),
    src = cms.InputTag("slimmedMuons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.modifiedElectrons = cms.EDProducer("ModifiedElectronProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.modifiedPhotons = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.prefiringweight = cms.EDProducer("L1ECALPrefiringWeightProducer",
    DataEra = cms.string('2016BtoH'),
    L1Maps = cms.string('CMSSW_8_0_32/src/L1Prefiring/EventWeightProducer/data/L1PrefiringMaps_new.root'),
    PrefiringRateSystematicUncty = cms.double(0.2),
    TheJets = cms.InputTag("slimmedJets"),
    ThePhotons = cms.InputTag("slimmedPhotons"),
    UseJetEMPt = cms.bool(False)
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.slimmedElectrons = cms.EDProducer("ModifiedElectronProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(cms.PSet(
            eOverP_ECALTRKThr = cms.double(0.025),
            ecalrechitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
            ecalrechitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
            electron_config = cms.PSet(
                regressionKey_ecalonly = cms.vstring('electron_eb_ECALonly_lowpt', 
                    'electron_eb_ECALonly', 
                    'electron_ee_ECALonly_lowpt', 
                    'electron_ee_ECALonly'),
                regressionKey_ecaltrk = cms.vstring('electron_eb_ECALTRK_lowpt', 
                    'electron_eb_ECALTRK', 
                    'electron_ee_ECALTRK_lowpt', 
                    'electron_ee_ECALTRK'),
                uncertaintyKey_ecalonly = cms.vstring('electron_eb_ECALonly_lowpt_var', 
                    'electron_eb_ECALonly_var', 
                    'electron_ee_ECALonly_lowpt_var', 
                    'electron_ee_ECALonly_var'),
                uncertaintyKey_ecaltrk = cms.vstring('electron_eb_ECALTRK_lowpt_var', 
                    'electron_eb_ECALTRK_var', 
                    'electron_ee_ECALTRK_lowpt_var', 
                    'electron_ee_ECALTRK_var')
            ),
            epDiffSig_ECALTRKThr = cms.double(15.0),
            epSig_ECALTRKThr = cms.double(10.0),
            highEnergy_ECALTRKThr = cms.double(200.0),
            lowEnergy_ECALTRKThr = cms.double(50.0),
            lowEnergy_ECALonlyThr = cms.double(300.0),
            modifierName = cms.string('EGExtraInfoModifierFromDBUser'),
            photon_config = cms.PSet(
                regressionKey_ecalonly = cms.vstring('photon_eb_ECALonly_lowpt', 
                    'photon_eb_ECALonly', 
                    'photon_ee_ECALonly_lowpt', 
                    'photon_ee_ECALonly'),
                uncertaintyKey_ecalonly = cms.vstring('photon_eb_ECALonly_lowpt_var', 
                    'photon_eb_ECALonly_var', 
                    'photon_ee_ECALonly_lowpt_var', 
                    'photon_ee_ECALonly_var')
            ),
            rhoCollection = cms.InputTag("fixedGridRhoFastjetAll"),
            useLocalFile = cms.bool(False)
        ))
    ),
    src = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.slimmedPhotons = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(cms.PSet(
            eOverP_ECALTRKThr = cms.double(0.025),
            ecalrechitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
            ecalrechitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
            electron_config = cms.PSet(
                regressionKey_ecalonly = cms.vstring('electron_eb_ECALonly_lowpt', 
                    'electron_eb_ECALonly', 
                    'electron_ee_ECALonly_lowpt', 
                    'electron_ee_ECALonly'),
                regressionKey_ecaltrk = cms.vstring('electron_eb_ECALTRK_lowpt', 
                    'electron_eb_ECALTRK', 
                    'electron_ee_ECALTRK_lowpt', 
                    'electron_ee_ECALTRK'),
                uncertaintyKey_ecalonly = cms.vstring('electron_eb_ECALonly_lowpt_var', 
                    'electron_eb_ECALonly_var', 
                    'electron_ee_ECALonly_lowpt_var', 
                    'electron_ee_ECALonly_var'),
                uncertaintyKey_ecaltrk = cms.vstring('electron_eb_ECALTRK_lowpt_var', 
                    'electron_eb_ECALTRK_var', 
                    'electron_ee_ECALTRK_lowpt_var', 
                    'electron_ee_ECALTRK_var')
            ),
            epDiffSig_ECALTRKThr = cms.double(15.0),
            epSig_ECALTRKThr = cms.double(10.0),
            highEnergy_ECALTRKThr = cms.double(200.0),
            lowEnergy_ECALTRKThr = cms.double(50.0),
            lowEnergy_ECALonlyThr = cms.double(300.0),
            modifierName = cms.string('EGExtraInfoModifierFromDBUser'),
            photon_config = cms.PSet(
                regressionKey_ecalonly = cms.vstring('photon_eb_ECALonly_lowpt', 
                    'photon_eb_ECALonly', 
                    'photon_ee_ECALonly_lowpt', 
                    'photon_ee_ECALonly'),
                uncertaintyKey_ecalonly = cms.vstring('photon_eb_ECALonly_lowpt_var', 
                    'photon_eb_ECALonly_var', 
                    'photon_ee_ECALonly_lowpt_var', 
                    'photon_ee_ECALonly_var')
            ),
            rhoCollection = cms.InputTag("fixedGridRhoFastjetAll"),
            useLocalFile = cms.bool(False)
        ))
    ),
    src = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.vetoElectrons = cms.EDProducer("PATElectronIdSelector",
    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
    idLabel = cms.string('veto'),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedElectrons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.BadChargedCandidateFilter = cms.EDFilter("BadParticleFilter",
    PFCandidates = cms.InputTag("packedPFCandidates"),
    filterType = cms.string('BadChargedCandidate'),
    innerTrackRelErr = cms.double(1.0),
    maxDR = cms.double(1e-05),
    minMuonPt = cms.double(100.0),
    minMuonTrackRelErr = cms.double(2.0),
    minPtDiffRel = cms.double(1e-05),
    muons = cms.InputTag("slimmedMuons"),
    segmentCompatibility = cms.double(0.3),
    taggingMode = cms.bool(False)
)


process.BadPFMuonFilter = cms.EDFilter("BadParticleFilter",
    PFCandidates = cms.InputTag("packedPFCandidates"),
    algo = cms.int32(14),
    filterType = cms.string('BadPFMuon'),
    innerTrackRelErr = cms.double(1.0),
    maxDR = cms.double(0.001),
    minMuonPt = cms.double(100),
    minMuonTrackRelErr = cms.double(2.0),
    minPtDiffRel = cms.double(0.0),
    muons = cms.InputTag("slimmedMuons"),
    segmentCompatibility = cms.double(0.3),
    taggingMode = cms.bool(False)
)


process.goodAK4Jets = cms.EDFilter("PFJetIDSelectionFunctorFilter",
    filterParams = cms.PSet(
        quality = cms.string('LOOSE'),
        version = cms.string('WINTER16')
    ),
    src = cms.InputTag("slimmedJets")
)


process.goodPhotons = cms.EDFilter("PATPhotonSelector",
    cut = cms.string('pt > 15 && fabs(eta) < 2.5'),
    src = cms.InputTag("slimmedPhotons")
)


process.leptonicVFilter = cms.EDFilter("CandViewCountFilter",
    filter = cms.bool(False),
    minNumber = cms.uint32(0),
    src = cms.InputTag("leptonicV")
)


process.leptonicVSelector = cms.EDFilter("CandViewSelector",
    cut = cms.string('pt > 0.0'),
    filter = cms.bool(False),
    src = cms.InputTag("leptonicV")
)


process.treeDumper = cms.EDAnalyzer("PKUTreeMaker",
    PKUChannel = cms.string('VW_CHANNEL'),
    RunOnMC = cms.bool(True),
    ak4jetsSrc = cms.InputTag("cleanAK4Jets"),
    beamSpot = cms.InputTag("offlineBeamSpot","","RECO"),
    conversions = cms.InputTag("reducedEgamma","reducedConversions","PAT"),
    crossSectionPb = cms.double(1),
    effAreaChHadFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfChargedHadrons_25ns_NULLcorrection.txt'),
    effAreaNeuHadFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfNeutralHadrons_25ns_90percentBased.txt'),
    effAreaPhoFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfPhotons_25ns_90percentBased.txt'),
    elPaths1 = cms.vstring('HLT_Ele23_WPTight_Gsf_v*'),
    elPaths2 = cms.vstring('HLT_Ele27_WPTight_Gsf_v*'),
    electrons = cms.InputTag("slimmedElectrons"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    genSrc = cms.InputTag("prunedGenParticles"),
    generator = cms.InputTag("generator"),
    hltToken = cms.InputTag("TriggerResults","","HLT"),
    isGen = cms.bool(False),
    jecAK4PayloadNames = cms.vstring('Summer16_23Sep2016V4_MC_L1FastJet_AK4PFchs.txt', 
        'Summer16_23Sep2016V4_MC_L2Relative_AK4PFchs.txt', 
        'Summer16_23Sep2016V4_MC_L3Absolute_AK4PFchs.txt'),
    jecAK4chsPayloadNames = cms.vstring('Summer16_23Sep2016V4_MC_L1FastJet_AK4PFchs.txt', 
        'Summer16_23Sep2016V4_MC_L2Relative_AK4PFchs.txt', 
        'Summer16_23Sep2016V4_MC_L3Absolute_AK4PFchs.txt'),
    leptonicVSrc = cms.InputTag("leptonicV"),
    lhe = cms.InputTag("externalLHEProducer"),
    looseelectronSrc = cms.InputTag("vetoElectrons"),
    loosemuonSrc = cms.InputTag("looseMuons"),
    metSrc = cms.InputTag("slimmedMETs"),
    muPaths1 = cms.vstring('HLT_IsoMu20_v*', 
        'HLT_IsoTkMu20_v*'),
    muPaths2 = cms.vstring('HLT_IsoMu24_v*', 
        'HLT_IsoTkMu24_v*'),
    muPaths3 = cms.vstring('HLT_IsoMu27_v*', 
        'HLT_IsoTkMu27_v*'),
    noiseFilter = cms.InputTag("TriggerResults","","PAT"),
    noiseFilterSelection_EcalDeadCellTriggerPrimitiveFilter = cms.string('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    noiseFilterSelection_HBHENoiseFilter = cms.string('Flag_HBHENoiseFilter'),
    noiseFilterSelection_HBHENoiseIsoFilter = cms.string('Flag_HBHENoiseIsoFilter'),
    noiseFilterSelection_badChargedHadron = cms.InputTag("BadChargedCandidateFilter"),
    noiseFilterSelection_badMuon = cms.InputTag("BadPFMuonFilter"),
    noiseFilterSelection_eeBadScFilter = cms.string('Flag_eeBadScFilter'),
    noiseFilterSelection_globalTightHaloFilter = cms.string('Flag_globalTightHalo2016Filter'),
    noiseFilterSelection_goodVertices = cms.string('Flag_goodVertices'),
    originalNEvents = cms.int32(1),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    photonSrc = cms.InputTag("slimmedPhotons"),
    pileup = cms.InputTag("slimmedAddPileupInfo"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    t1jetSrc = cms.InputTag("slimmedJets"),
    t1muSrc = cms.InputTag("slimmedMuons"),
    targetLumiInvPb = cms.double(1.0),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.eleSequence = cms.Sequence(process.goodElectrons+process.vetoElectrons)


process.muSequence = cms.Sequence(process.goodMuons+process.looseMuons)


process.leptonicVSequence = cms.Sequence(process.Wtomunu+process.Wtoenu+process.leptonicV)


process.NJetsSequence = cms.Sequence(process.goodAK4Jets+process.cleanAK4Jets)


process.regressionApplication = cms.Sequence(process.slimmedElectrons+process.slimmedPhotons)


process.photonSequence = cms.Sequence(process.goodPhotons)


process.metfilterSequence = cms.Sequence(process.BadPFMuonFilter+process.BadChargedCandidateFilter)


process.jetSequence = cms.Sequence(process.NJetsSequence)


process.leptonSequence = cms.Sequence(process.muSequence+process.eleSequence+process.leptonicVSequence+process.leptonicVSelector+process.leptonicVFilter)


process.analysis = cms.Path(process.leptonSequence+process.jetSequence+process.metfilterSequence+process.photonIDValueMapProducer+process.prefiringweight+process.treeDumper)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(99999999),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(200)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    calibratedPatElectrons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(81)
    ),
    calibratedPatPhotons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(81)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('treePKU.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v8'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
        label = cms.untracked.string('electron_eb_ECALonly'),
        record = cms.string('GBRDWrapperRcd'),
        tag = cms.string('GEDelectron_EBCorrection_80X_EGM_v4')
    ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_eb_ECALonly_lowpt'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_lowpt_EBCorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_eb_ECALonly_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_EBUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_eb_ECALonly_lowpt_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_lowpt_EBUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_ee_ECALonly'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_EECorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_ee_ECALonly_lowpt'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_lowpt_EECorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_ee_ECALonly_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_EEUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_ee_ECALonly_lowpt_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_lowpt_EEUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_eb_ECALTRK'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_track_EBCorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_eb_ECALTRK_lowpt'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_track_lowpt_EBCorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_eb_ECALTRK_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_track_EBUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_eb_ECALTRK_lowpt_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_track_lowpt_EBUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_ee_ECALTRK'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_track_EECorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_ee_ECALTRK_lowpt'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_track_lowpt_EECorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_ee_ECALTRK_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_track_EEUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('electron_ee_ECALTRK_lowpt_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDelectron_track_lowpt_EEUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('photon_eb_ECALonly'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDphoton_EBCorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('photon_eb_ECALonly_lowpt'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDphoton_lowpt_EBCorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('photon_eb_ECALonly_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDphoton_EBUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('photon_eb_ECALonly_lowpt_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDphoton_lowpt_EBUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('photon_ee_ECALonly'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDphoton_EECorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('photon_ee_ECALonly_lowpt'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDphoton_lowpt_EECorrection_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('photon_ee_ECALonly_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDphoton_EEUncertainty_80X_EGM_v4')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('photon_ee_ECALonly_lowpt_var'),
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('GEDphoton_lowpt_EEUncertainty_80X_EGM_v4')
        ))
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    iLumi = cms.double(-1.0),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.prefer("es_hardcode")


_VEH_CELL_RESULTS_PUBLIC = ('health', 'credits', 'xp', 'achievementCredits', 'achievementXP', 'achievementFreeXP', 'shots', 'directHits', 'directTeamHits', 'explosionHits', 'piercings', 'damageDealt', 'sniperDamageDealt', 'damageAssistedRadio', 'damageAssistedTrack', 'damageReceived', 'damageBlockedByArmor', 'directHitsReceived', 'noDamageDirectHitsReceived', 'explosionHitsReceived', 'piercingsReceived', 'spotted', 'damaged', 'kills', 'tdamageDealt', 'tdestroyedModules', 'tkills', 'isTeamKiller', 'capturePoints', 'droppedCapturePoints', 'mileage', 'lifeTime', 'killerID', 'achievements', 'potentialDamageReceived', 'isPrematureLeave', 'fortResource', 'damaged_while_moving', 'killed_while_moving', 'assistedDamage', 'assistedKills', 'critsByType', 'innerModuleCritCount')
_VEH_CELL_RESULTS_PRIVATE = ('repair', 'freeXP', 'details')
_VEH_CELL_RESULTS_SERVER = ('protoAchievements', 'potentialDamageDealt', 'soloHitsAssisted', 'isEnemyBaseCaptured', 'stucks', 'autoAimedShots', 'presenceTime', 'spot_list', 'damage_list', 'damage_list_with_damage', 'kill_list', 'ammo', 'crewActivityFlags', 'series', 'tkillRating', 'tkillLog', 'destroyedObjects', 'committedSuicide', 'discloseShots', 'guerrillaShots', 'critsCount', 'aimerSeries')
VEH_CELL_RESULTS = _VEH_CELL_RESULTS_PUBLIC + _VEH_CELL_RESULTS_PRIVATE + _VEH_CELL_RESULTS_SERVER
VEH_CELL_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_CELL_RESULTS)))
_VEH_BASE_RESULTS_PUBLIC = ('accountDBID', 'team', 'typeCompDescr', 'gold', 'deathReason', 'fortBuilding')
_VEH_BASE_RESULTS_PRIVATE = ('xpPenalty', 'creditsPenalty', 'creditsContributionIn', 'creditsContributionOut', 'creditsToDraw')
_VEH_BASE_RESULTS_SERVER = ('eventIndices', 'vehLockTimeFactor', 'misc', 'cybersportRatingDeltas', 'clanDBID')
VEH_BASE_RESULTS = _VEH_CELL_RESULTS_PUBLIC + _VEH_BASE_RESULTS_PUBLIC + _VEH_CELL_RESULTS_PRIVATE + _VEH_BASE_RESULTS_PRIVATE + _VEH_CELL_RESULTS_SERVER + _VEH_BASE_RESULTS_SERVER
VEH_BASE_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_BASE_RESULTS)))
VEH_PUBLIC_RESULTS = _VEH_CELL_RESULTS_PUBLIC + _VEH_BASE_RESULTS_PUBLIC
VEH_PUBLIC_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_PUBLIC_RESULTS)))
VEH_FULL_RESULTS_UPDATE = ('tmenXP', 'isPremium', 'eventCredits', 'eventGold', 'eventXP', 'eventFreeXP', 'eventTMenXP', 'autoRepairCost', 'autoLoadCost', 'autoEquipCost', 'histAmmoCost', 'premiumVehicleXP', 'premiumXPFactor10', 'premiumCreditsFactor10', 'dailyXPFactor10', 'igrXPFactor10', 'aogasFactor10', 'markOfMastery', 'dossierPopUps', 'vehTypeLockTime', 'serviceProviderID', 'marksOnGun', 'movingAvgDamage', 'damageRating', 'orderCredits', 'orderXP', 'orderTMenXP', 'orderFreeXP', 'orderFortResource', 'fairplayViolations', 'refSystemXPFactor10')
VEH_FULL_RESULTS_UPDATE_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_FULL_RESULTS_UPDATE)))
_VEH_FULL_RESULTS_PRIVATE = ('originalCredits', 'originalXP', 'originalFreeXP', 'questsProgress')
VEH_FULL_RESULTS_SERVER = ('eventGoldByEventID',)
VEH_FULL_RESULTS = _VEH_CELL_RESULTS_PUBLIC + _VEH_BASE_RESULTS_PUBLIC + _VEH_CELL_RESULTS_PRIVATE + _VEH_BASE_RESULTS_PRIVATE + VEH_FULL_RESULTS_UPDATE + _VEH_FULL_RESULTS_PRIVATE
VEH_FULL_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEH_FULL_RESULTS)))
PLAYER_INFO = ('name', 'clanDBID', 'clanAbbrev', 'prebattleID', 'team', 'igrType')
PLAYER_INFO_INDICES = dict(((x[1], x[0]) for x in enumerate(PLAYER_INFO)))
COMMON_RESULTS = ('arenaTypeID', 'arenaCreateTime', 'winnerTeam', 'finishReason', 'duration', 'bonusType', 'guiType', 'vehLockMode', 'sortieDivision')
COMMON_RESULTS_INDICES = dict(((x[1], x[0]) for x in enumerate(COMMON_RESULTS)))
handled = 1 

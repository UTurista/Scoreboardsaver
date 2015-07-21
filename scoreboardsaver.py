#
# Server Scoreboard Saver
# - It saves the information of each player in the end of each round
# 
# By: UTurista
#


# =======================================================
# ===============   CONFIGURATION   =====================
# =======================================================
record_folder = '/logs/' 
record_extension = '.log'



# =======================================================
# ===================   CODE   ==========================
# =======================================================

import host
import bf2

from datetime import datetime

 
def init():
  host.registerGameStatusHandler(onGameStatusChanged)


def deinit():
  host.unregisterGameStatusHandler(onGameStatusChanged)


json_separator = ','
def onGameStatusChanged(status):
  if status == bf2.GameStatus.EndGame:
    now = datetime.now()
    path = host.sgl_getModDirectory() + record_folder + str(bf2.gameLogic.getMapName()) + '_' + str(now.day) + str(now.hour) + str(now.minute) + record_extension
    
    try:
      f = open(path,'w+')
      json = '['

      # Available values:
      #('deaths','kills','TKs','score','skillScore','rplScore','cmdScore','fracScore','rank','firstPlace','secondPlace','thirdPlace',
      #	'bulletsFired','bulletsGivingDamage','bulletsFiredAndClear','bulletsGivingDamageAndClear')
      first = 1
      for p in bf2.playerManager.getPlayers():
        try:
            name = p.getName()
            deaths = str(p.score.__getattr__('deaths'))
            kills = str(p.score.__getattr__('kills'))
            wounded = str(p.isManDown());
        except Exception, e:
            name = str(e)
            kills = 'Invalid'
            deaths = 'Invalid'
            wounded = 'Invalid'
  
        if first:
          first = 0
          json += '{'
        else:
          json += ',{'
          
        json += '"name":"' + name  + '"' + json_separator
        json += '"deaths":"' + deaths  + '"' + json_separator
        json += '"wounded":"' + wounded  + '"' + json_separator
        json += '"kills":"' + kills + '"'
        json += '}'
        
      json += ']'
      f.write(json)
      f.close()


    except Exception, e:
      try:
        f = open(path,'w+')
        f.write(str(e))
        f.close()
      except : pass
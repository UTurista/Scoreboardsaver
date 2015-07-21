# Scoreboard Saver

Battelfield 2 module to record the scoreboard at the end of the round. Usefull to see past the hardcoded 20 players in the final ingame scoreboard.

At the end of each round, a file will be created with named `<mapName>_<day>_<hour>_<minute>.log` and with a JSON structured content.


##Usage
In the file:
`<mod>\python\game\__init__.py`
where _<mod>_ is the modification in use (eg:  _pr_ or _bf2_), add the following: 
```python
import scoreboardsaver
scoreboardsaver.init()
```
in the same folder `<mod>\python\game\` add the file [scoreboardsaver.py](https://github.com/Vascko/Scoreboardsaver/blob/master/scoreboardsaver.py) 

##Configuration
`record_folder` -  Will change where the information is saved
###Available stats
* deaths
* kills
* TKs
* score
* skillScore
* rplScore
* cmdScore
* fracScore
* rank
* firstPlace
* secondPlace
* thirdPlace
* bulletsFired
* bulletsGivingDamage
* bulletsFiredAndClear
* bulletsGivingDamageAndClear
* isAIPlayer
* alive
* mandown
* connected
* fholder (holds Flag)
* team
* ping
* suicide
* sqid (squad ID)
* isql  (is Squad Leader)
* commander  (is Commander)
* name


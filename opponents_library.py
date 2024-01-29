from enum import Enum


class OpponentType(Enum):
    MS1 = ('M', "MS1", 100, 25, 3)
    T28 = ('T', "T28", 200, 45, 4)
    KV85 = ('K', "KV85", 300, 60, 5)
    IS3 = ('I', "IS3", 400, 80, 6)
    O277 = ('O', "O277", 800, 120, 7)
class OpponentLvl1:
    opponentlv1 = [OpponentType.MS1, OpponentType.MS1, OpponentType.MS1, OpponentType.MS1, OpponentType.MS1]

class OpponentLvl2:
    opponentlv2 = [OpponentType.MS1, OpponentType.MS1, OpponentType.MS1, OpponentType.T28, OpponentType.T28]

class OpponentLvl3:
    opponentlv3 = [OpponentType.T28, OpponentType.T28, OpponentType.KV85, OpponentType.KV85, OpponentType.KV85]

class OpponentLvl4:
    opponentlv4 = [OpponentType.KV85, OpponentType.T28, OpponentType.KV85, OpponentType.IS3, OpponentType.IS3]

class OpponentLvl5:
    opponentlv5 = [OpponentType.T28, OpponentType.IS3, OpponentType.KV85, OpponentType.IS3, OpponentType.O277]

class OpponentLvl6:
    opponentlv6 = [OpponentType.IS3, OpponentType.O277, OpponentType.KV85, OpponentType.T28, OpponentType.T28]

class OpponentLvl7:
    opponentlv7 = [OpponentType.IS3, OpponentType.O277, OpponentType.KV85, OpponentType.IS3, OpponentType.O277]

class OpponentLvl8:
    opponentlv8 = [OpponentType.O277, OpponentType.O277, OpponentType.O277, OpponentType.O277, OpponentType.IS3]

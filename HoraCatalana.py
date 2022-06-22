from datetime import datetime as dt
from sys import prefix

class HoraCatalana:
    def __init__(self, _dt = None):
        self.dt = _dt if _dt else None
        self.strHoraCat = None
        

        self.dictHora = {
            0: 'dotze',
            1: 'una',
            2: 'dues',
            3: 'tres',
            4: 'quatre',
            5: 'cinc',
            6: 'sis',
            7: 'set',
            8: 'vuit',
            9: 'nou',
            10: 'deu',
            11: 'onze'
        }

        self.dictMin = {
            1: 'un',
            2: 'dos',
            3: 'tres',
            4: 'quatre',
            5: 'cinc',
            6: 'sis',
            7: 'set',
            8: 'vuit',
            9: 'nou',
        }

        self.rangPrefixMinutsPlural = [
            0, 1, 2, 3, 4, 5, 6, 8, 9, 53, 54, 55, 56, 57, 58, 59]

        if not _dt:
            self.tic()
        else:
            self.updateFrase()

    def updateFrase(self):
        self.strHoraCat = self.frase(
            h = int("{0:%H}".format( self.dt )),
            m = int("{0:%M}".format( self.dt ))
        )

    def tic(self):
        self.dt = dt.now()
        self.updateFrase()

    def prefixHora(self, _h):
        h = _h % 12

        prefixos = {
            'prefix1': None,
            'prefix2': None,
            'horaText': self.dictHora[h]
        }

        if h == 1:
            prefixos['prefix1'] = "d'"
            prefixos['prefix2'] = "la "
        elif h == 11:
            prefixos['prefix1'] = "d'"
            prefixos['prefix2'] = "les "
        else:
            prefixos['prefix1'] = "de "
            prefixos['prefix2'] = "les "

        return prefixos

    def pluralMin(self, m):
        return 'minut' if m == 1 else 'minuts'

    def pluralFalta(self, m):
        return 'Falta' if m == 1 else 'Falten'

    def quart(self, m):
        if m not in [15, 30, 45]:
            raise Exception("Minuts no vàlids, no són 15, 30 ni 45")

        ret = {'prefix': None, 'q': None}
        if m == 15:
            ret['prefix'] = "un"
            ret['q'] = "quart"
        if m == 30:
            ret['prefix'] = "dos"
            ret['q'] = "quarts"
        if m == 45:
            ret['prefix'] = "tres"
            ret['q'] = "quarts"

        return ret

    def stringPreviQuart(self, m, properQuart, prefix, hora):
        txt = "{0} {1} {2} per {3} {4} {5}{6}".format(
            self.pluralFalta(properQuart-m),
            self.dictMin[properQuart-m],
            self.pluralMin(properQuart-m),
            self.quart(properQuart)['prefix'],
            self.quart(properQuart)['q'],
            prefix,
            hora
        )
        return txt

    def stringPostQuart(self, m, quartPassat, prefix, hora):
        txt = "Són {0} {1} i {2} {3}{4}".format(
            self.quart(quartPassat)['prefix'],
            self.quart(quartPassat)['q'],
            self.dictMin[m-quartPassat] if (m-quartPassat) != 1 else 'u',
            prefix,
            hora
        )
        return txt


    def frase(self, h, m):
        if m not in range(0, 60):
            raise Exception("Minut fora del rang 00-59")

        txt = None
        hora = self.prefixHora(h)['horaText']
        prefix = None

        if m in self.rangPrefixMinutsPlural:
            prefix = self.prefixHora(h)['prefix2']
        else:
            prefix = self.prefixHora(h)['prefix1']

        if m == 0:
            txt = "Són {0}{1} en punt".format(prefix, hora)
        elif m in [1, 2, 3, 4, 5, 6, 8, 9]:
            txt = "Són {0}{1} i {2} {3}".format(prefix, hora, self.dictMin[m], self.pluralMin(m))
        elif m == 7:
            txt = "Són mig quart {0}{1}".format(prefix, hora)
        elif m in range(10, 15):
            txt = self.stringPreviQuart(m, 15, prefix, hora)
        elif m in range(23, 30):
            txt = self.stringPreviQuart(m, 30, prefix, hora)
        elif m in range(38, 45):
            txt = self.stringPreviQuart(m, 45, prefix, hora)
        elif m in [15, 30, 45]:
            txt = "Són {0} {1} {2}{3}".format(self.quart(m)['prefix'], self.quart(m)['q'], prefix, hora)
        elif m in [22, 37, 52]:
            txt = "Són {0} {1} i mig {2}{3}".format(self.quart(m-7)['prefix'], self.quart(m-7)['q'], prefix, hora)
        elif m in range(16, 22):
            txt = self.stringPostQuart(m, 15, prefix, hora)
        elif m in range(31, 37):
            txt = self.stringPostQuart(m, 30, prefix, hora)
        elif m in range(46, 52):
            txt = self.stringPostQuart(m, 45, prefix, hora)
        elif m in range(53,60):
            h += 1
            hora = self.prefixHora(h)['horaText']
            txt = "{0} {1} {2} per {3}{4}".format(self.pluralFalta(60-m), self.dictMin[60-m], self.pluralMin(60-m), prefix, hora)
        else:
            txt = "ERROR"

        return txt

    def __str__(self):
        return self.strHoraCat

    __repr__ = __str__



if __name__ == "__main__":
    # hc1 = HoraCatalana()
    # hc2 = HoraCatalana(dt(2015, 1, 1, 12, 30, 59, 0))
    
    # Test:
    hc = HoraCatalana()
    for _h in range(0, 24):
        for _m in range(0, 60):
            strtest = "{0:02d}:{1:02d} --> {2}".format(_h, _m, hc.frase(_h, _m))
            print(strtest)

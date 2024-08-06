# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
#     Copyright (c) 2023+ TYPETR
#     Usage by MIT License
# ..............................................................................
#
#   TYPETR_full_set.py
#
#   This is an example of a glyphset definition, derived from another one.
#   Don't forget to make a deepcopy first, before altering anything.
#
from copy import deepcopy

if __name__ == '__main__': # Used for doc tests to find assistantLib
    import os, sys
    PATH = '/'.join(__file__.split('/')[:-4]) # Relative path to this respository that holds AssistantLib
    if not PATH in sys.path:
        sys.path.append(PATH)

from assistantLib.assistantModules.glyphsets.glyphData import * #GD, TOP, TOP_, _BOTTOM, BOTTOM_ etc.
from assistantLib.assistantModules.glyphsets.TYPETR_full_set import TYPETR_FULL_SET

TYPETR_UPGRADENEON_SET_NAME = 'TYPETR UpgradeNeon set'

# The "c" attribtes are redundant, if the @uni or @hex atre defined, but they offer easy searching in the source by char.

TYPETR_UPGRADENEON_SET = GDS = deepcopy(TYPETR_FULL_SET)

# Add missing glyphs for Neon that are not in the TYPETR_full_set
GDS['Euro.lc'] = GD(name='Euro.lc')
GDS['J.base_sc'] = GD(name='J.base_sc')
GDS['Ruble'] = GD(name='Ruble')
GDS['Sigma'] = GD(name='Sigma')
GDS['Won'] = GD(name='Won')
GDS['a.alt'] = GD(name='a.alt')
GDS['a.sinf'] = GD(name='a.sinf', base='a.sups')
GDS['a.sups'] = GD(name='a.sups')
GDS['aacute.alt'] = GD(name='aacute.alt', base='a.alt', accents=('acutecmb'))
GDS['abreve.alt'] = GD(name='abreve.alt', base='a.alt', accents=('brevecmb'))
GDS['acircumflex.alt'] = GD(name='acircumflex.alt', base='a.alt', accents=('circumflexcmb'))
GDS['adieresis.alt'] = GD(name='adieresis.alt', base='a.alt', accents=('dieresiscmb'))
GDS['ae.alt'] = GD(name='ae.alt')
GDS['agrave.alt'] = GD(name='agrave.alt', base='a.alt', accents=('gravecmb'))
GDS['amacron.alt'] = GD(name='amacron.alt', base='a.alt', accents=('macroncmb'))
GDS['aogonek.alt'] = GD(name='aogonek.alt', base='a.alt', accents=('ogonekcmb'))
GDS['apple'] = GD(name='apple')
GDS['approxequal.lc'] = GD(name='approxequal.lc', base='approxequal')
GDS['approxequal.tab'] = GD(name='approxequal.tab', base='approxequal')
GDS['aring.alt'] = GD(name='aring.alt', base='a.alt', accents=('ringcmb'))
GDS['aringacute.alt'] = GD(name='aringacute.alt', base='a.alt', accents=('ringcmb_acutecmb'))
GDS['atilde.alt'] = GD(name='atilde.alt', base='a.alt', accents=('tildecmb'))
GDS['b.sinf'] = GD(name='b.sinf', base='b.sups')
GDS['b.sups'] = GD(name='b.sups')
GDS['backslash.tab'] = GD(name='backslash.tab', base='backslash')
GDS['bitcoin.lc'] = GD(name='bitcoin.lc')
GDS['bitcoin.sc'] = GD(name='bitcoin.sc')
GDS['braceleft.sc'] = GD(name='braceleft.sc')
GDS['braceleft.tab'] = GD(name='braceleft.tab', base='braceleft')
GDS['braceleft.uc'] = GD(name='braceleft.uc')
GDS['braceright.sc'] = GD(name='braceright.sc')
GDS['braceright.tab'] = GD(name='braceright.tab', base='braceright')
GDS['braceright.uc'] = GD(name='braceright.uc')
GDS['bracketleft.sc'] = GD(name='bracketleft.sc')
GDS['bracketleft.tab'] = GD(name='bracketleft.tab', base='bracketleft')
GDS['bracketleft.uc'] = GD(name='bracketleft.uc')
GDS['bracketright.sc'] = GD(name='bracketright.sc')
GDS['bracketright.tab'] = GD(name='bracketright.tab', base='bracketright')
GDS['bracketright.uc'] = GD(name='bracketright.uc')
GDS['c.sinf'] = GD(name='c.sinf', base='c.sups')
GDS['c.sups'] = GD(name='c.sups')
GDS['cent.alt'] = GD(name='cent.alt')
GDS['cent.lc'] = GD(name='cent.lc')
GDS['cent.lc.alt'] = GD(name='cent.lc.alt', base='cent.lc')
GDS['cent.sc'] = GD(name='cent.sc')
GDS['cent.sc.alt'] = GD(name='cent.sc.alt')
GDS['cent.tab.alt'] = GD(name='cent.tab.alt', base='cent.alt', accents=('cent.lc'))
GDS['cent'] = GD(name='cent')    
GDS['colon.tab'] = GD(name='colon.tab', base='colon')
GDS['commaaccent'] = GD(name='commaaccent', base='commaaccentcmb')
GDS['commaaccentabove'] = GD(name='commaaccentabove', base='commaaccentabovecmb')
GDS['commaaccentabovecmb'] = GD(name='commaaccentabovecmb')
GDS['commaaccentcmb'] = GD(name='commaaccentcmb')
GDS['d.sinf'] = GD(name='d.sinf', base='d.sups')
GDS['d.sups'] = GD(name='d.sups')
GDS['dagger.uc'] = GD(name='dagger.uc')
GDS['daggerdbl.uc'] = GD(name='daggerdbl.uc')
GDS['dcroat'] = GD(name='dcroat')
GDS['degree.lc'] = GD(name='degree.lc', base='degree')
GDS['degree.sc'] = GD(name='degree.sc', base='degree')
GDS['degree.tab'] = GD(name='degree.tab', base='degree')
GDS['divide.lc'] = GD(name='divide.lc', base='divide')
GDS['divide.tab'] = GD(name='divide.tab', base='divide')
GDS['dollar.alt'] = GD(name='dollar.alt')
GDS['dollar.lc'] = GD(name='dollar.lc')
GDS['dollar.lc.alt'] = GD(name='dollar.lc.alt', base='dollar.sc.alt')
GDS['dollar.sc'] = GD(name='dollar.sc')
GDS['dollar.sc.alt'] = GD(name='dollar.sc.alt')
GDS['dollar.tab.alt'] = GD(name='dollar.tab.alt', base='dollar.alt')
GDS['dollar'] = GD(name='dollar')
GDS['e.alt'] = GD(name='e.alt')
GDS['e.sinf'] = GD(name='e.sinf', base='e.sups')
GDS['e.sups'] = GD(name='e.sups')
GDS['eacute.alt'] = GD(name='eacute.alt', base='e.alt', accents=('acutecmb'))
GDS['ebreve.alt'] = GD(name='ebreve.alt', base='e.alt', accents=('brevecmb'))
GDS['ecaron.alt'] = GD(name='ecaron.alt', base='e.alt', accents=('caroncmb'))
GDS['ecircumflex.alt'] = GD(name='ecircumflex.alt', base='e.alt', accents=('circumflexcmb'))
GDS['edieresis.alt'] = GD(name='edieresis.alt', base='e.alt', accents=('dieresiscmb'))
GDS['edotaccent.alt'] = GD(name='edotaccent.alt', base='e.alt', accents=('dotaccentcmb'))
GDS['egrave.alt'] = GD(name='egrave.alt', base='e.alt', accents=('gravecmb'))
GDS['egrave.sinf'] = GD(name='egrave.sinf', base='egrave.sups')
GDS['egrave.sups'] = GD(name='egrave.sups', base='e.sups')
GDS['eight.lc'] = GD(name='eight.lc')
GDS['eight.tab_lc'] = GD(name='eight.tab_lc', base='eight.lc')
GDS['eight.tab_sc'] = GD(name='eight.tab_sc', base='eight.sc')
GDS['emacron.alt'] = GD(name='emacron.alt', base='e.alt', accents=('macroncmb'))
GDS['endash.tab'] = GD(name='endash.tab', base='endash')
GDS['Eng.sc'] = GD(name='Eng.sc', base='N.sc')
GDS['Eng'] = GD(name='Eng', base='N')
GDS['eogonek.alt'] = GD(name='eogonek.alt', base='e.alt', accents=('ogonekcmb'))
GDS['equal.lc'] = GD(name='equal.lc', base='equal')
GDS['equal.tab'] = GD(name='equal.tab', base='equal')
GDS['Eth.sc'] = GD(name='Eth.sc')
GDS['Eth'] = GD(name='Eth')
GDS['Euro'] = GD(name='Euro')
GDS['exclam.sc'] = GD(name='exclam.sc')
GDS['exclamdown.sc'] = GD(name='exclamdown.sc')
GDS['f.salt_noconnect'] = GD(name='f.salt_noconnect')
GDS['f.sinf'] = GD(name='f.sinf', base='f.sups')
GDS['f.sups'] = GD(name='f.sups')
GDS['fi'] = GD(name='fi', base='f', accents=('idotless',))
GDS['five.lc'] = GD(name='five.lc')
GDS['five.tab_lc'] = GD(name='five.tab_lc', base='five.lc')
GDS['five.tab_sc'] = GD(name='five.tab_sc', base='five.sc')
GDS['fl'] = GD(name='fl')
GDS['florin.lc'] = GD(name='florin.lc')
GDS['florin.sc'] = GD(name='florin.sc')
GDS['florin.tab'] = GD(name='florin.tab', base='florin')
GDS['four.lc'] = GD(name='four.lc')
GDS['four.tab_lc'] = GD(name='four.tab_lc', base='four.lc')
GDS['four.tab_sc'] = GD(name='four.tab_sc', base='four.sc')
GDS['g.salt'] = GD(name='g.salt')
GDS['g.sinf'] = GD(name='g.sinf', base='g.sups')
GDS['g.sups'] = GD(name='g.sups')
GDS['gbreve.salt'] = GD(name='gbreve.salt', base='g.salt', accents=('brevecmb',))
GDS['gcaron.salt'] = GD(name='gcaron.salt', base='g.salt', accents=('caroncmb',))
GDS['gcircumflex.salt'] = GD(name='gcircumflex.salt', base='g.salt', accents=('circumflexcmb'))
GDS['gcommaaccent.salt'] = GD(name='gcommaaccent.salt', base='g.salt', accents=('brevecmb'))
GDS['gdotaccent.salt'] = GD(name='gdotaccent.salt', base='g.salt', accents=('brevecmb'))
GDS['germandbls.sc'] = GD(name='germandbls.sc', base='S.sc', accents=('S.sc',))
GDS['greater.lc'] = GD(name='greater.lc', base='greater')
GDS['greater.tab'] = GD(name='greater.tab', base='greater')
GDS['greaterequal.lc'] = GD(name='greaterequal.lc', base='greaterequal')
GDS['greaterequal.tab'] = GD(name='greaterequal.tab', base='greaterequal')
GDS['h.sinf'] = GD(name='h.sinf', base='h.sups')
GDS['h.sups'] = GD(name='h.sups')
GDS['Hbar.sc'] = GD(name='Hbar.sc')
GDS['Hbar'] = GD(name='Hbar')
GDS['hbar'] = GD(name='hbar')
GDS['horizontalbar'] = GD(name='horizontalbar')
GDS['i.sinf'] = GD(name='i.sinf', base='i.sups')
GDS['i.sups'] = GD(name='i.sups')
GDS['idotaccent'] = GD(name='idotaccent', base='idotless', accents=('dotaccentcmb',))
GDS['j.sinf'] = GD(name='j.sinf', base='j.sups')
GDS['j.sups'] = GD(name='j.sups')
GDS['Jcircumflex.base'] = GD(name='Jcircumflex.base', base='J.base', accents=('circumflexcmb',))
GDS['Jcircumflex.base_sc'] = GD(name='Jcircumflex.base_sc', base='J.base_sc', accents=('circumflexcmb',))
GDS['k.sinf'] = GD(name='k.sinf', base='k.sups')
GDS['k.sups'] = GD(name='k.sups')
GDS['l.sinf'] = GD(name='l.sinf', base='l.sups')
GDS['l.sups'] = GD(name='l.sups')
GDS['less.lc'] = GD(name='less.lc', base='less')
GDS['less.tab'] = GD(name='less.tab', base='less')
GDS['lessequal.lc'] = GD(name='lessequal.lc', base='lessequal')
GDS['lessequal.tab'] = GD(name='lessequal.tab', base='lessequal')
GDS['logicalnot.lc'] = GD(name='logicalnot.lc', base='logicalnot')
GDS['Lslash.sc'] = GD(name='Lslash.sc')
GDS['Lslash'] = GD(name='Lslash')
GDS['lslash'] = GD(name='lslash')
GDS['m.sinf'] = GD(name='m.sinf', base='m.sups')
GDS['m.sups'] = GD(name='m.sups')
GDS['minus.lc'] = GD(name='minus.lc', base='minus')
GDS['minus.tab'] = GD(name='minus.tab', base='minus')
GDS['minute.lc'] = GD(name='minute.lc')
GDS['minute.tab'] = GD(name='minute.tab', base='minute')
GDS['multiply.lc'] = GD(name='multiply.lc', base='multiply')
GDS['multiply.tab'] = GD(name='multiply.tab', base='multiply')
GDS['n.sinf'] = GD(name='n.sinf', base='n.sups')
GDS['n.sups'] = GD(name='n.sups')
GDS['nbspace'] = GD(name='nbspace')
GDS['nine.lc'] = GD(name='nine.lc')
GDS['nine.salt'] = GD(name='nine.salt')
GDS['nine.tab_lc'] = GD(name='nine.tab_lc', base='nine.lc')
GDS['nine.tab_sc'] = GD(name='nine.tab_sc', base='nine.sc')
GDS['notequal.lc'] = GD(name='notequal.lc', base='notequal')
GDS['notequal.tab'] = GD(name='notequal.tab')
GDS['notequal'] = GD(name='notequal')
GDS['numbersign.lc'] = GD(name='numbersign.lc', base='numbersign')
GDS['numbersign.sc'] = GD(name='numbersign.sc')
GDS['numbersign.tab'] = GD(name='numbersign.tab', base='numbersign')
GDS['o.sinf'] = GD(name='o.sinf', base='o.sups')
GDS['o.sups'] = GD(name='o.sups')
GDS['oe.alt'] = GD(name='oe.alt')
GDS['oe'] = GD(name='oe')
GDS['one.lc'] = GD(name='one.lc')
GDS['one.tab_lc'] = GD(name='one.tab_lc', base='one.lc')
GDS['one.tab_sc'] = GD(name='one.tab_sc', base='one.sc')
GDS['ordfeminine.lc'] = GD(name='ordfeminine.lc', base='ordfeminine')
GDS['ordmasculine.lc'] = GD(name='ordmasculine.lc', base='ordmasculine')
GDS['p.sinf'] = GD(name='p.sinf', base='p.sups')
GDS['p.sups'] = GD(name='p.sups')
GDS['paragraph.lc'] = GD(name='paragraph.lc', base='paragraph')
GDS['parenleft.sc'] = GD(name='parenleft.sc')
GDS['parenleft.tab'] = GD(name='parenleft.tab', base='parenleft')
GDS['parenleft.uc'] = GD(name='parenleft.uc')
GDS['parenright.sc'] = GD(name='parenright.sc')
GDS['parenright.tab'] = GD(name='parenright.tab', base='parenright')
GDS['parenright.uc'] = GD(name='parenright.uc')
GDS['percent.lc'] = GD(name='percent.lc')
GDS['percent.tab'] = GD(name='percent.tab')
GDS['periodcmb'] = GD(name='periodcmb')
GDS['perthousand.lc'] = GD(name='perthousand.lc')
GDS['perthousand.tab'] = GD(name='perthousand.tab')
GDS['plus.lc'] = GD(name='plus.lc', base='plus')
GDS['plus.tab'] = GD(name='plus.tab', base='plus')
GDS['plusminus.lc'] = GD(name='plusminus.lc', base='plusminus')
GDS['plusminus.tab'] = GD(name='plusminus.tab', base='plusminus')
GDS['Q.sc'] = GD(name='Q.sc')
GDS['Q'] = GD(name='Q')
GDS['q.sinf'] = GD(name='q.sinf', base='q.sups')
GDS['q.sups'] = GD(name='q.sups')
GDS['question.sc'] = GD(name='question.sc')
GDS['questiondown.sc'] = GD(name='questiondown.sc')
GDS['quoteright'] = GD(name='quoteright')
GDS['r.sinf'] = GD(name='r.sinf', base='r.sups')
GDS['r.sups'] = GD(name='r.sups')
GDS['ringcmb_acutecmb'] = GD(name='ringcmb_acutecmb')
GDS['s.sinf'] = GD(name='s.sinf', base='s.sups')
GDS['s.sups'] = GD(name='s.sups')
GDS['schwa.alt'] = GD(name='schwa.alt')
GDS['second.lc'] = GD(name='second.lc')
GDS['second.tab'] = GD(name='second.tab', base='second')
GDS['second'] = GD(name='second', base='quotesingle', accents=('quotesingle',))
GDS['section.lc'] = GD(name='section.lc', base='section')
GDS['semicolon.tab'] = GD(name='semicolon.tab', base='semicolon')
GDS['seven.lc'] = GD(name='seven.lc')
GDS['seven.tab_lc'] = GD(name='seven.tab_lc', base='seven')
GDS['seven.tab_sc'] = GD(name='seven.tab_sc', base='seven.sc')
GDS['sfthyphen'] = GD(name='sfthyphen')
GDS['six.lc'] = GD(name='six.lc')
GDS['six.salt'] = GD(name='six.salt')
GDS['six.tab_lc'] = GD(name='six.tab_lc', base='six')
GDS['six.tab_sc'] = GD(name='six.tab_sc', base='six.sc')
GDS['slash.tab'] = GD(name='slash.tab', base='slash')
GDS['space.em'] = GD(name='space.em')
GDS['space.en'] = GD(name='space.en')
GDS['space.frac'] = GD(name='space.frac')
GDS['space.tab'] = GD(name='space.tab')
GDS['space.tab_em'] = GD(name='space.tab_em')
GDS['space.tab_en'] = GD(name='space.tab_en')
GDS['space.tab_thin'] = GD(name='space.tab_thin')
GDS['space.thin'] = GD(name='space.thin')
GDS['sterling.lc'] = GD(name='sterling.lc')
GDS['t.sinf'] = GD(name='t.sinf', base='t.sups')
GDS['t.sups'] = GD(name='t.sups')
GDS['Tbar.sc'] = GD(name='Tbar.sc')
GDS['Tbar'] = GD(name='Tbar')
GDS['three.lc'] = GD(name='three.lc')
GDS['three.tab_lc'] = GD(name='three.tab_lc', base='three.lc')
GDS['three.tab_sc'] = GD(name='three.tab_sc', base='three.sc')
GDS['two.lc'] = GD(name='two.lc')
GDS['two.tab_lc'] = GD(name='two.tab_lc', base='two.lc')
GDS['two.tab_sc'] = GD(name='two.tab_sc', base='two.sc')
GDS['u.sinf'] = GD(name='u.sinf', base='u.sups')
GDS['u.sups'] = GD(name='u.sups')
GDS['uni2117'] = GD(name='uni2117', base='copyrightsound')
GDS['v.sinf'] = GD(name='v.sinf', base='v.sups')
GDS['v.sups'] = GD(name='v.sups')
GDS['w.sinf'] = GD(name='w.sinf', base='w.sups')
GDS['w.sups'] = GD(name='w.sups')
GDS['x.sinf'] = GD(name='x.sinf', base='x.sups')
GDS['x.sups'] = GD(name='x.sups')
GDS['y.sinf'] = GD(name='y.sinf', base='y.sups')
GDS['y.sups'] = GD(name='y.sups')
GDS['yen.lc'] = GD(name='yen.lc')
GDS['yen'] = GD(name='yen')
GDS['z.sinf'] = GD(name='z.sinf', base='z.sups')
GDS['z.sups'] = GD(name='z.sups')
GDS['zero.lc'] = GD(name='zero.lc')
GDS['zero.lc_salt_slash'] = GD(name='zero.lc_salt_slash', base='zero.lc')
GDS['zero.salt_slash'] = GD(name='zero.salt_slash', base='zero')
GDS['zero.sc_salt_slash'] = GD(name='zero.sc_salt_slash')
GDS['zero.tab_lc'] = GD(name='zero.tab_lc', base='zero.lc')
GDS['zero.tab_lc_salt_slash'] = GD(name='zero.tab_lc_salt_slash', base='zero.sc')
GDS['zero.tab_salt_slash'] = GD(name='zero.tab_salt_slash')
GDS['zero.tab_sc'] = GD(name='zero.tab_sc', base='zero.sc')

class ConverNotesToXML:

  def __init__(self):
    pass
  
  def main(self, predicted_notes):
    print(predicted_notes)

    notes_to_print = ''
    tab_to_print = ''
    for note in predicted_notes:
      note_info = predicted_notes[note]
      print(note_info)
      if len(note_info[2]) == 3:
        print(note_info[2][0])
        print(note_info[2][2])
        notes_to_print += f'<note default-x="82">\
                <pitch>\
                    <step>{note_info[2][0]}</step>\
                    <alter>1</alter>\
                    <octave>{note_info[2][2]}</octave>\
                </pitch>\
                <duration>2</duration>\
                <voice>1</voice>\
                <type>quarter</type>\
                <accidental>sharp</accidental>\
                <stem default-y="-50.5">down</stem>\
                <notations>\
                    <slur number="1" placement="above" type="start"/>\
                </notations>\
            </note>'
        tab_to_print += f'<note default-x="82">\
                <pitch>\
                    <step>{note_info[2][0]}</step>\
                    <alter>1</alter>\
                    <octave>{note_info[2][2]}</octave>\
                </pitch>\
                <duration>2</duration>\
                <voice>1</voice>\
                <type>quarter</type>\
                <stem>none</stem>\
                <notations>\
                    <technical>\
                        <string>3</string>\
                        <fret>5</fret>\
                    </technical>\
                    <slur bezier-x="18" bezier-y="28" default-x="5" default-y="-21" number="1" placement="above" type="start"/>\
                </notations>\
            </note>'
      else:
        notes_to_print += f'<note default-x="82">\
                <pitch>\
                    <step>{note_info[2][0]}</step>\
                    <octave>{note_info[2][1]}</octave>\
                </pitch>\
                <duration>2</duration>\
                <voice>1</voice>\
                <type>quarter</type>\
                <stem default-y="-50.5">down</stem>\
                <notations>\
                    <slur number="1" placement="above" type="start"/>\
                </notations>\
            </note>'
        tab_to_print += f'<note default-x="82">\
                <pitch>\
                    <step>{note_info[2][0]}</step>\
                    <octave>{note_info[2][1]}</octave>\
                </pitch>\
                <duration>2</duration>\
                <voice>1</voice>\
                <type>quarter</type>\
                <stem>none</stem>\
                <notations>\
                    <technical>\
                        <string>3</string>\
                        <fret>5</fret>\
                    </technical>\
                    <slur bezier-x="18" bezier-y="28" default-x="5" default-y="-21" number="1" placement="above" type="start"/>\
                </notations>\
            </note>'

    base_xml = f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>\
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">\
<score-partwise version="3.1">\
    <identification>\
        <encoding>\
            <software>Finale v25 for Mac</software>\
            <encoding-date>2017-12-15</encoding-date>\
            <supports attribute="new-system" element="print" type="yes" value="yes"/>\
            <supports attribute="new-page" element="print" type="yes" value="yes"/>\
            <supports element="accidental" type="yes"/>\
            <supports element="beam" type="yes"/>\
            <supports element="stem" type="yes"/>\
        </encoding>\
    </identification>\
    <defaults>\
        <scaling>\
            <millimeters>6.35</millimeters>\
            <tenths>40</tenths>\
        </scaling>\
        <page-layout>\
            <page-height>1760</page-height>\
            <page-width>1360</page-width>\
            <page-margins type="both">\
                <left-margin>80</left-margin>\
                <right-margin>80</right-margin>\
                <top-margin>80</top-margin>\
                <bottom-margin>80</bottom-margin>\
            </page-margins>\
        </page-layout>\
        <system-layout>\
            <system-margins>\
                <left-margin>0</left-margin>\
                <right-margin>0</right-margin>\
            </system-margins>\
            <system-distance>173</system-distance>\
            <top-system-distance>68</top-system-distance>\
        </system-layout>\
        <staff-layout>\
            <staff-distance>67</staff-distance>\
        </staff-layout>\
        <appearance>\
            <line-width type="stem">0.8333</line-width>\
            <line-width type="beam">5</line-width>\
            <line-width type="staff">1.25</line-width>\
            <line-width type="light barline">1.4583</line-width>\
            <line-width type="heavy barline">5</line-width>\
            <line-width type="leger">1.875</line-width>\
            <line-width type="ending">1.4583</line-width>\
            <line-width type="wedge">0.9375</line-width>\
            <line-width type="enclosure">1.4583</line-width>\
            <line-width type="tuplet bracket">1.4583</line-width>\
            <note-size type="grace">50</note-size>\
            <note-size type="cue">50</note-size>\
            <distance type="hyphen">60</distance>\
            <distance type="beam">8</distance>\
        </appearance>\
        <music-font font-family="Maestro,engraved" font-size="18"/>\
        <word-font font-family="Times New Roman" font-size="9"/>\
    </defaults>\
    <part-list>\
        <score-part id="P1">\
            <part-name print-object="no">Guitar</part-name>\
            <part-abbreviation print-object="no">Gtr.</part-abbreviation>\
            <score-instrument id="P1-I1">\
                <instrument-name>Acoustic Guitar (steel)</instrument-name>\
                <instrument-sound>pluck.guitar</instrument-sound>\
            </score-instrument>\
            <midi-instrument id="P1-I1">\
                <midi-channel>1</midi-channel>\
                <midi-program>26</midi-program>\
                <volume>80</volume>\
                <pan>0</pan>\
            </midi-instrument>\
        </score-part>\
        <score-part id="P2">\
            <part-name print-object="no">Guitar [TAB]</part-name>\
            <part-abbreviation print-object="no">Gtr.</part-abbreviation>\
        </score-part>\
    </part-list>\
    <!--=========================================================-->\
    <part id="P1">\
        <measure number="1" width="485">\
            <print>\
                <page-layout>\
                    <page-height>1760</page-height>\
                    <page-width>1360</page-width>\
                    <page-margins>\
                        <left-margin>80</left-margin>\
                        <right-margin>727</right-margin>\
                        <top-margin>80</top-margin>\
                        <bottom-margin>80</bottom-margin>\
                    </page-margins>\
                </page-layout>\
                <system-layout>\
                    <system-margins>\
                        <left-margin>68</left-margin>\
                        <right-margin>0</right-margin>\
                    </system-margins>\
                    <top-system-distance>187</top-system-distance>\
                </system-layout>\
                <measure-numbering>system</measure-numbering>\
            </print>\
            <attributes>\
                <divisions>2</divisions>\
                <key>\
                    <fifths>0</fifths>\
                    <mode>major</mode>\
                </key>\
                <time>\
                    <beats>4</beats>\
                    <beat-type>4</beat-type>\
                </time>\
                <clef>\
                    <sign>G</sign>\
                    <line>2</line>\
                </clef>\
                <transpose>\
                    <diatonic>0</diatonic>\
                    <chromatic>0</chromatic>\
                    <octave-change>1</octave-change>\
                </transpose>\
            </attributes>\
            <sound tempo="120"/>\
            {notes_to_print}\
        </measure>\
    </part>\
    <!--=========================================================-->\
    <part id="P2">\
        <measure number="1" width="485">\
            <print>\
                <measure-numbering>none</measure-numbering>\
            </print>\
            <attributes>\
                <divisions>2</divisions>\
                <key print-object="no">\
                    <fifths>0</fifths>\
                    <mode>major</mode>\
                </key>\
                <clef>\
                    <sign>TAB</sign>\
                    <line>5</line>\
                </clef>\
                <staff-details>\
                    <staff-lines>6</staff-lines>\
                    <staff-tuning line="1">\
                        <tuning-step>E</tuning-step>\
                        <tuning-octave>2</tuning-octave>\
                    </staff-tuning>\
                    <staff-tuning line="2">\
                        <tuning-step>A</tuning-step>\
                        <tuning-octave>2</tuning-octave>\
                    </staff-tuning>\
                    <staff-tuning line="3">\
                        <tuning-step>D</tuning-step>\
                        <tuning-octave>3</tuning-octave>\
                    </staff-tuning>\
                    <staff-tuning line="4">\
                        <tuning-step>G</tuning-step>\
                        <tuning-octave>3</tuning-octave>\
                    </staff-tuning>\
                    <staff-tuning line="5">\
                        <tuning-step>B</tuning-step>\
                        <tuning-octave>3</tuning-octave>\
                    </staff-tuning>\
                    <staff-tuning line="6">\
                        <tuning-step>E</tuning-step>\
                        <tuning-octave>4</tuning-octave>\
                    </staff-tuning>\
                    <staff-size>167</staff-size>\
                </staff-details>\
            </attributes>\
            <sound tempo="120"/>\
            {tab_to_print}\
        </measure>\
    </part>\
    <!--=========================================================--> \
</score-partwise>'

    
    # Todo - dynamically return xml based on notes
    return base_xml

convert = ConverNotesToXML()
convert.main({0: [0.15083861909277893, 0.8122079489611174, 'Cs4'], 1: [0.9688480534036186, 1.003656965501952, 'Ds4'], 2: [1.978306504255293, 1.067473304348897, 'F4'], 3: [3.0515812939539124, 0.9456421120047295, 'Fs4'], 4: [4.049436774106142, 0.9514435973544517, 'Gs4'], 5: [5.006681856810316, 1.003656965501952, 'As5'], 6: [6.016140307661991, 1.003656965501952, 'C5'], 7: [7.025598758513665, 1.6302173832719569, 'Cs5']})
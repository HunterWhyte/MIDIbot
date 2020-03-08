# MIDIbot

The Piano Bot
KeysBot is a IRC bot for livestreaming that can turn messages in your twitch chat into MIDI notes that play on your computer


## How to use:

To use KeysBot type

!play (notes separated by commas) (bpm)

For example: !play C2,D3,C#4,Ab5 120

For each note include the octave at the end or leave blank to play all in the default position

To add rests in between your notes use more commas like this: !play C2,,,,,Bb1,,A

To hold notes over those rests use --- after a comma and the note like this: !play C3,-----,B

Each note at default is a quarter note using the defined BPM

Using this bot you can suggest things to add to the song I'm working on or just mess around

## Playing Chords With The Piano Bot
!chords
!chords (key) (scale) (chord,chord) (bpm)

## example
!chords C major I,I,IV,V 200

All the same formatting as the !play command.

To learn more about roman numeral notation for chords click [here](https://peterburk.github.io/chordProgressions/index.html#1e)

## Fun Examples for the Piano Bot
Fur Elise
!play E4,Eb4,E4,Eb4,E4,B3,D4,C4,A3,,C3,E3,A3,B3 200

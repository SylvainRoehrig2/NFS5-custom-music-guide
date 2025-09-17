# NFS5-custom-music-guide
A guide bundled with scripts allowing the use of custom music in NFS5 (Porsche Unleashed/2000)

# Requirements
- A copy of the game
- [NHL 2002 Ditty Importer](https://ditty-importer.softag.com/)
- [VIV file encoder/decoder](https://www.nfsaddons.com/downloads/nfshp/tools/7236/viv-file-decoderencoder.html)
- (Optional) The scripts available on this repository
- (Optional) Ffmpeg, if your audio files are not in WAV format

# 1st part : Decoding music
* Go to `<game_folder>/GameData/Music`. There should be a file named `zzzmus.viv`.
* Create a folder for backup, and copy/paste your original `zzzmus.viv` file in it.
* Create a folder (I will now refer to it as `music_mod`) where you will put your `zzzmus.viv` file
* Put the two executables `vivdec.exe` and `vivenc.exe` from the VIV file encoder/decoder addon in the `music_mod` folder.
* Open a terminal (cmd or PowerShell) in the `music_mod` folder and type this :

  `vivdec.exe zzzmus.viv`

  A list of files should appear like this

  <img width="372" height="121" alt="image" src="https://github.com/user-attachments/assets/87b60f38-082d-4370-a9ce-14715b31cbb3" />

# 2nd part : Adding music
NFS5 only allow music with a special proprietary encoding that EA uses. 

Thankfully, the Ditty Importer allow us to encode any music we want in this special encoding.

But before we do that we need to do a few things.

* Rename the audio file you want to put in the game so that it matches the format of already existing music.

  If the file starts with :

  * "gameXX" -> Played during races, can be selected in the jukebox
  * "loseXX" -> Played when you don't get first place
  * "menuXX" -> PLayed in the menus
  * "vicXX" -> Played when you win all the trophies of an era and change era
  * "winXX" -> Played when you get 1st place in a race

  I have not tested if the number ("XX" in "gameXX" for example) has any impact, I merely added songs while increasing the number. Needs testing.

  Include the name of the artist and song in the file's name, following the same structure, as the game seems to use the file's name for the jukebox.

  So for example if you want to put "Dirty Great Monster" by "Duran Duran" as a menu's music, name it `menu06-Dirty Great Monster-Duran Duran`.

  Ideally, you want the audio file to be added to have a .wav extension.

* Your audio file must have a .wav extension. The `wav_convert.py` available in this repository allows easy conversion in the right encoding.

  To use it, create two folders named "to_be_converted" and "converted", put the audio files in the "to_be_converted" folder.

  Then launch the python script (the folder containing the script must also contain the two folders).

  The converted files that you should use for the next step are found in the "converted" folder.

* Open the ditty importer (wimpditt.exe)
* For each song you want to add:
  * "Convert File" is the file you want to add
  * "Output folder" is the ouput folder for the conversion (duh)
  * Press "Import"
  * When it's done, an ASF file should have been created in the designated output folder

Sadly this part with the ditty importer is not automated (yet ?). You must import files one by one.

# 3rd part : Encoding music

* Create a folder in `music_mod` named `input`. The full path should be `music_mod/input`.
* Put the original music files that were decoded (the ones without an extension) and your newly created files (with and .asf extension)

  It may be possible to actually not put the original files at all if you don't want them anymore. Needs testing.

  The files can have an .asf extension or no extension without issue.

* Place the `vivencoding.py` script in the `music_mod` folder and launch it.

  If you don't want to use the script, you will have to use the vivenc.exe in a terminal.

  But you will have to list ALL the files you want to encode together (which is long and tedious).

  So it'll be : `vivenc.exe <name_of_viv> <file1> <file2> .... <last_file>`

* Place the newly created/modified `zzzmus.viv` file in `<game_folder>/GameData/Music`.

You can now launch the game, and everything should work now !

* Make sure that you select the songs you want in the jukebox if you intend on actually hearing them during races.

Have fun !


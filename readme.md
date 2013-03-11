Movie Renamer
=============
The application is currently incomplete:
 - There's no nice gui, only very basic console ui.
 
 - There's no way to install the app (besides cloning the repository).

 - The renamer doesn't work on a significant portion of possible movie file names.
 
Examples
--------
Using ui
```bash
[phasip@MobileP ~]$ cd /tmp/movies
[phasip@MobileP movies]$ touch "Back.To.The.Future.Part.II.1989.1080p.BluRay.X264-LCHD.mkv"
[phasip@MobileP movies]$ touch "Inception.DVDRiP.XviD-ARROW.avi"
[phasip@MobileP movies]$ touch "Back.To.The.Future.Part.II.1989.DVDRip.DivX.AC3.iNTERNAL-FFM.avi"
[phasip@MobileP movies]$ touch "Kill Bill.2003.DVDRip.XviD-DiCE.avi"
[phasip@MobileP movies]$ touch "Gladiator[Extended.Edition]DvDrip.AC3[Eng]-aXXo.avi"
[phasip@MobileP movies]$ touch "Pirates_of_the_Caribbean_The_Curse_of_the_Black_Pearl.720p.ESiR.mkv"
[phasip@MobileP movies]$ touch "Shutter.Island.2010.480p.BRRip.x264.DXVA.AC3-FLAWL3SS.mkv"
[phasip@MobileP movies]$ touch "Monty.Python.and.the.Holy.Grail.DVDivX-SCHIZO.avi"
[phasip@MobileP movies]$ touch "King.Kong.2005.DVDRip.DivX5.AC3.2CH-aXXo.avi"
[phasip@MobileP movies]$ touch "The.Avengers.2012.DVDRip.XviD-NYDIC.avi"
[phasip@MobileP movies]$ touch "Pulp.Fiction.1994.720p.BluRay.x264-SiNNERS.mkv"
[phasip@MobileP movies]$ touch "no.country.for.old.man.mp4"
[phasip@MobileP movies]$ touch "The Big Lebowski [Eng][XviD][1998].avi"
[phasip@MobileP movies]$ /home/phasip/Projects/Python/Movie-Renamer/src/interface.py
Rename	The Big Lebowski [Eng][XviD][1998]
to	The Big Lebowski (1998) [Y/n] 
Rename	Pulp.Fiction.1994.720p.BluRay.x264-SiNNERS
to	Pulp Fiction (1994) [Y/n] 
Rename	The.Avengers.2012.DVDRip.XviD-NYDIC
to	The Avengers (2012) [Y/n] 
Rename	King.Kong.2005.DVDRip.DivX5.AC3.2CH-aXXo
to	King Kong (2005) [Y/n] 
Fail to rename Monty.Python.and.the.Holy.Grail.DVDivX-SCHIZO
Rename	Shutter.Island.2010.480p.BRRip.x264.DXVA.AC3-FLAWL3SS
to	Shutter Island (2010) [Y/n] 
Rename	Pirates_of_the_Caribbean_The_Curse_of_the_Black_Pearl.720p.ESiR
to	Pirates of the Caribbean: The Curse of the Black Pearl (2003) [Y/n] 
Rename	Gladiator[Extended.Edition]DvDrip.AC3[Eng]-aXXo
to	Gladiator (2000) [Y/n] 
Rename	Kill Bill.2003.DVDRip.XviD-DiCE
to	Kill Bill: Vol. 1 (2003) [Y/n] 
Rename	Back.To.The.Future.Part.II.1989.DVDRip.DivX.AC3.iNTERNAL-FFM
to	Back to the Future Part II (1989) [Y/n] 
Rename	Inception.DVDRiP.XviD-ARROW
to	Inception (2010) [Y/n] 
Rename	Back.To.The.Future.Part.II.1989.1080p.BluRay.X264-LCHD
to	Back to the Future Part II (1989) [Y/n] 
Fail to rename Back.To.The.Future.Part.II.1989.1080p.BluRay.X264-LCHD to Back to the Future Part II (1989)
[phasip@MobileP movies]$ ls -la
total 0
-rw-r--r--  1 phasip users   0 Mar 11 21:56 no.country.for.old.man.mp4
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 The Big Lebowski (1998)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 The Avengers (2012)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Shutter Island (2010)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Pulp Fiction (1994)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Pirates of the Caribbean: The Curse of the Black Pearl (2003)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Monty.Python.and.the.Holy.Grail.DVDivX-SCHIZO
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 King Kong (2005)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Kill Bill: Vol. 1 (2003)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Inception (2010)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Gladiator (2000)
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Back.To.The.Future.Part.II.1989.1080p.BluRay.X264-LCHD
drwxr-xr-x  2 phasip users  60 Mar 11 21:56 Back to the Future Part II (1989)
drwxrwxrwt 26 root   root  760 Mar 11 21:49 ..
drwxr-xr-x 14 phasip users 300 Mar 11 21:56 .
```
Or using library
```python
>>> from movie_renamer import rename
>>> rename('Back.To.The.Future.Part.II.1989.1080p.BluRay.X264-LCHD.mkv')
0: 'Back to the Future Part II (1989).mkv'
>>> rename('Inception.DVDRiP.XviD-ARROW.avi')
1: 'Inception (2010).avi'
>>> rename('Back.To.The.Future.Part.II.1989.DVDRip.DivX.AC3.iNTERNAL-FFM.avi')
2: 'Back to the Future Part II (1989).avi'
>>> rename('Kill Bill.2003.DVDRip.XviD-DiCE.avi')
3: 'Kill Bill: Vol. 1 (2003).avi'
>>> rename('Gladiator[Extended.Edition]DvDrip.AC3[Eng]-aXXo.avi')
4: 'Gladiator (2000).avi'
>>> rename('Pirates_of_the_Caribbean_The_Curse_of_the_Black_Pearl.720p.ESiR.mkv')
5: 'Pirates of the Caribbean: The Curse of the Black Pearl (2003).mkv'
>>> rename('Shutter.Island.2010.480p.BRRip.x264.DXVA.AC3-FLAWL3SS.mkv')
6: 'Shutter Island (2010).mkv'
>>> rename('Monty.Python.and.the.Holy.Grail.DVDivX-SCHIZO.avi')
7: 'Monty Python and the Holy Grail (1975).avi'
>>> rename('King.Kong.2005.DVDRip.DivX5.AC3.2CH-aXXo.avi')
8: 'King Kong (2005).avi'
>>> rename('The.Avengers.2012.DVDRip.XviD-NYDIC.avi')
9: 'The Avengers (2012).avi'
>>> rename('Pulp.Fiction.1994.720p.BluRay.x264-SiNNERS.mkv')
10: 'Pulp Fiction (1994).mkv'
>>> rename('aladdin disney')
11: 'Aladdin (1994)'
>>> rename('green mile')
12: 'The Green Mile (1999)'
>>> rename('theDarkKnightRises')
13: 'The Dark Knight Rises (2012)'
>>> rename('matrix 2')
14: 'The Matrix Reloaded (2003)'
>>> rename('no.country.for.old.man.mp4')
15: 'No Country for Old Men (2007).mp4'
>>> rename('The Big Lebowski [Eng][XviD][1998].avi')
16: 'The Big Lebowski (1998).avi'
```

More examples can be found in the tests.

Requirements
------------
 - Python 2.7
 - IMDbPY

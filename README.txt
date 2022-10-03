Za koriscenje je potrebno imati python 3.10.x

Kada instalirate najbolje je da napravite i virtuelno okruzenje. To mozete uraditi sledecim komandama
	pip install virtualenv
	cd {u musix folder}
	virtualenv venv

Nakon toga aktivirajte orkuzenje komandom
	ako koristite powershell: ./venv/Source/activate
	ako koristite git bash: source venv/Source/activate

Instalirajte neophodnu biblioteku koja je u folderu komandom (kada je aktivirano okruzenje)
	pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl
	
Za hostovanje:
	Bilo dobro da pronadjete svoj IP
		To mozete uraditi preko komande ipconfig i pod sekcijom Ethernet adapter Ethernet ipv4 ce vam biti potreban
	
	Treba aktivirati Stereo Mix na Windowsu
		https://thegeekpage.com/stereo-mix/
	
	Ukoliko imate usb/wireless slusalice, verovatno nece raditi. Treba ubaciti bilo koje 3.5mm slusalice ili aux kabl i izabrati da je to default device za output.
	Da bi se zvuk cuo i na vasim slusalicama mozete u podesavanjima stereo mix-a pod sekcijom Listen izabrati listen to this device i u padajucem meniju izabrati vase usb slusalice.
	
	Sada mozete pokrenuti server komandom (iz aktiviranog okruzenja)
		python server.py
		
	Prvo ispisite sve uredjaje, trebace vam index uredjaja
	Zapamtite index -> ime: Stereo Mix i hostApi: 0
	Taj indeks ce biti neophodan pri strimovanju
	
	Nakon toga samo pokrenite stream i unesite potrebne podatke.
	
Za slusanje:
	Kada neko pokrene server treba da vam posalje svoj ip
	
	Kada aktivirate okruzenje pokrenite client komandom
		python client.py
		
	Unesite ip host-a i trebalo bi da radi sve :D
	
	
Potencijalni problemi:
	Mozda ce biti problema sa gasenjem ali mislim da sam popravio to.
	Svasta jos...
	
	
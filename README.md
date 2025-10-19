# Oheislaitteiden arvostelut
-Sovelluksessa käyttäjät voivat jättää arvosteluja oheislaitteista (näppäimistöt, hiiret, yms). Arvostelussa näkyy arvosana, hinta ja arvostelu.  
-Käyttäjä voi luoda tunnukset ja kirjautumaan sisään sovellukseen.  
-Käyttäjä pystyy lisäämään arvosteluja ja muokkaamaan tai poistamaan itse lisäämiään arvostelujaan.  
-Käyttäjä pystyy valitsemaan arvostelulla yhden tai useamman luokittelun (Arvosana, hintaluokka).  
-Käyttäjä näkee kaikkien lisäämät arvostelut.  
-Käyttäjäsivu näyttää lisättyjen arvostelujen määrän, listan arvosteluista, sekä arvostelujen keskiarvon.  
-Käyttäjäsivu näyttää käyttäjän kommentit ja listan niistä.  
-Käyttäjä pystyy hakemaan arvosteluja nimellä tai luokittelulla.  
-Käyttäjä pystyy antamaan arvostelulle kommentin ja arosanan.  

Välipalautus 2:  
-Käyttäjä voi luoda tunnuksen ja kirjautumaan sisään tai pois sovelluksessa.  
-Käyttäjä voi lisätä uusia tietokohteita ja muokata tai poistaa niitä.  
-Käyttäjä pystyy lisäämään tietokohteisiin kommentteja.  
-Käyttäjä pystyy etsimään tietokohteita niiden otsikkojen mukaan.  

Välipalautus 3:  
-CSRF-aukko korjattu.  
-Käyttäjä voi nyt poistaa tietokohteen.  
-Käyttäjillä käyttäjäsivut, jossa näkyy kaikki käyttäjän viestit.  
-Käyttäjä voi lisätä profiilikuvan.  

Ohjeet sovelluksen käyttöön (windows 11 ja git cmd):  
git clone https://github.com/MMorko/tikawe-oheislaitesovellus  
cd tikawe-oheislaitesovellus  
python -m venv venv  
venv\Scripts\activate  
python -m pip install --upgrade pip  
pip install flask  
pip install werkzeug  
sqlite3 database.db < schema.sql  
python -m flask run  

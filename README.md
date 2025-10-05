# Oheislaitteiden arvostelut
-Sovelluksessa käyttäjät voivat jättää arvosteluja oheislaitteista (näppäimistöt, hiiret, yms). Arvostelussa näkyy arvosana, hinta ja arvostelu.  
-Käyttäjä voi luoda tunnukset ja kirjautumaan sisään sovellukseen.  
-Käyttäjä pystyy lisäämään arvosteluja ja muokkaamaan tai poistamaan itse lisäämiään arvostelujaan.  
-Käyttäjä pystyy valitsemaan arvostelulla yhden tai useamman luokittelun (Mikä oheislaite, hintaluokka).  
-Käyttäjä näkee kaikkien lisäämät arvostelut.  
-Käyttäjäsivu näyttää lisättyjen arvostelujen määrän, listan arvosteluista, sekä arvostelujen keskiarvon.  
-Käyttäjä pystyy hakemaan arvosteluja nimellä tai luokittelulla.  
-Käyttäjä pystyy antamaan arvostelulle kommentin ja arosanan.  

##Välipalautus 2:  
-Käyttäjä voi luoda tunnuksen ja kirjautumaan sisään tai pois sovelluksessa.  
-Käyttäjä voi lisätä uusia tietokohteita ja muokata tai poistaa niitä.  
-Käyttäjä pystyy lisäämään tietokohteisiin kommentteja.  
-Käyttäjä pystyy etsimään tietokohteita niiden otsikkojen mukaan.  

##Välipalautus 3:  
-CSRF-aukko korjattu.  
-Käyttäjä voi nyt poistaa tietokohteen.  
-Käyttäjillä käyttäjäsivut, jossa näkyy kaikki käyttäjän viestit.  
-Käyttäjä voi lisätä profiilikuvan.  

Sovelluksen saa toimimaan lisäämällä kaikki tiedostot samaan kansioon ja luomalla schema.sql tiedoston avulla tietokannan database.db  
Toiminta olettaa venv, sqlite, werkzeug.security, Flask lataamista samaan osoitteeseen missä sovellus.  

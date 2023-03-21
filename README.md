# Ravintola-arvostelusovellus

Tässä sovelluksessa voi arvostella ravintoloita.
Ajankohtainen versio [sovelluksesta](https://ravintola-arvostelu.fly.dev/). 

## Toiminnallisuus

- Käyttäjätilin luonti
- Kirjautuminen
- Arvosteluiden selaaminen
- Arvostelun lisääminen
- Arvostelun poistaminen
- Moderaattori voi poistaa muiden arvosteluita

## Käyttäjät 

On kaksi erilaista käyttäjtyyppiä. 

- Peruskäyttäjä
- Ylläpitäjä

Peruskäyttäjä voi tarkastella kaikkien arvosteluja. Lisätä ja poistaa omia arvosteluita.
Ylläpitäjä(moderaattori) peruskäyttäjätoiminnalisuuden lisäksi voi poistaa muiden arvosteluita, jos ovat epäasiallisia.

## Tietokanta

Sovelluksessa käytetään PostgreSQl-tietokantaa. Alustavasti viisi(5) tietokantataulua. Määrän kasvattaminen mahdollinen.


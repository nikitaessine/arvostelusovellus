# Ravintola-arvostelusovellus

Tässä sovelluksessa voi arvostella ravintoloita.

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

##Käynnistysohjeet

Tästä pääsee kokeilemaan [sovellusta](https://ravintola-arvostelu.fly.dev/). (ei ajantasalla). 

Paikallisesti sovelluksen saa toimimaan seuraavasti:

1. Kloonaa repositorio koneellesi ja siirry sen juurihakemistoon
2. Luo .env tiedosto ja määritä sen sisältö seuraavanlaisesksi:

```bash
DATABASE_URL=postgresql:///<tietokannan-nimi>
SECRET_KEY=<salainen-avain>
```
- missä tietokannan nimi on käyttäjän tunnus
- salaisen avaimen voi luoda seuraavilla komennoilla

```bash
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```

3. Käynnistä virtuaaliympäristö

```bash
python3 -m venv venv
source venv/bin/activate
```
4. Asenna riippuvuudet

```bash
pip install -r requirements.txt
```
5. Määritä tietokannan skeema

```bash
psql < schema.sql
```
6. Käynnistä sovellus

```bash
flask run
```


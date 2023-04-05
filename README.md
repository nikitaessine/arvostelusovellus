# Ravintola-arvostelusovellus

Tässä sovelluksessa voi lisätä ja arvostella ravintoloita.

## Toiminnallisuus

- Käyttäjätilin luonti(toimii)
- Kirjautuminen(toimii)
- Ravintolan lisääminen(toimii)
- Arvosteluiden selaaminen(toimii)
- Arvostelun lisääminen(toimii)
- Arvostelun poistaminen
- Moderaattori voi poistaa muiden arvosteluita
- Moderaattoi voi poistaa ravintolan(toimii)

## Käyttäjät 

On kaksi erilaista käyttäjtyyppiä. 

- Peruskäyttäjä
- Ylläpitäjä

Peruskäyttäjä voi tarkastella kaikkien arvosteluja. Lisätä arvosteluita.
Ylläpitäjä(moderaattori) peruskäyttäjätoiminnalisuuden lisäksi voi poistaa muiden arvosteluita tai ravintolalisäyksiä, jos ovat epäasiallisia.

## Tietokanta

Sovelluksessa käytetään PostgreSQl-tietokantaa. Alustavasti viisi(5) tietokantataulua. Määrän kasvattaminen mahdollinen.

## Käynnistysohjeet

Tästä pääsee kokeilemaan [sovellusta](https://ravintola-arvostelu.fly.dev/). (ei toimi). 

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
5. Käynnistä tietokanta toisessa terminaaliikkunassa

```bash
start-pg.sh
```
6. Alkuperäisessä terminaalikkunassa aja seuraava

```bash
$ psql
user=# CREATE DATABASE <tietokannan-nimi>;
```
- tietokannan nimi on sama jonka määritit 2.kohdassa

7. Määritä tietokannan skeema

```bash
 psql -d <tietokannan-nimi> < schema.sql
```
- tietokannan nimi on sama jonka määritit 2.kohdassa

6. Käynnistä sovellus

```bash
flask run
```


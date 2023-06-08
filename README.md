# SecureLock
Ein Hochsicherheitssystem zur Überprüfung und Validierung an elektronischen Türschlössern

Bauteile, welche hierfür verwendet werden:
  1. ein RFID-Modul (MFRC522
  2. ein 16x2 LCD Display
  3. ein Servomotor mit "Schranke"

Hierfür verwendete Bibliotheken:
  1. RPi.GPIO
  2. mfrc522
  3. time
  4. lcddriver

Ausgangsszenario des Projekts ist eine elektronisch verschlossene Tür, welche geöffnet werden soll. Hierzu soll eine Karte genutzt werden
Ziel des Projekts ist, dass die Authentifizierung an einer Tür zu simulieren

Beispielhaft soll so ein LCD-Display als eine kleine Klartextausgabe fungieren und Anweisungen sowie Infos ausgeben.
Das RFID-Modul soll mittels Karten, welche verschiedenen Personen gehören, eine haptische Authentifizierung ermöglichen.
Der Servomotor soll mittels Pulsweitenmodulation eine Tür simulieren, welche bei Authentifizierung eine sich öffnende und wieder schließende Tür simulieren.

Im Hintergrund geschriebene Logs sollen dazu dienen, dass nachvollziehbar ist, wann und wo eine Tür geöffnet wurde oder zumindest wann und wo versucht wurde sich (unberechigten) Zutritt zu verschaffen. 

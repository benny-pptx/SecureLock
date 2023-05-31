# SecureLock
Ein Hochsicherheitssystem zur Überprüfung und Validierung an elektronischen Türschlössern

Bauteile, welche hierfür verwendet werden:
  1. ein RFID-Modul (MFRC522)
  2. eine RasPi Kamera (nativer RPi Kamera Anschluss)
  3. ein 16x2 LCD Display
  4. ein Fingerabdrucksensor
  5. ein Servomotor mit "Schranke"

Hierfür verwendete Bibliotheken:
  1. cv2
  2. RPi.GPIO
  3. mfrc522
  4. time
  5. lcddriver

Ausgangsszenario des Projekts ist eine elektronisch verschlossene Tür, welche geöffnet werden soll. Verschiedene Möglichkeiten zur Authentifizierung sollen möglich sein. Ein Alles-in-Allem-Paket mit allen möglichen Authentifizierungen oder aber weniger umfangreiche Versionen mit weniger Authentifizierungsmethoden. Beispielhaft wäre, dass der Ausweis, die Kamera und der Fingerabdrucksensor gleichzeitig zur Authentifizierung genutzt werden. Es wäre ebenfalls denkbar, dass eine Kamera Authentifizierung nicht gewünscht ist (aufgrund von Datenschutzbedenken oder ähnlichem) und lediglich Fingerabdruck und Karte verwendet werden. 
Ziel des Projekts ist, dass mehrere Authentifizierungsmethoden, mehrere Fallbeispiele abdecken.

Beispielhaft soll so ein LCD-Display als eine kleine Klartextausgabe fungieren und Anweisungen sowie Infos ausgeben.
Das RFID-Modul soll mittels Karten, welche verschiedenen Personen gehören, eine haptische Authentifizierung ermöglichen.
Die RasPi Kamera soll einer Gesichtserkennung dienen.
Der Fingerabdrucksensor soll eine biometrische Authentifizierung ermöglichen.
Der Servomotor soll mittels Pulsweitenmodulation eine Tür simulieren, welche bei Authentifizierung eine sich öffnende und wieder schließende Tür simulieren.

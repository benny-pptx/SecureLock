# SecureLock
Ein Hochsicherheitssystem zur Überprüfung und Validierung an elektronischen Türschlössern

Bauteile, welche hierfür verwendet werden:
  1. ein RFID-Modul (MFRC522)
  2. eine RasPi Kamera
  3. ein 16x2 LCD Display
  4. ein Fingerabdrucksensor
  5. ein Servomotor mit "Schranke"

Hierfür verwendete Bibliotheken:
  1. cv2
  2. RPi.GPIO
  3. mfrc522
  4. time
  5. lcddriver

Ziel des Ganzen ist es, dass mehrere Profile mit mehreren Authentifizierungsmethoden möglich sein sollen und somit mehrere Fallbeispiele abgedeckt werden!
Beispielhaft soll so ein LCD-Display als eine kleine Klartextausgabe fungieren und Anweisungen sowie Infos ausgeben.
Das RFID-Modul soll mittels Karten, welche verschiedenen Personen gehören, eine haptische Authentifizierung ermöglichen.
Die RasPi Kamera soll einer Gesichtserkennung dienen.
Der Fingerabdrucksensor soll eine biometrische Authentifizierung ermöglichen.
Der Servomotor soll mittels Pulsweitenmodulation eine Tür simulieren, welche bei Authentifizierung eine sich öffnende und wieder schließende Tür simulieren.

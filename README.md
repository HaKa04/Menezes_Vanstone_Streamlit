# Menezes-Vanstone Verschlüsselung im Körper $F_{q}$

Dies ist eine Implementierung des Menezes-Vanstone-Kryptosystems in Python. Das System erlaubt die Ver- und Entschlüsselung von Nachrichten mit Hilfe von elliptischen Kurven im Körper $F_{131^8}$. Die Anwendung verwendet meine eigene Python-Bibliothek, die für Berechnungen mit elliptischen Kurven und dem Körper $F_{131^8}$ entwickelt wurde.

## Anweisungen für die Verwendung des Programms

Eine Webseite zur Veranschaulichung wird von Streamlit selbst gehostet [hier](https://menezes-vanstone.streamlit.app/).
### Lokal
Wenn Sie es lokal benutzen wollen, hier ist die Anleitung:
### Abhängigkeiten

Stellen Sie sicher, dass die folgenden Python-Bibliotheken installiert sind:

- Streamlit
- Numpy
- elliptic-curves-fq

Dies wird unten beschrieben.

### Installation

```sh
   pip install requirements.txt
   ```


### Anwendung ausführen

Um die Anwendung auszuführen, verwenden Sie den folgenden Befehl:

```sh
streamlit run Streamlit.py
```
## Anmerkungen

Die Anwendung dient nur zur Veranschaulichung dieses Verschlüsselungsverfahrens und stellt keine praktische Anwendung dar.

## Autor

Kaspar Hui

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](https://opensource.org/licenses/MIT).
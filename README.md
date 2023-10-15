# Menezes-Vanstone Verschlüsselung in endlichen Körpern

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
Linux:
```sh
pip install -r src/requirements.txt
```
Windows:
```sh
pip install -r .src\requirements.txt
```


### Anwendung ausführen

Um die Anwendung auszuführen, verwenden Sie den folgenden Befehl:

Linux:
```shell
streamlit run src/Streamlit.py
```
Windows:
```shell
streamlit run .src\Streamlit.py
```
## Anmerkungen

Die Anwendung dient nur zur Veranschaulichung dieses Verschlüsselungsverfahrens und stellt keine praktische Anwendung dar.

## Autor

Kaspar Hui

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](https://opensource.org/licenses/MIT).
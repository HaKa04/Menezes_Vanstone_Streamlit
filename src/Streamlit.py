import streamlit as st
import math
import random
import streamlit.components.v1 as components
from elliptic_curves_fq import text_to_ascii, Menezes_Vanstone_decrybtion, Menezes_Vanstone_encrybtion, ascii_to_text, Ascii
import numpy as np

def main():

    # Titel
    st.set_page_config(page_title="Menezes Vanstone Kryptosystem im Körper F(p^n)", layout="wide")
    
    # Seitentitel im Hauptfeld
    st.title('Beispiel zur Überprüfung des Menezes Vanstone Verschlüsselungssystem')
    Elliptische_Kurve  = st.sidebar.container()
    Kurve = Ascii()
    startpunkt = Kurve.startpoint
    with Elliptische_Kurve:
        st.title("Elliptische Kurve mit folgenden Parametern")
        st.latex('y^2 = x^3 + ax + b', help=None)
        st.write(f'''a = {Kurve.a.value}, b = {Kurve.b.value}''')
        st.write("Punkt P = ", str(startpunkt))
        st.write(f'''Primzahl = 131, irreduzibles Polynom = {Kurve.a.ir_poly}''')
    
    text = st.text_input("Zu verschlüsselnder Text: ")
    packets = 1 + math.ceil(len(text)/16)
    if st.button('Berechnungen starten'):
    # Erstelle ein Layout mit drei Spalten
    
        privater_schluessel_a = random.randrange(int(Kurve.bound()[0]))
        öffentlicher_schluessel_Qa = startpunkt * privater_schluessel_a

        # Erstelle Boxen für öffentliche und private Schlüssel in der Seitenleiste
        private_key_box = st.sidebar.container()
        public_key_box = st.sidebar.container()
        
        with private_key_box:
            st.title("Privater Schlüssel Empfänger: ")
            st.latex(r" \text{Privatschlüssel } k_A: " )
            st.latex(str(privater_schluessel_a))

        with public_key_box:
            st.title("Öffentlicher Schlüssel Empfänger: ")
            st.latex(r" \text{Öffentlicher Schlüssel }  Q_A = P \cdot k_A:"  )
            st.write(f" {str(öffentlicher_schluessel_Qa)} ")

        List_of_tabs= ["Schema der Verschlüsselung/Entschlüsselung", "Gesamtanzahl von Blöcken", "Block 0 mit Länge der Nachricht"]
        for j in range(1,packets):
            List_of_tabs.append(f"Block {j}")
        tabs = st.tabs(List_of_tabs)

        with tabs[0]:
            first_layer = st.container()
            with first_layer:
                st.subheader("Setup ")
                st.write("""Elliptische Kurve mit Gleichung und Parametern wie in der linken Seitenleiste. Punkt G auf dieser Kurve ist ebenfalls gegeben. 
                         Wir konstruieren der endliche Körper F(131^8). Das irreduzible Polynom wird für die Berechnung verwendet.  """)
                st.write("-----")
                st.latex(r'''\text{Empfänger generiert privaten Schlüssel } k_A \text{ mit einer ganzen Zahl zwischen 0 und } q = 131^8 = 86’730’203’469’006’241''')
                st.latex(r'''\text{Empfänger berechnet öffentlichen Schlüssel Punkt } Q_A = P \cdot k_A \text{ |(Punktaddition)}''')
                st.write("-----")
                st.write("Nun gilt für jeden Block von 2 mal 8 Zeichen in ASCII dasselbe Schema.")
                st.write("-----")
            transform_message = st.container()
            with transform_message:
                st.subheader("Transformiere Nachricht in passende Form")
                st.latex(r'''\text{Der Sender teilt die Nachricht in Blöcke von jeweils 2 mal 8 Zeichen auf. Der erste Block ist die Länge der Nachricht in Dezimalziffern. Die nächsten Blöcke sind die Nachricht.}  ''')
                st.latex(r''' \text{Wenn im letzten Block nicht 16 Zeichen vorhanden sind, wird dieser mit "-" aufgefüllt. Der Sender transformiert diese 2 mal 8 Blöcke in Elemente von } F(131^8) ''')
                st.latex(r'''\text{Jedes Zeichen wird in seinen ASCII-Code umgewandelt und 8 davon bilden ein Element. Zwei Elemente bilden ein Paar} (m_{i1},m_{i2}) \text{, hier als Blöcke bezeichnet.}''')
                st.write("-----")
            encryption = st.container()
            with encryption:
                st.subheader("Verschlüsselung")
                st.latex(r'''\text{Sender generiert für jeden Block privaten Schlüssel } z_i \text{ mit einer ganzen Zahl zwischen 0 und } q = 131^8 = 86’730’203’469’006’241''')
                st.latex(r'''\text{Sender berechnet Punkt } R_i = P \cdot z_i \text{ |(Punktaddition)}''')
                st.latex(r'''\text{Sender berechnet Punkt } Q_A \cdot z_i = P \cdot k_A \cdot z_i = (s_{i1},s_{i2}) \text{ |(Punktaddition)}''')
                st.latex(r'''\text{Sender verschlüsselt Nachrichtenpaar} (t_{i1},t_{i2}) = (m_{i1} \cdot s_{i1}, m_{i2} \cdot s_{i2}) \text{ |(Multiplikation in } F(131^8) \text{ (ist kein Punkt)})''')
                st.write("-----")
            exchange = st.container()
            with exchange:
                st.subheader("Austausch")
                st.latex(r''' \text{Die verschlüsselte Nachricht für jeden Block ist }(R,(t_{i1},t_{i2}))''')
                st.write("-----")
            decryption = st.container()
            with decryption:
                st.subheader("Entschlüsselung")
                st.latex(r''' \text{Empfänger empfängt }(R,(t_{i1},t_{i2}))''')
                st.latex(r'''\text{Empfänger berechnet Punkt } R_i \cdot k_A = P  \cdot z_i \cdot k_A = P \cdot k_A \cdot z_i = (s_{i1},s_{i2}) \text{ |(Punktaddition)}''')
                st.latex(r'''\text{Empfänger entschlüsselt Nachrichtenpaar } (m_{i1},m_{i2}) = (\frac{t_{i1}}{s_{i1}}, \frac{t_{i2}}{s_{i2}}) \text{ |(Division in } F(131^8) \text{ (ist kein Punkt)})''')
                st.latex(r'''\text{Empfänger wandelt Blöcke in entsprechende ASCII-Symbole um} ''')
                st.latex(r'''\text{Empfänger fügt diese Blöcke zu einem String zusammen. Schneidet den ersten Block ab und nimmt so viele Zeichen, wie im ersten Block angegeben}''')
                st.write("-----")

        with tabs[1]:
            col1, col2, col3 = st.columns([10,13,13])

            with col1:
                st.title('Sender')
                st.write(("Text: " + f"**{text}**" ))
                gesamtnachricht = (text_to_ascii(text))
                nachricht = gesamtnachricht[0]
                for i in range (len(gesamtnachricht[1])):
                    for j in range(2):
                        gesamtnachricht[1][i][j] = list(gesamtnachricht[1][i][j])
                
                st.write(np.array(gesamtnachricht[1]))
                st.write("---")
                st.write(np.array(nachricht))
                
            with col2:
                st.title("Austausch")        
                verschlüsselt_mit_schlüsseln = Menezes_Vanstone_encrybtion(nachricht, Kurve, öffentlicher_schluessel_Qa)
                verschlüsselt = verschlüsselt_mit_schlüsseln[0]
                st.write("Verschlüsselt:")
                st.write(verschlüsselt)

            with col3:
                st.title('Empfänger')
                if 'verschlüsselt' in locals():  # Überprüfe, ob die Variable 'verschlüsselt' existiert
                    entschlüsselt = Menezes_Vanstone_decrybtion(verschlüsselt, Kurve, privater_schluessel_a)
                    text_entschlüsselt = ascii_to_text(entschlüsselt)

                    st.write("Entschlüsselt:")
                    st.write(entschlüsselt)
                    st.write(("Text: " + f"**{text_entschlüsselt}**" ))
        for i in range(0, packets):
            with tabs[i+2]:
                encryption = st.container()
                with encryption:
                    st.subheader("Verschlüsselung")
                    if i == 0:
                        st.write("Länge der Nachricht:", str(len(text)))
                    else:
                        st.write(f"**Text : {text[(i-1)*16:i*16]}**" )
                    row1, row2 = st.columns([10,10])
                    with row1:
                        st.write("Text als Blöcke: ", np.array(gesamtnachricht[1][i]))
                    with row2:
                        st.write("In ASCII transformiert: ", np.array(gesamtnachricht[0][i]))
                    m1, m2 = gesamtnachricht[0][i][0], gesamtnachricht[0][i][1]
                    st.write(f"m_1 = " + str(m1) )
                    st.write(f"m_2 = " + str(m2) )
                    st.write("-----")
                    st.write(f'''Generiere privaten Schlüssel **z_{i}** = **{verschlüsselt_mit_schlüsseln[1][i]}**''')
                    st.write(f"Berechne **R** = P * z_{i} = {startpunkt} * {verschlüsselt_mit_schlüsseln[1][i]} = **{verschlüsselt[i][0]}**")
                    s = öffentlicher_schluessel_Qa * verschlüsselt_mit_schlüsseln[1][i]
                    st.write(f"Berechne **(s_1, s_2)** = Q_A * z_{i} = {öffentlicher_schluessel_Qa} * {verschlüsselt_mit_schlüsseln[1][i]} * = **{s}**")
                    st.write(f"Berechne verschlüsselte Nachricht **t_1** = m_1 * s_1 = {m1} * {s.x.value} = **{verschlüsselt[i][1][0].value}** ")
                    st.write(f"Berechne verschlüsselte Nachricht **t_2** = m_2 * s_2 = {m2} * {s.y.value} = **{verschlüsselt[i][1][1].value}** ")

                    st.write("-----")
                    
                exchange = st.container()
                with exchange:
                    st.subheader("Austausch")
                    st.write(f'''Die verschlüsselte Nachricht für diesen Block ist (R,(t_1,t_2)) = ({verschlüsselt[i][0]}, {verschlüsselt[i][1][0].value},{verschlüsselt[i][1][1].value})''')
                    st.write("-----")
                decryption = st.container()
                with decryption:
                    st.subheader("Entschlüsselung")
                    st.write(f"Berechne **(s_1, s_2)** = R_i * K_A = {verschlüsselt[i][0]} * {privater_schluessel_a} * = **{s}**")
                    st.write(f"Berechne entschlüsselte Nachricht **m_1** = t_1 / s_1 = {verschlüsselt[i][1][0].value} / {s.x.value} = **{entschlüsselt[2*i].value}** ")
                    st.write(f"Berechne entschlüsselte Nachricht **m_2** = t_2 / s_2 = {verschlüsselt[i][1][1].value} / {s.y.value} = **{entschlüsselt[2*i+1].value}** ")
                    nachricht1 = ""
                    for j in entschlüsselt[2*i].value:
                        nachricht1 += chr(j)
                    nachricht2 = ""
                    for j in entschlüsselt[2*i+1].value:
                        nachricht2 += chr(j)
                    st.write("m_1 zusammengefügt: " + nachricht1)
                    st.write("m_2 zusammengefügt: " + nachricht2)

                    
                
if __name__ == '__main__':
    
    main()

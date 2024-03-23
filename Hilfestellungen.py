import ipywidgets as widgets
from IPython.display import display, Markdown, clear_output

# Hilfe 0:
# Einlesen von Messdaten
def h_beispiel(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Beispiel)

    Führen Sie die Zelle neu aus, um die Hilfestellung wieder auszublenden.
    
    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)

# Hilfe 1:
# Einlesen von Messdaten
def h_einlesen(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Einlesen von Messdaten)

    Durch den Parameter unpack=True werde die einzelnen Spalten in einzelne numpy-Arrays aufgeteilt. Es muss also für jede übergebene Spalte ein Array erzeugt werden.  
    Wie in dem Einführungs-Notebook gezeigt, kann ein solches Einlesen von Messdaten wie folgt aussehen:

    spalte1, spalte2, spalte3 = np.loadtxt('Name_der_Datei.csv', delimiter='?', skiprows=?, unpack=True)

    Die Fragezeichen und die Namen der Arrays bzw. der Datei müssen noch entsprechend angepasst werden.

    Die Arrays können anschließend mit print(spalte1, spalte2, spalte3) getestet werden.
    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)



# Hilfe 2:
# Plotten der Daten
def h_plotten(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Plotten der Messdaten)

    Die Funktion zum Plotten der Daten muss wie folgt angegeben werden:

    plt.plot(x_werte, y_werte, marker='?', linestyle='?')
    
    Hier müssen "x_"- und "y_werte" mit dem Namen des entsprechenden Arrays sowie die Fragezeichen ersetzt werden.
    Die Funktionen plt.minorticks_on() und plt.grid() können einfach darunter geschrieben werden. Die Zelle muss nach jeder Änderung aktualisiert werden.

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 3:
# Deklaration von Funktionen
def h_function(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Deklaration einer Funktion)

    So kann z. B. die Funktion y = a*x^2 definiert werden:
    
    def name_funktion(a,x)
        y = a * x**2
        return y
    
    Diese berechnet unter Angabe der Werte a und x bei jedem Aufruf y.
    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)

# Hilfe 4:
# Beschleunigungsverlauf
def h_b_function(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Verlauf der Beschleunigung am Federpendel)

    Die gesuchte Funktion für den Beschleunigungsverlauf entspricht einer harmonischen Schwingung. Diese kann angegeben werden als:

    y = - y_0 * cos(omega*t + phi)

    https://de.wikipedia.org/wiki/Schwingung#Harmonische_Schwingung

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 4:
# Raten
def h_guess(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Startwerte für Fit-Funktion)
    
    Der Algorithmus der Fit-Funktion (nächste Zelle) benötigt Startwerte. Für den ersten Test kann überall 1 angegeben werden.

    Bei passenden Anfangswerten wird die Fit-Funktion die konstanten Parameter der Beschleunigungsfunktion (harmonische Schwingung) ermitteln, die dem Verlauf der Messwerte entsprechen. Das kann anschließend in einem Plot (2 Zellen weiter) überprüft werden. Die Parameter passen, falls der über die Fit-Funktion ermittelt Fit die Messwerte widerspiegelt.

    Falls der Plot nicht wie erwartet aussieht, müssen die Anfangswerte angepasst werden. Nach jeder Änderung der Anfangswerte müssen die Zellen der Fit-Funktion und des Plots neu ausgeführt werden.

    Der ausschlaggebendste Parameter ist die Winkelgeschwindigkeit omega. Der Wert liegt in der Regel ungefähr zwischen 2 und 20 (1/s) (abhängig von der Messung).

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 5:
# Fit-Funktion
def h_fit(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Fit-Funktion)
    
    Curve_fit bestimmt die unbekannten Parameter der übergebenen mathematischen Funktion (hier harmonische Schwingung) mit ihren zugehörigen Abweichungen. Dafür müssen curve_fit die Liste der x- bzw. y-Werte sowie die Anfangswerte der unbekannten Konstanten übergeben werden.

    Die von der Fit-Funktion ermittelten Konstanten sowie die Fehlermatrix müssen abgespeichert werden. Dafür bieten sich zwei Arrays an. Diese werden in der Regel "opt" und "cov" genannt.

    Der Code sollte dann wie folgt aussehen:

    opt, cov = otimize.curve_fit(...)

    Mit print(opt) können anschließend die ermittelten Konstanten betrachtet werden.

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 6:
# Plot von Funktionen
def h_plot_function(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Plotten einer Funktion)
    
    Mit den über curve_fit() ermittelten Konstanten und den bekannten x-Werten (Messwerte der Zeit) kann die deklarierte Funktion des Beschleunigungsverlaufs y-Werte berechnen. Wird die Funktion (Beschleunigung) mit einem Arrays (den x-Werten) aufgerufen, gibt sie ein neues Array mit y-Werten zurück.

    Diese y-Werte können plt.plot() direkt übergeben werden:

    plt.plot(x_werte, funktion(x_werte, opt[0], ...), ...)

    Wichtig: Es muss auf die Reihenfolge der Parameter der deklarierten Funktion geachtet werden (die x-Werte sind nicht zwingend an 1. Stelle). -> def function(x,a,b,c)

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)



# Hilfe 7:
# Massen
def h_u_massen(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Unsicherheit der unbekannten Massen)
    
    Die Berechung der Massen kann wie folgt umgesetzt werden:

    m_massestück = ?
    m_smartphone = ?
    
    m1 = m_smartphone
    m2 = m1 + 1*m_massestück
    ...

    massen = [m1,...]   # Array der Massen


    Für die Unsicherheiten kann analog vorgegangen werden. Dabei muss jedoch die Fehlerforpflanzung berücksichtigt werden.

    Beide Arrays (Massen und Unsicherheiten) können abschließend zu einem unp.uarray zusammengeführt werden.
    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 8:
# Funktion ODR
def h_odr_func(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Funktionen in ODR)
    
    Die lineare Funktion muss bei ODR wie folgt deklariert werden:

    def lin_func(beta,x)
        y = beta[0]*x + beta[1]
        return y

    'beta' ist ein Array mit den unbekannten Konstanten. beta[0] entspricht der Steigung und beta[1] dem y-Achsenabschnitt. 


    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 9:
# ODR
def h_odr(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (ODR)
    
    Zuerst muss das Modell definiert werden. Das entspricht der vorher deklarierten Funktion.

    model = Model(?name_funktion?)

    Anschließend werden die bekannten Daten übergeben.

    data = RealData(?x_werte?, ?y_werte?, sx=?unsicherheiten_x?, sy=?unsicherheiten_y?)    
    # Die mit Fragezeichen eingerahmten Arrays müssen entsprechend ersetzt werden

    Im nächsten Schritt wird der Algorithmus deklariert. Dort werden die vorher festgelegten Daten und das Modell sowie die Startwerte der unbekannten Parameter (beta[]) übergeben.

    odr = ODR(data, model, [1,1])

    In den abschließenden Zeilen wird der Algorithmus gestartet, das Ergebnis abgespeichert und ausgegeben.

    out = odr.run()
    out.pprint()



    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)
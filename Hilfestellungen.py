import ipywidgets as widgets
from IPython.display import display, Markdown, clear_output


# Hilfe 1:
# Einlesen von Messdaten
def h_einlesen(b):
    global hilfe_output
    hilfe_text = """
    ### Hilfestellung (Einlesen von Messdaten)

    Durch den Parameter unpack=True werde die einzelnen Spalten in einzelne numpy-Arrays aufgeteilt. Es muss also für jede übergebene Spalte eine Liste erzeugt werden.  
    Wie in dem Einführungs-Notebook gezeigt, kann ein solches Einlesen von Messdaten wie folgt aussehen:

    spalte1, spalte2, spalte3 = np.loadtxt('Name_der_Datei.csv', delimiter='?', skiprows=?, unpack=True)

    Die Fragezeichen und die Namen der Listen bzw. der Datei müssen noch entsprechend angepasst werden.

    Die Listen können anschließend mit print(spalte1, spalte2, spalte3) getesten werden.
    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)



# Hilfe 2:
# Plotten der Daten
def h_plotten(b):
    global hilfe_output
    hilfe_text = """
    ### Hilfestellung (Plotten der Messdaten)

    Die Funktion zum Plotten der Daten muss wie folgt angegeben werden:

    plt.plot(x_werte, y_werte, marker='?', linestyle='?')
    
    Hier müssen "x_"- bzw. und "y_werte" mit dem Namen der entsprechenden Liste sowie die Fragezeichen ersetzt werden.
    Die Funktionen plt.miorticks_on() und plt.grid() können einfach darunter geschrieben werden. Die Zelle muss nach jeder Änderung aktualisiert werden.

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 3:
# Deklaration von Funktionen
def h_function(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Deklaration einer Funktion)

    So könnt ihr z. B. die Funktion y = a*x^2 definieren:
    
    def name_funktion(a,x)
        y = a * x**2
        return y
    
    Diese berechnet unter angabe der Werte a und x bei jedem Aufruf y. Die gesuchte Funktion für den Beschleunigungsverlauf kann hier gefunden werden: 
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
    
    Der Algorithmus der Fit-Funktion (nächste Zelle) benötigt Startwerte. Für den ertsen Test kann überall 1 angegeben werden.

    Bei passenden Anfangswerten wird die Fit-Funktion die konstanten Parameter der Beschleunigungsfunktion (harmonische Schwingung) ermitteln, die den Messwerten entsprechen. Das kann anschließend in einem Plot (2 Zellen weiter) überprüft werden. Die Parameter passen, falls der über die Fit-Funktion ermittelt Fit die Messwerte widerspiegelt.

    Falls der Plot nicht wie erwartet aussieht, müssen die Anfangswerte angepasst werden. Nach jeder Änderung der Anfangswerte müssen die Zellen der Fit-Funktion und des Plots neu ausgeführt werden.

    Der wichtigsten Parameter ist die Winkelgeschwindigkeit omega. Der Wert liegt in der Regel ungefähr zwischen 2 und 20 (1/s) (abhängig von der Messung).

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 5:
# Raten
def h_fit(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Fit-Funktion)
    
    curve_fit bestimmt die unbekannten Parameter der übergebenen mathematischen Funktion (hier harmonische Schwingung) mit ihren zugehörigen Abweichungen. Dafür müssen curve_fit die Liste der x- bzw. y-Werte sowie die Anfangswerte der unbekannten Konstanten übergeben werden.

    Die von der Fit-Funktion ermittelten Konstanten sowie die Fehlermatrix müssen abgespeichert werden. Dafür bieten sich zwei Listen an. Diese werden in der Regel "opt" und "cov" genannt.

    Der Code sollte dann wie folgt aussehen:

    opt, cov = otimize.curve_fit(...)

    Die ermittelten Konstanten sollten anschließend mit print(opt) betrachtet werden.

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 6:
# Raten
def h_plot_function(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Plotten einer Funktion)
    
    Mit den über curve_fit() ermittelten Konstanten und den bekannten x-Werten (Messwerte der Zeit) kann die deklarierte Funktion des Beschleunigungsverlaufs y-Werte berechnen. Wird die Funktion (Beschleunigung) mit einer Liste (den x-Werten) aufgerufen, gibt sie eine neue Liste mit y-Werten zurück.

    Diese y-Werte können plt.plot() direkt übergeben werden:

    plt.plot(x_werte, funktion(x_werte, opt[0], ...), ...)

    Wichtig: Es muss auf die Reihenfolge der Parameter der deklarierten Funktion geachtet werden (die x-Werte sind nicht zwingend an 1. Stelle). 

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)



# Hilfe 7:
# Raten
def h_u_massen(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung (Unsicherheit der unbekannten Massen)
    
    

    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)
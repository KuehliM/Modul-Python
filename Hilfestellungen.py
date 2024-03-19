import ipywidgets as widgets
from IPython.display import display, Markdown, clear_output


# Hilfe 1:
# Funktion zur Anzeige der Hilfszelle
def h_einlesen(b):
    global hilfe_output
    hilfe_text = """
    ### Hilfestellung

    Ihr könnt die Daten auf folgende Weise einlesen:
    ...
    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)



# Hilfe 2:
# Funktion zur Anzeige der Hilfszelle
def h_plotten(b):
    global hilfe_output
    hilfe_text = """
    ### Hilfestellung

    Ihr könnt die Daten auf folgende Weise plotten:
    ...
    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)


# Hilfe 3:
# Funktion zur Anzeige der Hilfszelle
def h_function_def(b):
    global hilfe_output
    hilfe_text = """
    Hilfestellung

    So könnt ihr eine Funktion definieren:
    
    def function(a,b,c)
        return y
    
    """
    clear_output(wait=True)
    hilfe_output = display(Markdown(hilfe_text), display_id=True)
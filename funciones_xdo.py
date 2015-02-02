import os

def go_presentation_mode(xdoscreen):
    os.popen("xdotool windowactivate --sync %s" % xdoscreen)
    os.popen("xdotool key F5")
    return True


def change_evince_page(pagina, xdoscreen):
    os.popen("xdotool windowactivate --sync %s" % xdoscreen)
    os.popen("xdotool key ctrl+l")
    os.popen("xdotool type %s" % pagina)
    os.popen("xdotool key KP_Enter")
    return True

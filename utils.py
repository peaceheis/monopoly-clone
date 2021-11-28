import PySimpleGUI as sg

def get_logo(size, just):
    return [
        sg.T("MONOPOLY"[i], text_color=["red", "orange", "yellowgreen", "green", "blue", "pink", "red", "orange"][i],
             font=("Arial", size), auto_size_text=True, justification=just) for i in range(8)]
    
def complement(color): 
       val = int(color.replace("#", "0x"), base=0)
       return str(hex(0xFFFFFF- val)).replace("0x", "#")

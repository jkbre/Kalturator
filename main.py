import calculator as calc
import sys

app = calc.calculator()
if len(sys.argv) == 1:
    print("Wpisz 'help' by zobaczyć listę dostepnych komend")
app.controlLine()
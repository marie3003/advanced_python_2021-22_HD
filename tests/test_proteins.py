import sys
from pathlib import Path
# -------- START of inconvenient addon block --------
# This block is not necessary if you have installed your package
# using e.g. pip install -e (requires setup.py)
# or have a symbolic link in your sitepackages (my preferend way)
sys.path.append(
    str(Path(__file__).parent.parent.resolve())
)
# It make import peak_finder possible
# This is a demo hack for the course :)
# --------  END of inconvenient addon block  --------

import proteins

def test_protein_name():
    p_A = proteins.basic.Protein('Protein A', "AAA")
    name_t = p_A.name
    assert name_t == "Protein A"
    
def test_protein_sequence():
    p_A = proteins.basic.Protein('Protein A', "AAA")
    sequence_t = p_A.sequence
    assert sequence_t == "AAA"

def test_plot_hist():
    assert
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

def test_find_metric_values():
    p_AR = proteins.basic.Protein('Protein AR', "AR")
    metric_v = p_AR.find_metric_values()
    assert metric_v == [1.8, -4.5]

def test_calculate_sliding_window():
    p_AR = proteins.basic.Protein('Protein AR', "ARARA")
    mean_v = p_AR.calculate_sliding_window()
    assert mean_v == [1.8, -1.35, -0.30000000000000004, -1.35, -0.7200000000000001]

def test_create_positions():
    p_AR = proteins.basic.Protein('Protein AR', "ARARA")
    positions = p_AR.create_positions()
    assert positions == [0,1,2,3,4]
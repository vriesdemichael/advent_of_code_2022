import __main__ as main
from pathlib import Path



def load_data(split_lines=True) -> str | list[str]:
    data_dir = Path(__file__).parent.parent / "data"
    current_day =  Path(main.__file__).stem
    print(current_day)
    current_day_data = data_dir / current_day
    
    data = current_day_data.read_text()
    
    if split_lines:
        return data.splitlines()
        
    return data
    
def load_as_type(type_func):
    """
    Load as a type, e.g. load_as_type(int) -> [1,2,3]
    """
    return [type_func(x) for x in load_data()]


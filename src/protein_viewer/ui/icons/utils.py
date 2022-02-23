from pathlib import Path


hex_content = Path(r"C:\Users\komar\PycharmProjects\protein_viewer\static\icons\icon.png").read_bytes()
Path("app_icon.py").write_text(f"icon = {hex_content}")

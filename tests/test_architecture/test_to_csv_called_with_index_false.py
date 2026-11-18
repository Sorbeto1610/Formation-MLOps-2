"""Architecture test.

Vérifie que tous les appels à `to_csv` faits dans le package
`formation_mlops_2` sont bien appelés avec l'argument `index=False`.

Cela évite d'écrire l'index du DataFrame dans les fichiers CSV générés
(données, prédictions, etc.).
"""
import ast
from pathlib import Path

PACKAGE_ROOT = Path(__file__).parents[2] / "formation_mlops_2"


def test_to_csv_called_with_index_false():
    # Given
    python_files = list(PACKAGE_ROOT.rglob("*.py"))

    # When
    violations = []
    for file_path in python_files:
        tree = ast.parse(file_path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "to_csv"
                and not any(
                    kw.arg == "index"
                    and isinstance(kw.value, ast.Constant)
                    and kw.value.value is False
                    for kw in node.keywords
                )
            ):
                violations.append(f"{file_path.name}:{node.lineno}")

    # Then
    assert python_files, f"No Python files found in {PACKAGE_ROOT}"
    assert not violations, f"to_csv without index=False: {violations}"
    
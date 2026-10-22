import importlib.util
import importlib.machinery
from pathlib import Path


def load_game_module():
    script_path = Path(__file__).resolve().parent / "PythonProjectsAI"
    loader = importlib.machinery.SourceFileLoader("maze_game_app", str(script_path))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load app module from {script_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


game_module = load_game_module()
app = game_module.app


if __name__ == "__main__":
    host = game_module.os.environ.get("HOST", "0.0.0.0")
    port = int(game_module.os.environ.get("PORT", "5000"))
    app.run(host=host, port=port, debug=False)

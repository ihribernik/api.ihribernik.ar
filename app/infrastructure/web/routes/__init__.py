import importlib
import pkgutil


def register_routes(app):
    package = __name__

    for _, module_name, is_pkg in pkgutil.iter_modules(__path__):
        if is_pkg:
            continue
        module = importlib.import_module(f"{package}.{module_name}")
        if hasattr(module, "bp"):
            print(f" * Registering '{module_name}' blueprint")
            app.register_blueprint(module.bp, url_prefix="/api")

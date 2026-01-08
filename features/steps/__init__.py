import os
import pkgutil
import importlib

__all__ = []
PATH = [os.path.dirname(__file__)]
for loader, module_name, is_pkg in pkgutil.walk_packages(PATH):
    __all__.append(module_name)
    full_name = f'{__package__}.{module_name}' if __package__ else f'features.steps.{module_name}'
    _module = importlib.import_module(full_name)
    globals()[module_name] = _module

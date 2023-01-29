"""{{ cookiecutter.project_name.replace('-', ' ').title() }}."""
import pkg_resources


__version__ = pkg_resources.get_distribution("{{cookiecutter.package_name}}").version

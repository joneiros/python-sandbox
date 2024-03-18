# Django Setup

- When creating a Django project, create a virtual environment.
    - This allows module installation per-project, rather than installing
    everything into the global environment
    - `python3 -m venv .venv`
        The last argument is the folder name. VSCode sets this to `.venv`, though
        `venv` is used in [some tutorials](https://realpython.com/python-virtual-environments-a-primer/)
- With `.venv` folder created, activate the environment: `source .venv/bin/activate`
    - This will change the shell environment to act on the venv virtual environment
    - From here, we can install packages into that virtual environment, like
    ```
    python -m pip install django
    ```
    - Even if the code was working before,
    this is handy for resolving missing import warnings in VSCode,
    and allows inspection of the imported classes.
- These added requirements are similar to PHP's `vendor` folder. Pacakges are
installed now, but we want something similar to the `composer.json` file so
that we can consistently get the package versions we expect. That's where a
requirements file comes into play.
    - `python -m pip freeze --local > requirements.txt`
        - The `--local` option skips global requirements
        - These requirements are a great way to track dependencies in your VCS
- When setting up the repo, rebuild packages from `requirements.txt` by:
    - reactivate the venv environment
    - `python -m pip install -r requirements.txt`


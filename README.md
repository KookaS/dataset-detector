# deepfake

Deepfake using the custom dataset managed with [scrapper](https://github.com/KookaS/scrapper) and [gui](https://github.com/KookaS/dataset-gui)

## installation

    python3 -m venv deepfake_env
    
    source deepfake_env/bin/activate

    pip install -r requirements.txt

## pep8

To check with pep8 linter for all files in src:

    pylint src

To auto-format the files:

    black src

## decorators

[decorators](src/decorators/README.md)

Use case:

    from decorators import <DECORATOR>
    @<DECORATOR>
    def function(a):
        pass
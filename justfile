build:
  python3 setup.py sdist
  python3 setup.py build

clean:
  rm -rf dist build

publish:
  twine upload dist/*

sample *name:
  python3 paragon "$(cat ./examples/{{name}}.py)" -a 20

lint:
  pylint paragon

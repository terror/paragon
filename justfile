build:
  python3 setup.py sdist
  python3 setup.py build

clean:
  rm -rf dist build paragon.egg-info

publish:
  twine upload dist/*

one *name:
  python3 paragon -f ./examples/{{name}}.py -a 20

many:
  python3 paragon -f ./examples/comp.py \
                  -f ./examples/hello.py \
                  -f ./examples/sort.py \
                  -a 20
lint:
  pylint paragon

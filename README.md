# upython
Документация по uPython для ESP32-S3

- [MkDocs - Project documentation with Markdown](https://www.mkdocs.org/)
- Сборка
```
$ mkvirtualenv mkdocs -p python3
(mkdocs) $ python -m pip install pip-tools
(mkdocs) $ cd upython
(mkdocs) $ pip-compile docs/requirements.in
(mkdocs) $ pip install -r docs/requirements.txt
(mkdocs) $ deactivate
```
- Сервер разработки
```
$ workon mkdocs
(mkdocs) $ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.06 seconds
INFO    -  [14:29:04] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [14:29:04] Serving on http://127.0.0.1:8000/
```
- [Открыть в браузере](http://127.0.0.1:8000/)
- Статический сайт
```
$ mkdocs build -s --no-directory-urls
```

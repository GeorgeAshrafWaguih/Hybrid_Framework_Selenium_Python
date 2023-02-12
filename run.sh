REM chrome
pytest -s -v -m "sanity" --html=Reports/report.html --browser chrome
REM pytest -s -v -m "regression" --html=Reports/report.html --browser chrome
REM pytest -s -v -m "regression and sanity" --html=Reports/report.html --browser chrome
REM pytest -s -v -m "regression or sanity" --html=Reports/report.html --browser chrome

REM firefox
pytest -s -v -m "sanity" --html=Reports/report.html --browser firefox
REM pytest -s -v -m "regression" --html=Reports/report.html --browser firefox
REM pytest -s -v -m "regression and sanity" --html=Reports/report.html --browser firefox
REM pytest -s -v -m "regression or sanity" --html=Reports/report.html --browser firefox
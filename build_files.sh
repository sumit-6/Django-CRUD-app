echo "BUILD START"
pip install -r requirements.txt
python3.9 -m venv env
env\Scripts\activate
python3.9 manage.py collectstatic
echo "BUILD END"
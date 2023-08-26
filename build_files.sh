echo "BUILD START"
pip install --upgrade pip
pip install --root-user-action=ignore requests
pip install -r requirements.txt
python3.9 manage.py collectstatic
echo "BUILD END"
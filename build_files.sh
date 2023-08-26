echo "BUILD START"
pip install --upgrade pip
pip install --root-user-action=ignore -r requirements.txt
python3.9 manage.py collectstatic
echo "BUILD END"
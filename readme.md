create virtual env with python3:
    virtualenv venv --python python3

activate env:
    source venv/bin/activate

install requirements:
    pip install -r requirements.txt

run app:
    streamlit run main.py
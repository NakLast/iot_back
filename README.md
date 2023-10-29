"# iot_back" 

สร้าง venv env
เข้าไปใช้งาน env/Scripts/activate

pip install -r requirements.txt
หรือ 
pip install fastapi
pip install influxdb_client
pip install pandas

uvicorn main:app --reload

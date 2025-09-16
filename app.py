from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/biodata")
def biodata():
    anggota = [
        {"Nama": "Abdullah Alham", "TTL": "Bekasi, 26 Agustus 2006", "Pendidikan": "S1-Matematika", "foto": "alham.jpg"},
        {"Nama": "Devina Anggraeni Zidny", "TTL": "Bekasi, 03 Desember 2005", "Pendidikan": "Not yet", "foto": ""},
        {"Nama": "Ellva Maulina Bukhari", "TTL": "Bekasi, 09 April 2006", "Pendidikan": "S1-Teknik Industri", "foto": ""},
        {"Nama": "Hafizh Reza Mulia", "TTL": "Magelang, 09 November 2005", "Pendidikan": "S1-Teknik Elektro", "foto": "hafizh.jpg"},
        {"Nama": "Langgeng Widjayanto", "TTL": "Bekasi, 29 September 2006", "Pendidikan": "S1-Matematika", "foto": "langgeng.jpg"},
        {"Nama": "Mutia", "TTL": "Bekasi, 01 Januari 2006", "Pendidikan": "Not yet", "foto": ""},
        {"Nama": "Rinda Najma Kholidiya", "TTL": "Bekasi, 05 November 2005", "Pendidikan": "Not yet", "foto": ""},
        {"Nama": "Syiffarani Bunga Pratiwi", "TTL": "Bekasi, 28 April 2006", "Pendidikan": "S1-Sistem Informasi Kelautan", "foto": ""},
    ]
    return render_template("biodata.html", anggota=anggota)

if __name__ == "__main__":
    app.run(debug=True)



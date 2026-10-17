# NAMIZUN (Fork) — ⚠️ Original Project Retired

> **This is a personal fork of the retired Namizun project.**
>
> The original Namizun is **no longer maintained**. The original author
> recommends using [**github.com/salehi/tavazon**](https://github.com/salehi/tavazon)
> instead.
>
> This fork is kept only for personal/compatibility reasons.
> **Use at your own risk.**

---

## ⚠️ Why the original Namizun was retired

The original project had two fundamental detection problems:

- **Traffic "ceiling" and sharp edges at the start of each hour.**
  The traffic pattern resets/spikes when the hour changes, producing a visible
  step in monitoring graphs. On tools like **PRTG**, those edges are obvious
  to the naked eye.

- **Identical packet fingerprint.**
  Every packet shares the same fingerprint, which is hard evidence a NOC can
  use to prove you are sending junk traffic.

The successor project **[Tavazon](https://github.com/salehi/tavazon)** fixes
both issues (smooth traffic distribution, non-repeating packet fingerprint,
single static binary, built-in web panel, MaxMind GeoIP support).

👉 **If you are starting fresh, use [Tavazon](https://github.com/salehi/tavazon) instead.**

---

## 📦 About this fork

This fork (`aliamg1356/namizun`) keeps the original Namizun codebase intact
and only updates the repository URLs so the install/update scripts work
against this fork.

- Original repo: `github.com/malkemit/namizun` (retired)
- This fork:    `github.com/aliamg1356/namizun`

This project is used to remove the limitation of asymmetric ratio for
uploading and downloading Iranian servers.

### Dockerized installation

```bash
git clone https://github.com/aliamg1356/namizun
cd namizun
docker-compose pull
docker-compose up -d
You need menu to adjust settings?
bash
docker-compose run --rm --entrypoint bash namizun
python3 menu.py
You want to build docker image by yourself?
bash
docker-compose build namizun
One line installation command:
bash
sudo curl https://raw.githubusercontent.com/aliamg1356/namizun/master/else/setup.sh | sudo bash
Manual installation
Important Note: use it on Ubuntu 20+ (Python 3.8+)

Install pip, redis & git:
bash
sudo apt install python3-pip python3-venv redis git -y
Note: Sometimes Redis does not start automatically, start it with:

bash
sudo systemctl start redis.service
Create a directory to clone the project:
bash
mkdir -p /var/www/namizun && cd /var/www/namizun
Clone the project with Git:
bash
git init
bash
git remote add origin https://github.com/aliamg1356/namizun.git
bash
git pull origin master
Make virtual environment:
bash
python3 -m venv /var/www/namizun/venv
Install the project requirements with pip by setup.py (namizun_core & namizun_menu):
bash
cd /var/www/namizun && source /var/www/namizun/venv/bin/activate && pip install wheel && pip install namizun_core/ namizun_menu/ && deactivate
Create service for uploader.py (for running namizun script):
bash
ln -s /var/www/namizun/else/namizun.service /etc/systemd/system/
Reload the service files and start namizun.service:
bash
sudo systemctl daemon-reload && sudo systemctl enable namizun.service && sudo systemctl start namizun.service
Create namizun command to execute menu.py:
bash
ln -s /var/www/namizun/else/namizun /usr/local/bin/ && chmod +x /usr/local/bin/namizun
Update
With the following command, you can update the script you have already installed:

bash
cd /var/www/namizun && git reset --hard HEAD && git pull origin master && source /var/www/namizun/venv/bin/activate && pip install namizun_core/ namizun_menu/ && deactivate && systemctl daemon-reload && chmod +x /usr/local/bin/namizun
Configuration
See the original tutorial (Persian): command list of namizun

Notes:
In this script, you don't need to buy a download host or another server, or even upload to your foreign server.
Only fake traffic will be sent to Iranian IPs, which will be lost.

Although the essence of this script is used to attack, due to the limited size of the buffer and the distribution of traffic between different IPs, this does not happen in practice.
(To attack, many servers must send traffic to one IP, but this works exactly the opposite.)

This script is designed to upload up to 50 terabytes of traffic at maximum; it can be used on a server with minimal resources.

If you want to use a speed of more than 3, pay attention to CPU consumption.
High CPU consumption will cause restrictions from the provider (at least 2 CPU cores recommended).

If you are using a dedicated server, it is suggested to virtualize it and use your virtual servers.
This way, your traffic will be distributed among more IPs and will prevent you from being banned.

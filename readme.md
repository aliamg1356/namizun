# NAMIZUN — ⚠️ Retired / Archived

> **This project is no longer maintained.**
>
> ## 👉 Use [**github.com/salehi/tavazon**](https://github.com/salehi/tavazon) instead.
>
> Everything below is kept **as an archive only**. Do not use it for new setups.

---

## Why Namizun is retired

Namizun did its job, but it has two fundamental detection problems that make it
easy to catch:

- **Traffic "ceiling" and sharp edges at the start of each hour.**
  The traffic pattern resets/spikes when the hour changes, producing a visible
  step in the monitoring graphs. On tools like **PRTG**, those edges are obvious
  to the naked eye — a NOC operator can spot the pattern just by looking at the
  chart.

- **Identical packet fingerprint.**
  Every packet shares the same fingerprint. That repeating signature is hard
  evidence the NOC can use to prove you are sending garbage/junk traffic.

## Tavazon fixes all of this

[**Tavazon**](https://github.com/salehi/tavazon) is the successor and solves
every problem above:

- ✅ **One-line install** via systemd
- ✅ **Single static binary, under 3 MB**
- ✅ Built-in **web panel**
- ✅ Uses **MaxMind `.mmdb`** GeoIP databases — target by **Country**, by
  **AS (ASN)**, or even a **single IP**
- ✅ Panel to set the **exact amount of traffic to send over a 24-hour period**
- ✅ **Smooth traffic distribution — no edges/spikes at hour changes**, so
  PRTG-style monitoring can't pick it out by eye
- ✅ **No repeating packet fingerprint**

The PRTG admins are out of luck. 😎

### 👉 Get started at [github.com/salehi/tavazon](https://github.com/salehi/tavazon)

---

## 📦 Archive — original Namizun documentation

> The content below is preserved for historical reference only and is
> **no longer maintained**.

This project is used to remove the limitation of asymmetric ratio for uploading and downloading Iranian servers

### Dockerized installation

```bash
git clone https://github.com/aliamg1356/namizun
cd namizun
docker-compose pull
docker-compose up -d
```

#### You need menu to adjust settings?

```bash
docker-compose run --rm --entrypoint bash namizun
python3 menu.py
```

#### You want to build docker image by yourself?
```bash
docker-compose build namizun
```

### One line installation command:

```bash
sudo curl https://raw.githubusercontent.com/aliamg1356/namizun/master/else/setup.sh | sudo bash
```

### Manual installation

**Important Note : use it on ubuntu +20 (python +3.8)**

- 1\) you need to install pip, redis & git:

```bash
sudo apt install python3-pip python3-venv redis git -y
```

- Note: Sometimes Redis does not start automatically, start it with the following command

```bash
sudo systemctl start redis.service
```

- 2\) you need to create a directory to clone the project:

```bash
mkdir -p /var/www/namizun && cd /var/www/namizun
```

- 3\) Clone the project with Git:

```bash
git init
```

```bash
git remote add origin https://github.com/aliamg1356/namizun.git
```

```bash
git pull origin master
```

- 4\) make virtual environment:

```bash
python3 -m venv /var/www/namizun/venv
```

# تنظیم منبع آینه‌ای Tsinghua به عنوان پیش‌فرض
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# اگر با خطای SSL مواجه شدید، دستور زیر را اضافه کنید (معمولاً لازم نیست)
# pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn


- 5\) Install the project requirements with pip by **setup.py** (namizun_core & namizun_menu):

```bash
cd /var/www/namizun && source /var/www/namizun/venv/bin/activate && pip install wheel && pip install namizun_core/ namizun_menu/ && deactivate
```

- 6\) Create service for uploader.py (for running namizun script):

```bash
ln -s /var/www/namizun/else/namizun.service /etc/systemd/system/
```

- 7\) Reload the service files to include the new service and start **namizun.service** :

```bash
sudo systemctl daemon-reload && sudo systemctl enable namizun.service && sudo systemctl start namizun.service
```

- 8\) Create **namizun** command to execute **menu.py**

```bash
ln -s /var/www/namizun/else/namizun /usr/local/bin/ && chmod +x /usr/local/bin/namizun
```

### Update

- With the following command, you can update the script that you have already installed:

```bash
cd /var/www/namizun && git reset --hard HEAD && git pull origin master && source /var/www/namizun/venv/bin/activate && pip install namizun_core/ namizun_menu/ && deactivate && systemctl daemon-reload && chmod +x /usr/local/bin/namizun
```

### Configuration

- see our tutorial : [command list in persian](https://telegra.ph/commandlist-of-namizun-12-26)

### Notes:
- In this script, you don't need to buy a download host or another server or even upload to your foreign server.\
Only fake traffic will be sent to **Iranian IPs**, which will be lost!


- Although the essence of this script is used to attack, but due to the **limited size of the buffer** and the **distribution of traffic between different IPs**, this does not happen in practice.\
(To attack, many servers must send traffic to one IP, but **this works exactly the opposite**)


- This script is designed to upload up to **50** terabytes of traffic at maximum, it can be used on a server with minimal resources.


- If you want to use a speed of more than 3, be sure to pay attention to the **CPU consumption**.\
High CPU consumption will cause restrictions from the provider (it is better to have at least 2 CPU cores)


- If you are using a **dedicated server**, it is suggested to virtualize it and use your virtual servers.\
In this way, your traffic will be distributed among more IPs and will prevent you from being banned.

# Odoo
## Odoo install
```
apt-get install postgresql -y
sudo apt install virtualenvwrapper
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
sudo apt install build-essential python3-dev libxslt-dev libzip-dev libldap2-dev libsasl2-dev
mkvirtualenv -p /usr/bin/python3 odoo-venv
$ cd your_odoo_sources_path
$ pip install -r requirements.txt

git clone https://github.com/odoo/odoo.git -b 11.0 --depth = 1 # Получить исходный код Odoo

./odoo/setup/setup_dev.py setup_deps # Устанавливает системные зависимости Odoo
$ ./odoo/setup/setup_dev.py setup_pg # Устанавливает PostgreSQL и db пользователя

```

When you you want to leave the virtual environment, just issue this command:
`deactivate`
Whenever you want to work again with your 'odoo-venv' environment:
`workon odoo-venv`

## Odoo debug run


`$ odoo/odoo-bin -d mail_create_lead --dev=all -c odoo.conf`
## Known problems
* your text there :)
## 10 Common Mistakes Made by a New Partner
### 1. Low pricing
### 2. Fixed price commitment
### 3. No sales relationship with my AM
### 4. Lack in software demonstration
### 5. Selling too... BIG
#### Start small, expand big!
### 6. My first project on my own
### 7. Neglecting training
#### "Kill yourself in training so you don't die fighting"
### 8. I develop, therefor I'am.
####Know the functional scope, develop when needed.
### 9. Too much focus on new customers rasher than customer base.
#### Work on your installed base!
### 10. Low visibility
#### Make some noise for (nearly) free!
#### Your Website
* Work on you SEO
* LEAD GENERATION: Give CONTENT to get leads!
	- Ex 1 Webinar every 2 weeks (Discover CRM...)
	- Write a White book (Odoo Vs netsuite...)
* Invest in Customer Success Stories, this is GOLD
* More than 85 available today, let's contribute!
#### Contribute
* Who are the Best / Recognized Partners? The Best Contributors!

* Quality modules will bring you Customers
* Publish on GitHub
* Reference you Odoo Modules
#### Be social
* Just speak about you, Success Stories, Webinar, contribution, modules on all the Social Networks


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
$ sudo createuser --superuser $(whoami)
$ createdb demo
```

some trash
```
sudo apt-get install -y git python3.5 postgresql nano virtualenv xz-utils wget fontconfig libfreetype6 libx11-6 libxext6 libxrender1 node-less node-clean-css xfonts-75dpi

wget -O wkhtmltox.tar.xz https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz 

sudo apt-get install -y gcc python3.5-dev libxml2-dev libxslt1-dev libevent-dev libsasl2-dev libssl1.0-dev libldap2-dev libpq-dev libpng-dev libjpeg-dev

git config --global user.name "Your Name"

python3 odoo-bin -d odoo-test --addons-path=addons --db-filter=odoo-test

python3 odoo-bin -d odoo-test --addons-path=addons \ 
--db-filter=odoo-test
```


When you you want to leave the virtual environment, just issue this command:
`deactivate`
Whenever you want to work again with your 'odoo-venv' environment:
`workon odoo-venv`

## Режим разработки сервера Odoo
`--dev=all --log-level=debug `
`$ odoo/odoo-bin -d mail_create_lead --dev=all -c odoo.conf`

В Odoo 10 был добавлен новый вариант, обеспечивающий отличные возможности для разработчиков. 
Чтобы использовать его, запустите экземпляр сервера с дополнительной опцией `--dev = all`.
Это активирует несколько удобных функций которые ускорят наш цикл разработки. 
Наиболее важными являются:
* Автоматическая перезагрузка кода Python, как только файл Python будет сохранен, избегая ручного перезапуска сервера
* Чтение view описаний непосредственно из файлов XML, избегая ручного обновления модулей

## Debug
Для того чтобы установить уровень ведения журнала `my_module loggers` на `DEBUG` и 
сохранить уровень журнала по умолчанию для других аддонов, можно запустить Odoo следующим образом:
`python odoo.py --log-handler=odoo.addons.my_module:DEBUG`

## Работа с зависимостями
```
$ pip install pip-tools
$ pip-dump
```

## Интерактивная работа с Odoo
`$ ./odoo-bin shell -c project.conf --log-level=error`

`>>> product = env['product.product']`
`>>> location_stock = env.ref('stock.stock_location_stock')`
`>>> product.export_stock_level(location_stock)`
Завершаем транзакцию перед выходом
`>>> env.cr.commit()`
выходим из интерактивного режима с помощью `Ctrl + D`


## Тестирование модуля
Заполняем базу тестовыми данными
`$ ./odoo-bin -c project.cfg --without-demo=False --stop-after-init -i my_module`
`$ ./odoo-bin -c project.cfg --test-enable --log-level=error --stop-after-init -u my_module`



## Наследование в Odoo

Inheritance :

Inheritance mechanism is used to create idea of re usability.there re usability means that reuse the code of the parent class in any Object Oriented Programming.

**Advantages** :

* Reduce code redundancy.
* Provides code reusability.
* Reduces source code size and improves code readability.
* Code is easy to manage and divided into parent and child classes.
* Supports code extensibility by overriding the base class functionality within child classes.

**Disadvantages** :

In Inheritance base class and child classes are tightly coupled. Hence If you change the code of parent class, it will get affects to the all the child classes.

In class hierarchy many data members remain unused and the memory allocated to them is not utilized. Hence affect performance of your program if you have not implemented inheritance correctly.

There are two way to inheritance in Odoo.

1.Classical Using Pythonic Way :

It allows to add specific "generic" behavior to Model by inheriting classes that derive from orm.Model like geoModel that adds goegraphic support.
```
class Myclass(GeoModel, AUtilsClass):
```
**Using _inherit :-**

The main objective is to add new behaviors/extend existing models. For example you want to add a new field to an invoice and add a new method

class AccountInvoice(orm.Model):
    _inherit = "account.invoice"
    _column = {'my_field': fields.char('My new field')}
    def a_new_func(self, cr, uid, ids, x, y, context=None):
        # my stuff
        return something

**override the existing method :**
```
def existing(self, cr, uid, ids, x, y, z, context=None):
    parent_res = super(AccountInvoice, self).existing(cr, uid, ids, x, y, z, context=context)
    # my stuff
    return parent_res_plus_my_stuff
```
2.Polymorphic Way :-

Using _inherits :-

When using _inherits you will do a kind of polymorphic model in the database way.

For example product.product inherits product.template or res.users inherits res.partner. This mean we create a model that gets the know how of a Model but adds aditional data/columns in a new database table. So when you create a user, all partner data is stored in res_partner table (and a partner is created) and all user related info is stored in res_users table.

To do this we use a dict: `_inherits = {'res.partner': 'partner_id'}` The key corresponds to the base model and the value to the foreign key to the base model.

As same through XML you can do the inherit the Odoo views (like Form view,Tree view,Search View etc ..) and you can also change the behaviour from the view

Key point :

The above two method can be apply on the Odoo server side and which you can change the behaviour of existing view or any other things you can change in Odoo views the effect with on your client side.
[Ref](https://stackoverflow.com/questions/30712300/inheritance-in-openerp-odoo)




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


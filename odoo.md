# Odoo
## Odoo Backup
### Backup базы данных
```
pg_dump --user=odoo odoo | gzip -9 > /opt/odoo/YYYYMMDD-server.sql.gz
```


## Стандарт структуры проекта
Рекомендуется что бы dev окружение и prod окружение использовали приведённую ниже структуру каталога. Этот стандарт будет полезен, когда придётся выполнять операции по техническому обслуживанию, а так же облегчит повседневную работу.
Рецепт приведённый ниже создаёт структуру каталогов, которая группирует файлы, имеющие аналогичные жизненные циклы или аналогичное назначение в стандартизированные подпапки. Структура может быть изменена но она должна быть задокументирована.

Чтобы создать предложенный макет экземпляра, вам необходимо выполнить следующие действия:
Создаём одну директорию для каждого экземпляра
```
$ mkdir ~/odoo-dev/projectname
$ cd ~/odoo-dev/projectname
```
Создаём `virtualenv` в подпапке `env/`:
`$ virtualenv -p python3 env`
Создаём подпапки
`$ mkdir src local bin filestore logs`
Функции у папок следующие
src/: содержит клон самого Odoo и различных сторонних проектов-аддонов
local/: используется, чтобы сохранить специфичные для экземпляра аддоны
bin/: включает в себя различные вспомогательные исполняемые сценарии оболочки
filestore/: используется как хранилище файлов
logs/ (опционально): используется для хранения лог файлов

клонирование основного репозитория и установка вспомогательных модулей
```
$ git clone https://github.com/odoo/odoo.git src/odoo
$ env/bin/pip3 install -r src/odoo/requirements.txt
```

Скрипт ниже записываем в bin/odoo
```
#!/bin/sh
ROOT=$(dirname $0)/..
PYTHON=$ROOT/env/bin/python3
ODOO=$ROOT/src/odoo/odoo-bin
$PYTHON $ODOO -c $ROOT/projectname.cfg "$@"
exit $?
```
Добавляем права на выполнение
`$ chmod +x bin/odoo`

Создаём пустой фиктивный локальный модуль:
```
$ mkdir -p local/dummy
$ touch local/dummy/__init__.py
$ echo '{"name": "dummy", "installable": False}' >\ local/dummy/__manifest__.py
```
Создаём файл конфигурации для экземпляра:
```
$ bin/odoo --stop-after-init --save \
 --addons-path src/odoo/odoo/addons,src/odoo/addons,local \
 --data-dir filestore
```
Добавляем в  `.gitignore` игнор на `filestore/, env/, logs/` и `src/`:

```
# dotfiles, with exceptions:
.*
!.gitignore
# python compiled files
*.py[co]
# emacs backup files
*~
# not tracked subdirectories
/env/
/src/
/filestore/
/logs/
```
Создаём репозиторий Git для этого экземпляра и добавляем файлы, которые добавили в git:

```
$ git init
$ git add .
$ git commit -m "initial version of projectname"
```

**Пояснения**
Создаем чистую структуру каталогов с четко обозначенными каталогами и выделенными ролями; особенно, разделяем следующее:
Код, поддерживаемый другими людьми (src/)

## Odoo install
**todo** https://linuxize.com/post/install-odoo-11-on-ubuntu-16-04/

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

## How to `--dev=all` works
* When `.py` file is changed. Newer source code must be compiled to get the changes  ---->  Restart server
* When `.xml` file is changed. Database records must be updated to get the change ----> Update (upgrade) your module
* When `.js` file is changed.  Browser cache must be updated -----> Refresh web page


## Debug
Для того чтобы установить уровень ведения журнала `my_module loggers` на `DEBUG` и 
сохранить уровень журнала по умолчанию для других аддонов, можно запустить Odoo следующим образом:
`python odoo.py --log-handler=odoo.addons.my_module:DEBUG`

## Logging
`_logger = logging.getLogger(__name__)`
To write log messages in method code we can use:
```
_logger.info()
_logger.debug()
_logger.warning()
_logger.exception()
```

## Вывод debug сообщений только для заданного модуля
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

Ключевой частью этого рецепта является флаг командной строки `--test-enable`, который указывает Odoo на запуск тестов. Флаг `--stop-after-init` остановит экземпляр после запуска тестов, а `-u `обновит указанный модуль. Когда обновление (или установка) выполняется с включенными тестами, запускаются все протестированные модули модулей аддона \(это автоматически зависит от автоматически устанавливаемых зависимостей или обратных зависимостей\).


Если тесты не выполняются, убедитесь, что у вас есть демо-данные для модуля; в файле конфигурации параметр `no_demo` должен быть `False`. Если есть сомнения, можно форсировать no_demo=false, запустив `UPDATE ir_module_module SET demo = true WHERE name = 'my_module'`.
Можно запускать тесты, используя конфигурацию журнала `log-level = error -log-handler = odoo.modules.loading: INFO`. Это позволяет нам получать информацию о обрабатываемых файлах различных тестов, но не о деталях журналов операций, а только сообщения об ошибках.


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

## Useful links
[How to add Chatter to an existing model](http://www.odooninja.com/add-chatter-existing-model/)


## About creating values when field is a one2many or many2many
You cant create values in a many2many field just giving it the id (this is only for many2one). If the field is a one2many or many2many:
```
(0, 0, { values }) link to a new record that needs to be created with the given values dictionary
(1, ID, { values }) update the linked record with id = ID (write values on it)
(2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
(3, ID) cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
(4, ID) link to existing record with id = ID (adds a relationship)
(5) unlink all (like using (3,ID) for all linked records)
(6, 0, [IDs]) replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
```

So, what you should add is instead of a list, [(4, emp.employee_id.id)]

## how to colorize line in list view

For v9, colors are gone - replaced by the following decorators:
decoration-bf - shows the line in BOLD
decoration-it - shows the line in ITALICS
decoration-danger - shows the line in LIGHT RED
decoration-info - shows the line in LIGHT BLUE
decoration-muted - shows the line in LIGHT GRAY
decoration-primary - shows the line in LIGHT PURPLE
decoration-success - shows the line in LIGHT GREEN
decoration-warning - shows the line in LIGHT BROWN

The formatting is dependent on the bootstrap style, and these can be combined (the colors look better when shown bold).


## One2many many2one
In OpenERP we can create many2one and one2many relationships between models very easily by creating many2one and one2many fields. You just need to declare a field in _columns and then using this field normally in the rest programming and views as we normally do.
I created a small module to explain called hospital, I have two objects patient and doctor. To establish relationship between these two entities or objects, create doctor_id field in patient model as many2one, and patient_id as one2many in doctor model.
The relationship can be explained as one doctor with many patients and many patients going to a single doctor.
Now create a many2one field as:
in class patient(osv.osv):
```
'doctor_id':fields.many2one('doctor','Doctor'),
```
and in class doctor(osv.osv):
```
'patient_id':fields.one2many('patient','doctor_id',),
```


# QWeb
## diff between t-esc t-raw

The difference is in HTML (code) parsing or not. When you use t-esc it will literally print out the value from the field you want to print. When you use t-raw in combination with an HTML field for example it will keep the content in HTML. If you would do a t-esc on an HTML field it will print your HTML code without interpreting it to actual code.
For example you have a field with:
`<p>My code</p>`
If you would use t-raw it will be handled as HTML and so your `<p>` element won't be shown because it is converted. When you would do the same with t-esc it would literally print `<p>My code</p>` on your report.



# Interesting parts

```
<t t-set="atts" t-value="product.get_variant_groups()"/>
<t t-if='len(atts)'>
    <h3 class="text-center mb32">Specifications for <t t-esc="product.name"/></h3>
    <div class="row">
        <div class='col-md-8 col-md-offset-2' id='product_specifications'>
            <table class='table table-striped table-condensed table-hover'>
                <t t-foreach="atts.keys()" t-as="spec">
                    <t t-if="len(atts.keys())&gt;1">
                        <tr class="success text-left breadcrumb clickable" data-toggle="collapse" t-att-data-target="'.'+spec.split()[0]">
                            <th t-att-colspan="2"><t t-esc="spec"/></th>
                        </tr>
                    </t>
                    <tr t-foreach="atts[spec]" t-as="att" t-att-class="'collapse in ' + spec.split()[0]">
                        <td t-esc="att.attribute_id.name"/>
                        <td>
                            <t t-set='or_separator'>or</t>
                            <t t-esc="(' %s ' % or_separator).join(att.value_ids.mapped('name'))"/>
                        </td>
                    </tr>
                </t>
            </table>
        </div>
    </div>
</t>

```

## Refresh window by button
```
return {
                'type': 'ir.actions.client',
                'tag': 'reload',
                }
```

## Complex domain
```
[
                '|',
                    '&',
                        ('task_id.project_id.privacy_visibility', '=', 'portal'),
                        ('task_id.project_id.message_partner_ids', 'child_of', [user.partner_id.commercial_partner_id.id]),
                    '&',
                        ('task_id.project_id.privacy_visibility', '=', 'portal'),
                        ('task_id.message_partner_ids', 'child_of', [user.partner_id.commercial_partner_id.id]),
            ]
```

## Compute from one currency to another currency
```
res = self.env['res.currency'].browse(FROM_CURRENCY).compute(move_line.amount_currency, move_line.company_id.currency_id)


inv = self.env['account.invoice'].browse(invoice_id)
currency = inv.currency_id.with_context(date=inv.date_invoice) # Invoice Currency
company_currency = inv.company_id.currency_id  # Company Currency
currency.compute(AMOUNT, company_currency)   # From Invoice Currency, amount is converted to Company's Currency
```


## Different between col and colspan?
Every form view container (form itself, group, page, I think there are more) in OpenERP consists of 4 columns to start with.
```<form>
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │
└───┴───┴───┴───┘
</form> 
```
Every <field> takes 2 columns: label & input field
```
<field name="input" />
<field name="inpt2" />
┌───────┬───────┬───────┬───────┐
│ label │ input │ labl2 │ inpt2 │
└───────┴───────┴───────┴───────┘ 
```
With colspan, you can widen items.
```
<field name="inpt4" colspan="4"/>
<field name="input" />
<field name="inpt2" />
┌───────┬───────────────────────┐
│ labl4 │ inpt4_______________  │
├───────┼───────┬───────┬───────┤
│ label │ input │ labl2 │ inpt2 │
└───────┴───────┴───────┴───────┘

<field name="input" />
<field name="inpt4" colspan="4"/>
<field name="inpt2" />

┌───────┬───────┬───────┬───────┐
│ label │ input │       │       │
├───────┼───────┴───────┴───────┤
│ labl4 │ inpt4_______________  │
├───────┼───────┬───────┬───────┤
│ labl2 │ inpt2 │       │       │
└───────┴───────┴───────┴───────┘ 
```
When you add additional containers, like a page, you can tell OpenERP to use more or less columns.
```
<group col="2" colspan="2">
    <field name="a" />
    <field name="b" />
</group>
<group col="6" colspan="2">
    <field name="d" />
    <field name="e" />
    <field name="f" />
</group>
│       │       │                │                │
├───────┴───────┼────────────────┴────────────────┤
│ ┌────┬───┐    │  ┌────┬───┬────┬───┬────┬───┐   │
│ │ lb │ a │    │  │ lb │ d │ lb │ e │ lb │ f │   │
│ ├────┼───┤    │  └────┴───┴────┴───┴────┴───┘   │
│ │ lb │ b │    │                                 │
│ └────┴───┘    │                                 │
├───────┬───────┼────────────────┬────────────────┤
│       │       │                │                │
```

## How to add popup window in odoo 11
Необходимо добавить вьюху в манифест
```
<?xml version="1.0" encoding="utf-8"?>
<odoo>
        <template id="assets_backend_2" name="crm assets 2" inherit_id="web.assets_backend">
            <xpath expr="//script[last()]" position="after">
                <!-- dialog assets -->
                <script type="text/javascript" src="/ds_crm/static/src/js/my_dialog.js"></script>
            </xpath>
        </template>
</odoo>
```
js в static/js
```
odoo.define('ds_crm.my_dialog', function(require){
"user strict";

var core = require('web.core');
var session = require('web.session');

var qweb = core.qweb;
var mixins = core.mixins;
var Widget = require('web.Widget');
var rpc = require('web.rpc');
var Dialog = require('web.Dialog');
console.log('ds_crm_log');
function ActionShowDialog(parent, action){
    var dialog = new Dialog(document.body, {
        title: "not implemented yet",
        subtitle: "not implemented yet",
        size: 'medium',
        $content: "<div id='my_div'>not implemented yet</div>",
        buttons: []
    });
    dialog.open();
    setTimeout(function(){
        dialog.close();
        rpc.query({
            model: 'ds_crm.lead',
            method: 'my_dialog_func',
            //args: [], //here pass parameters of python function
        });
    }, 3000);
}

    core.action_registry.add("show_my_dialog", ActionShowDialog);
    console.log('ds_crm_log_2');
});
```
```
    @api.model
    def my_dialog_func(self):
        """необходимо для диалогового окна
        """
        pass
```
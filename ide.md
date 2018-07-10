# IDE
##Важные факты о JVM

Первое, JVM очень не любит swapping. Если мне жалуются, что java-приложение почему-то тормозит, то первое, что я делаю, это смотрю, нет ли на сервере своппинга. Потому что есть два фактора, делающих Java очень нетолерантной к свопингу:
* Сборка мусора в Java постоянно бегает по страничкам, и если она «промахивается» мимо резидентных страниц, то вызывает перекладывание страниц с диска в память и обратно.
* Если в JVM хотя бы один поток «наступил» на страницу, которой в памяти нет, то это может привести к заморозке всех потоков этой JVM.

Есть механизм safe-point, который используется в JVM для всякой чёрной магии вроде перекомпиляции кода на лету, сборки мусора и так далее. Если один поток попал на Page Fault и ждёт, то JVM не может нормально войти в состояние safe-point, потому что не получает подтверждение от потока, который ждёт «приезда» страницы памяти. А все остальные потоки уже остановились и тоже ждут. Все стоят, ждут один этот несчастный поток. Поэтому, как только у вас начинается пейджинг, может начаться очень существенная деградация производительности.

Второе, Java никогда не отдаёт память операционной системе. Она будет использовать столько, сколько вы разрешили, даже если ей сейчас не очень нужны эти ресурсы, она их обратно не отдаст. Есть сборщики мусора, которые технически умеют это делать, но не надо рассчитывать, что они будут это делать.
У сборщика мусора такая логика работы: он либо использует больше 
CPU, либо больше памяти. Если вы ему разрешили использовать 10 Гбайт, значит он разумно предполагает, что можно экономить ресурсы CPU, а эти 10 гигабайт с мусором подождут, а CPU пока пусть лучше делает делает что-то полезное, вместо чистки памяти, которая ещё не выходит за лимит.

В связи с этим важно правильно и обоснованно выставлять размер JVM. А если у вас несколько процессов в рамках одного контейнера, разумно распределять ресурсы памяти между ними.

Иначе пострадают все, что находится в этом контейнере.

# PyCharm 
##Remote access with pgAdmin to Odoo postgre database on Ubuntu
This is for PgAdmin integration, but same method working with PyCharm.
STEP #1 – get pgAdmin Install pgAdmin from pgadmin.org
STEP #2 – allow postgre server remote connections from everywhere Open `etc/postgresql/9.x/main/pg_hba.conf` and add following line: `host all all all md5`
STEP #3 – let the postgre server listen to everyone Open `etc/postgresql/9.x/main/postgresql.conf` and change following line: `listen_addresses = '*'`
STEP #4 – give the user “postgres” a password Start the psql terminal: sudo -u postgres psql Give a password: `ALTER USER postgres PASSWORD 'yourpassword';`Leave the psql terminal: `q`
STEP #5 Restart postgre server by executing this terminal command: `sudo /etc/init.d/postgresql restart`
STEP #6 Start pgAdmin and add a connection to a server

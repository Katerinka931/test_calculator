<h2>Калькулятор</h2>
<h3>Инструкция по запуску</h3>

<h5>Настройка проекта</h5>


1. Для начала откройте настройки File -> Settings -> Languages & Frameworks -> Django. В графе Django project root выберите test_opencode (папка, содержащая проект, должна быть одноименной), а в графе Settings - "test_opencode/settings.py". <br/>
2. Настроим виртуальнео окружение. Перейдем в настройки -> Project -> Python Interpreter -> Add interpreter -> Add local interpreter -> Virtual Environment. Выбираем нужный интерпретатор и устанавливаем в корневую папку проекта. 
Теперь перейдем в виртуальное окружение и активируем его. Для этого в терминале выполнить команды: cd .\venv\Scripts , .\activate, после чего вернуться в корневую папку проекта.<br/>
3. Далее установим зависимости. Для этого в терминале в корневой папке проекта пропишем команду pip install -r requirements.txt. Дожидаемся загрузки зависимостей. <br/>
4. Теперь откройте настройки конфигурации EditConfigurations... -> Add new -> DjangoServer.<br/>


<h5>Использование проекта</h5>
<p>
1. Запускаем проект. <br/>
2. Открываем, например, Postman. Отправлять данные будем в формате JSON в теле запроса. В Постман для этого надо выбрать "Body", "raw" и "JSON". <br/>
3. Выбираем POST-запрос. После пишем тело запроса. В строке адреса вводим "http://localhost:8000/calculate" <br/>
</p>
<pre>
{
    "expression": "4-2*a/(5*x-3)",
    "variables": {
            "a": 2.5,
            "x": 0
        }
}

или 

{
    "expression": "4-2*a/(5*x-3)",
    "variables": {
            "a": 2.5
        }
}
</pre>
<pre>
{
    "expression": "log(10+log(10))*5+lg(a)",
    "variables": {
            "a": 100,
            "x": 0
        }
}
</pre>

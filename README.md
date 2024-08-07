# Приложение интернет магазина


## Задание 1

 Настройте виртуальное окружение.
 Создайте новый Django-проект.

## Задание 2
После успешного создания проекта сделайте первую настройку. Для этого:

 Создайте первое приложение с названием catalog.
 Внесите начальные настройки проекта.
 Сделайте настройку урлов (URL-файлов) для нового приложения.

## Задание 3
Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.
Для создания шаблонов лучше использовать UIkit Bootstrap. Это удобный набор элементов, которые уже стилизованы и готовы к использованию. UIkit Bootstrap помогает избежать самостоятельной верстки макетов.
Если возникнут проблемы при создании собственного интерфейса, возьмите за основу данный шаблон: https://github.com/oscarbotru/.

## Задание 4
В приложении в контроллере реализуйте два контроллера:

 Контроллер, который отвечает за отображение домашней страницы.
 Контроллер, который отвечает за отображение контактной информации.

## * Дополнительное задание
Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.

Для POST-запроса обработка в контроллере будет выглядеть так:

def students_list(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        # а также передается информация, которую заполнил пользователь
        print(name)
    return render(request, 'index.html')

# Продолжение развития магазина (подключние магазина к БД)

## Задание 1
Подключите СУБД PostgreSQL для работы в проекте, для этого:
Создайте базу данных в ручном режиме.
Внесите изменения в настройки подключения.

## Задание 2
В приложении каталога создайте модели:
Product,
Category.
Опишите для них начальные настройки.

К начальным настройкам модели относятся метод 
__str__
 и 
class Meta с описанием свойств модели.

##Задание 3
Для каждой модели опишите следующие поля:
Product
Наименование
Описание
Изображение (превью)
Категория
Цена за покупку
Дата создания (записи в БД)
Дата последнего изменения (записи в БД)
Category
Наименование
Описание
Свяжите продукт и категорию, используя связь между таблицами «Один ко многим».

У одной категории может быть много продуктов, но у одного продукта может быть только одна категория.
Воспользуйтесь специальным полем модели — ForeignKey().
При необходимости подробнее про то, как работает такое поле, можно почитать тут.
Поля «Дата создания» и «Дата последнего изменения» стали стандартом для моделей. Их общепринятые названия — created_at и updated_at соответственно.

Примечание
Для поля с изображением необходимо добавить соответствующие настройки (MEDIA URL, MEDIA ROOT, настроить URL для отображения медиаданных) в проект, а также установить библиотеку для работы с изображениями 
Pillow. Не забудьте обновить файл с зависимостями для проекта после установки новой библиотеки.

## Задание 4
Перенесите отображение моделей в базу данных с помощью инструмента миграций, для этого:
создайте миграции для новых моделей;
примените миграции;
внесите изменения в модель продукта, добавьте поле «Дата производства продукта» (manufactured_at), примените обновление структуры с помощью миграций;
откатите миграцию до состояния, когда поле «Дата производства продукта» (manufactured_at) для модели продукта еще не существовало, и удалите лишнюю миграцию.
Важно сохранять всю историю миграций проекта для сохранения целостности базы данных проекта.

### Подсказка
Чтобы сбросить миграцию до определенной (по номеру), можно воспользоваться командой python manage.py migrate имя_приложения номер_миграции (например, 0003)
Номер миграции написан в названии файла.

## Задание 5
Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.
При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.

## Задание 6
Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
Установите библиотеку ipython для комфортной работы с инструментом shell. Не забудьте зафиксировать изменения в файле зависимостей проекта.

### Подсказка
1. В рамках задания реализуйте ORM-запросы на создание объектов, получение всех объектов, получение одного объекта по 
id, фильтрацию объектов по определенному полю и исключение объектов из выборки.
Для доступа к объектам используйте команду Model.objects… и дополняйте ее различными методами.
Документацию для методов взаимодействия с базой данных через Django ORM можно найти тут.
Чтобы создать объект, необходимо использовать метод create() и перечислить все обязательные поля
Чтобы получить список всех объектов, необходимо использовать метод all().
Чтобы получить один объект, используйте метод get().
Чтобы отфильтровать объекты по определенному значению поля, необходимо использовать метод filter() и указать в скобках 
имя_поля=”значение_поля”.
Чтобы исключить объекты из выборки по определенному значению поля, необходимо использовать метод 
exclude() и указать в скобках имя_поля=”значение_поля”.

2. Сформируйте фикстуры для заполнения базы данных.
Фикстуры создайте командой. Для управления кодировкой используйте опцию 
-Xutf8 для команды. Такой параметр уместно будет использовать на операционной системе Windows.
В общем случае команда для создания фикстур будет выглядеть следующим образом:
python -Xutf8 manage.py dumpdata имя_приложения > имя_папки_с_фикстурами/имя_приложения_data.json

3. Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно ее зачищать от старых данных.

# Продолжение наполнения магазина (данные из БД)

## Задание 1
Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром, на которой необходимо вывести всю информацию о самом товаре.

### Подсказка
Контроллер для отдельной страницы с товаром — это отображение одного товара.
Товар хранится в базе данных с определенным id (в Django принято использовать pk (PrimaryKey)).
Чтобы получить данные о товаре, необходимо забрать данные о нем из базы данных. Сделать это с помощью ORM-запроса, например: 
Model.objects.get(pk=pk)
Для выполнения такого ORM-запроса наш контроллер должен получать аргумент pk (или id) на вход. Контроллеры получают параметры из URL.
URL для контроллера отображения одного товара будет примерно таким: 
path('/путь_к_продукту/<int:pk>', имя_контроллера, name='имя_url')

Чтобы контроллер обработал переданный ему аргумент pk, нам нужно передать его в контроллер:
def имя_контроллера(request, pk):
Соберите контекст для шаблона. В контекст мы передаем данные, которые необходимо отобразить в шаблоне. Контекст формируется в виде словаря и передается в функцию render:
context = {'object': Model.objects.get(pk=pk)}
Обратите внимание на название ключа в словаре контекста. Через него мы будем получать данные об объекте в шаблоне.
Контекст необходимо передать в шаблон для обработки:
return render(request, 'путь_к_шаблону', context)
В самом шаблоне мы получаем данные через обращение к переданному в контексте объекту (по ключу) и обращаемся к его полям через точку, например: 
<p>{{ object.name }}</p>

## Задание 2
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание необходимо обрезать после первых выведенных 100 символов.

### Подсказка
Все товары хранятся в базе данных.
Чтобы получить данные о товарах, необходимо забрать данные о них из базы данных. Сделать это с помощью ORM-запроса, например:
Model.objects.all()
Соберите контекст для шаблона. В контекст мы передаем данные, которые необходимо отобразить в шаблоне. Контекст формируется в виде словаря и передается в функцию render:
context = {'object_list': Model.objects.all()}
Обратите внимание на название ключа в словаре контекста. Через него мы будем получать данные об объекте в шаблоне.
Контекст необходимо передать в шаблон для обработки: return render(request, 'путь_к_шаблону', context)
В самом шаблоне нам нужно получать данные о каждом объекте из списка — в шаблоне необходимо запустить цикл
{% for object in object_list %}
Теперь мы циклично будем обходить каждый объект в списке и обращаться к его полям через точку, например:
{{ object.name }}
Не забудьте закрыть цикл
{% endfor %}

## Задание 3
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон, а также подшаблон с главным меню.
В подшаблон вынесите общие для всех кодовые части (HTML-код). Не забудьте разместить блок с контентом, куда будут вставляться шаблоны, которые используют подшаблон:
{% block content %}
{% endblock %}
И подключите их к другим шаблонам с помощью
{% extends 'путь к базовому шаблону' %}
Код расширенного шаблона разместите внутри блока с контентом.

### Примечание
При необходимости можно выделить больше общих шаблонов.

## Задание 4
Для выводимого изображения на странице реализуйте шаблонный фильтр или шаблонный тег, который преобразует переданный путь в полный путь для доступа к медиафайлу.

### Подсказка
Создайте файл, например: 
your_app/templatetags/имя_файла.py
Создайте переменную для работы с библиотекой шаблонов Django:
register = template.Library()
Внутри файла используйте декоратор 
register.simple_tag()
 для регистрации тега или 
register.filter()
 для фильтра.
Создайте функцию тега/фильтра, которая будет принимать данные и добавлять к ним 
media/
 перед переданной строкой:
def mymedia(data):
    if data:
        return f'/media/{data}'
    return '#'
В вашем шаблоне загрузите ваш тег/фильтр 
{% load имя_файла %}
Используйте его для вывода пути к медиафайлу
<img class="card-img-top" src="{{ object.поле_изображения| название фильтра }}" ... >
или
<img class="card-img-top" src="{{ название тега object.поле_изображения }}" ... >

# Наполнение блога

## Задание 1
Переведите имеющиеся контроллеры с FBV на CBV.
Не забудьте про контроллер контактов. Для его замены можно воспользоваться 
View или TemplateView. Документацию можно найти тут: https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.TemplateView.

## Задание 2
Создайте новую модель блоговой записи со следующими полями:
заголовок;
slug (реализовать через CharField);
содержимое;
превью (изображение);
дата создания;
признак публикации;
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.

CRUD реализуйте на основе CBV (ListView, DetailView, CreateView, UpdateView, DeleteView)
Соблюдайте нейминг шаблонов для CBV контроллеров - …_list.html, …_detail.html, …_form.html.

### Примечание
Slug — человекопонятный URL, представляет собой набор символов, которые можно прочитать как связные слова или предложения в адресной строке и который служит уникальным идентификатором записи в рамках одной модели. Состоит из безопасных для обработки запроса символов:
0–9
a–z (обычно в нижнем регистре)
символ -

## Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

При открытии отдельной статьи увеличивать счетчик просмотров. Для решения этой задачи можно воспользоваться переопределением метода get_object() в DetailView.

### Подсказка
Метод get_object() должен получать данные из вызова метода get_object() родителя (с помощью функции super()), вносить необходимые изменения и сохранять объект в базе данных. Не забудьте вернуть измененный объект из метода.
Примерный код метода в DetailView:
def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.счетчик_просмотров += 1
        self.object.сохранить()
        return текущий_объект
Не забудьте определить верный queryset для View

Выводить в список статей только те, которые имеют положительный признак публикации.
Признак публикации — булево поле. Статья может быть опубликована или нет (True/False). Отфильтруйте статьи блога с помощью ORM-запроса.

При создании динамически формировать slug name для заголовка. Для решения этой задачи можно воспользоваться переопределением метода form_valid() в CreateView.

### Подсказка
Метод form_valid() должен получать данные из формы, вносить необходимые изменения и сохранять объект в базе данных. Не забудьте вызвать метод super().form_valid() для корректного завершения работы метода.
Примерный код метода в CreateView:
def form_valid(self, форма):
        if form.is_valid():
            new_blog = форма.save()
            new_blog.slug = преобразование заголовка в slug с помощью функции slugify()
            new_blog.save() 
        return super().form_valid(форма)

После успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
Для решения этой задачи можно воспользоваться переопределением метода get_success_url() в UpdateView. Метод должен возращать объект reverse с параметрами args.

# Формы и формсеты

## Задание 1
Для модели продуктов реализуйте механизм CRUD, задействовав модуль django.forms.
Условия для пользователей:
могут создавать новые продукты,
не могут создавать продукты с запрещенными словами в названии и описании.

## Задание 2
Добавьте новую модель «Версия», которая должна содержать свои поля.
При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

## Задание 3
Добавьте реализацию работы с формами для версий продукта.

### Примечание
Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы. Для этого можно воспользоваться методом __init__ либо самостоятельно изучить пакет crispy-forms.
При стилизации формы методом __init__ можно создать класс-миксин для сокращения дублирования кода.

Для стилизации булевого поля используйте специальный стиль — form-check-input.


# Авторизация пользователя, регистрация по почте
## Задание 1
Создайте новое приложения для работы с пользователем. Определите собственную модель для пользователя, при этом задайте электронную почту как поле для авторизации.
Также добавьте поля:
аватар,
номер телефона,
страна.
Не забудьте откатить миграции приложения auth до внесения изменений в настройки проекта и переопределения модели для авторизации. Если этого не сделать, вы не сможете взаимодействовать с базой данных. Чтобы откатить миграции приложения 
auth, можно воспользоваться командой python manage.py migrate auth zero

## Задание 2
В сервисе реализуйте функционал аутентификации, а именно:
### Регистрация пользователя по почте и паролю.
Создайте контроллер для регистрации, который будет взаимодействовать с формой регистрации — пользователю достаточно ввести почту и пароль.

### Верификация почты пользователя через отправленное письмо.
В контроллере регистрации переопределите метод form_valid() и встройте автоматическую отправку электронного сообщения пользователю на указанный в форме регистрации адрес.
Для отправки электронной почты воспользуйтесь встроенной в Django функцией send_mail().
Не забудьте настроить почтовый сервер, через который будет происходить отправка электронной почты.

### Авторизация пользователя.
Создайте отдельный контроллер для авторизации (LoginView) и зарегистрируйте его в приложении.

### Восстановление пароля зарегистрированного пользователя на автоматически сгенерированный пароль.
Создайте новый контроллер для восстановления пароля.
В интерфейсе кнопка «Восстановить пароль» должна отображаться на странице входа.
Пользователь вводит адрес электронной почты, в контроллере происходит генерация пароля, перезапись пароля для пользователя с соответсвующим адресом электронной почты и отправка сообщения с новым паролем на адрес почты.
Пароль можно сгенерировать с помощью библиотеки random.
Помните, что пароль в базе данных хранится в захешированном виде. Для установки пароля пользователю можно воспользоваться функцией make_password() (посмотреть в документации про эту функцию).

## Задание 3
Все контроллеры, которые отвечают за работу с продуктами, закройте для анонимных пользователей, при этом создаваемые продукты должны автоматически привязываться к авторизованному пользователю.
Чтобы закрыть контроллеры от анонимных пользователей, добавьте в CBV-контроллеры дополнительное наследование от LoginRequiredMixin.
Не забудьте добавить поле для продуктов, которое будет указывать на владельца. Оно должно быть ссылкой на модель пользователя.
Для автоматической привязки пользователя к продукту переопределите в контроллере создания продукта метод form_valid().

Текущий авторизованный пользователь доступен через self.request.user — запишите его в только что созданный продукт и не забудьте сохранить объект в базу данных.

# Добавление модератора. Права доступа к продуктам.

## Задание 1
Создайте группу для роли модератора и опишите необходимые доступы:
может отменять публикацию продукта,
может менять описание любого продукта,
может менять категорию любого продукта.
Группу создавайте в админке. Права доступа для продуктов опишите в модели продукта и назначьте группе через админку. Не забудьте сохранить группы фикстурой или создать команду для создания групп для отправки наставнику на проверку.

### Примечание
Недостающее поле признака публикации необходимо добавить таким образом, чтобы можно было определять статус продукта. Можно использовать BooleanField со значением False по умолчанию или CharField с указанием вариантов значений (choises). При этом по умолчанию должен быть вариант, который не предполагает публикации продукта.

### Подсказка
Проверяйте права, которые назначены пользователю в контроллерах или шаблонах. Данные об авторизованном пользователе хранятся в объекте request.user. Получить права пользователя в контроллере можно с помощью метода has_perm().
При необходимости проверки прав доступа в шаблонах для отображения, например, кнопок в зависимости от роли пользователя необходимо использовать {{ perms }} . Документацию по использованию можно найти здесь.

## Задание 2
Реализуйте решение, которое проверит, что редактирование продукта доступно только его владельцу.
Внедрите в шаблоны проверку на владельца объекта и отображайте кнопки редактирования только пользователям, которые являются владельцами (если пользователь не наделен другими правами).

# Кеширование и работа с переменными окружения

## Задание 1
Продолжаем работать с проектом. Установите брокер для кеширования Redis. Внесите необходимые настройки и проверьте работоспособность проекта с новыми настройками.
Обратите внимание на то, что Redis не работает на Windows. Для запуска используйте WSL Linux (вы устанавливали его ранее). Инструкцию можно найти здесь.
После проведения настроек Redis будет доступен для использования по адресу 127.0.0.1:6379, если вы не меняли порт для запуска. Если порт был изменен, указывайте тот, на котором запущен процесс.

## Задание 2
Настройте кеширование всего контроллера отображения данных относительно одного продукта.

### Примечание
Помните, что кеширование можно подключать не только в файле views.py, но и в файле маршрутизации urls.py. Важно делать всё в одном месте, чтобы достичь единообразия в коде проекта и не запутаться впоследствии.

## Задание 3
Создайте сервисную функцию, которая будет отвечать за выборку категорий и которую можно переиспользовать в любом месте системы. Добавьте низкоуровневое кеширование для списка категорий.
Также можно реализовать функцию для кеширования списка продуктов. Если вы не использовали категории в своей работе, реализуйте контроллер и шаблон для выдачи списка категорий и в качестве контекста передавайте результат работы этой функции. Также можно воспользоваться переопределением кверисета в CBV.

## Задание 4
Вынесите необходимые настройки в переменные окружения и настройте проект для работы с ними.
К необходимым настройкам относятся все чувствительные данные, которые хранятся в настройках приложения: секретный ключ Django, настройки базы данных, настройки кеширования (адрес подключения к брокеру, включение кеширования), включение режима отладки и любые логины и пароли от сторонних сервисов, например данные учетной записи для отправки почты. Любые данные, которые могут при утечке навредить вашему приложению и являются чувствительными.
## Запуск
Качаем: <br>
```
git clone https://github.com/LatikDesu/newer_lucky.git
```
### Frontend
Открываем терминал № 1, переходим в папку frontend'a <br>

```
cd video-to-text-front
```

Устанавливаем зависимости: <br>
```
npm install
```
Запускаем проект на localhost <br>
```
npm run start
```
Если не открылось автоматически, то в браузере ввести: http://localhost:3000/ <br>

### Backend
Открываем терминал № 2, переходим в папку backend'a <br>
```
cd video-to-text-back
```

Создаем виртуальное окружение: <br>
```
python -m venv venv
(Windows) venv\Scripts\activate.bat
(Mac, Linux) source venv/bin/activate
```

Устанавливаем зависимости: <br>
```
pip install -r requirements.txt
```

Запускаем проект на localhost <br>
```
python webapp.py
```

в браузере ввести: http://localhost:5000/ <br>

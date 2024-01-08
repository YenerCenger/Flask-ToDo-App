# ToDo Uygulaması

Bu, Flask ve SQLAlchemy kullanılarak oluşturulmuş basit bir ToDo web uygulamasıdır. Kullanıcılara görev eklemeleri, tamamlanan olarak işaretlemeleri ve silmeleri için olanak tanır.

## Kullanım

1. **Uygulamayı Çalıştırma:**
    - Bir terminal veya komut istemcisini açın ve `app.py` dosyasının bulunduğu dizine gidin.
    - Aşağıdaki komutu çalıştırın:
        ```bash
        python app.py
        ```
    - Uygulama `http://127.0.0.1:5000/` adresinden erişilebilir.

2. **Ana Sayfa:**
    - Tarayıcınızdan `http://127.0.0.1:5000/` adresine gidin.
    - ToDo görevlerinizi görüntüleyin ve yönetin.

3. **ToDo Ekleyin:**
    - Giriş alanına bir görev girin ve "Ekle" düğmesine tıklayın.
    - Eğer giriş boşsa, bir uyarı mesajı görüntülenir.

4. **ToDo Tamamla:**
    - Bir görevin yanındaki "Tamamla" düğmesine tıklayarak görevi tamamlandı olarak işaretleyin.
    - ToDo'nun durumu değiştirilecektir.

5. **ToDo Silme:**
    - Bir görevin yanındaki "Sil" düğmesine tıklayarak görevi listeden kaldırın.
    - Bir onay mesajı görüntülenecektir.

## Kullanılan Teknolojiler

- Flask: Web uygulamaları oluşturmak için kullanıldı.
- SQLAlchemy: SQLite ile veritabanı işlemleri için kullanıldı.

## Geliştirme

1. **Kodu Klonla:**
    ```bash
    git clone https://github.com/kullanici/ToDoApp.git
    cd ToDoApp
    ```

2. **Bağımlılıkları Yükle:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Uygulamayı Çalıştır:**
    ```bash
    python app.py
    ```

## Katkıda Bulunma

- Hataları bildirmek veya önerilerde bulunmak için [GitHub proje sayfasındaki](https://github.com/YenerCenger/ToDoApp) "Issues" bölümünü kullanabilirsiniz.
- Kodlara katkıda bulunmak için "Pull Requests" gönderebilirsiniz.

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

# ToDo App

This is a simple ToDo web application built with Flask and SQLAlchemy. It allows users to add, mark as complete, and delete tasks.

## Usage

1. **Run the Application:**
    - Open a terminal or command prompt and navigate to the directory where the `app.py` file is located.
    - Run the following command:
        ```bash
        python app.py
        ```
    - The application will be accessible at `http://127.0.0.1:5000/`.

2. **Home Page:**
    - Visit `http://127.0.0.1:5000/` from your browser.
    - View and manage your ToDo tasks.

3. **Add a ToDo:**
    - Enter a task in the input field and click the "Add" button.
    - If the input is empty, a warning message will be displayed.

4. **Complete a ToDo:**
    - Click the "Complete" button next to a task to mark it as complete.
    - The status of the ToDo will be toggled.

5. **Delete a ToDo:**
    - Click the "Delete" button next to a task to remove it from the list.
    - A confirmation message will be displayed.

## Technologies Used

- Flask: Used for building web applications.
- SQLAlchemy: Used for database operations with SQLite.

## Development

1. **Clone the Code:**
    ```bash
    git clone https://github.com/kullanici/ToDoApp.git
    cd ToDoApp
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```bash
    python app.py
    ```

## Contribution

- To report bugs or suggest improvements, use the "Issues" section on the [GitHub project page](https://github.com/YenerCenger/ToDoApp).
- Contributions to the code can be made through "Pull Requests".

## License

This project is licensed under the [MIT License](LICENSE).

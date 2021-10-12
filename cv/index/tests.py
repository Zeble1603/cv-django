from django.http import response
from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from .models import Message
from django.contrib.auth.models import User


class IndexPagesTest(SimpleTestCase):
    # We test the status code, the url name, the template
    
    # Index page
    def test_index_status_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_index_url_name(self):
        response = self.client.get(reverse("index:home"))
        self.assertEquals(response.status_code, 200)

    def test_index_correct_template(self):
        response = self.client.get(reverse("index:home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


    # Work page
    def test_work_status_code(self):
        response = self.client.get("/work/")
        self.assertEquals(response.status_code, 200)

    def test_work_url_name(self):
        response = self.client.get(reverse("index:work"))
        self.assertEquals(response.status_code, 200)

    def test_work_correct_template(self):
        response = self.client.get(reverse("index:work"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "work.html")


    # Education page
    def test_education_status_code(self):
        response = self.client.get("/education/")
        self.assertEquals(response.status_code, 200)

    def test_education_url_name(self):
        response = self.client.get(reverse("index:education"))
        self.assertEquals(response.status_code, 200)

    def test_education_correct_template(self):
        response = self.client.get(reverse("index:education"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")


    # Portfolio page
    def test_portfolio_status_code(self):
        response = self.client.get("/portfolio/")
        self.assertEquals(response.status_code, 200)

    def test_portfolio_url_name(self):
        response = self.client.get(reverse("index:portfolio"))
        self.assertEquals(response.status_code, 200)

    def test_portfolio_correct_template(self):
        response = self.client.get(reverse("index:portfolio"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio.html")   

    # Ortho page
    def test_ortho_status_code(self):
        response = self.client.get("/ortho/")
        self.assertEquals(response.status_code, 200)

    def test_ortho_url_name(self):
        response = self.client.get(reverse("index:ortho"))
        self.assertEquals(response.status_code, 200)

    def test_ortho_correct_template(self):
        response = self.client.get(reverse("index:ortho"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "ortho.html") 

    # Weather page
    def test_weather_status_code(self):
        response = self.client.get("/weather/")
        self.assertEquals(response.status_code, 200)

    def test_weather_url_name(self):
        response = self.client.get(reverse("index:weather"))
        self.assertEquals(response.status_code, 200)

    def test_weather_correct_template(self):
        response = self.client.get(reverse("index:weather"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "weather.html") 

    # Todo page
    def test_todo_status_code(self):
        response = self.client.get("/todo/")
        self.assertEquals(response.status_code, 200)

    def test_todo_url_name(self):
        response = self.client.get(reverse("index:todo"))
        self.assertEquals(response.status_code, 200)

    def test_todo_correct_template(self):
        response = self.client.get(reverse("index:todo"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "todo.html") 

    #Sudoku page
    def test_sudoku_status_code(self):
        response = self.client.get("/sudoku/")
        self.assertEquals(response.status_code, 200)

    def test_sudoku_url_name(self):
        response = self.client.get(reverse("index:sudoku"))
        self.assertEquals(response.status_code, 200)

    def test_sudoku_correct_template(self):
        response = self.client.get(reverse("index:sudoku"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "sudoku.html")                


    # Contact page
    def test_contact_status_code(self):
        response = self.client.get("/contact/")
        self.assertEquals(response.status_code, 200)

    def test_contact_url_name(self):
        response = self.client.get(reverse("index:contact"))
        self.assertEquals(response.status_code, 200)

    def test_contact_correct_template(self):
        response = self.client.get(reverse("index:contact"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")  

    #Thanks page       
    def test_thanks_status_code(self):
        response = self.client.get("/thanks/")
        self.assertEquals(response.status_code, 200)

    def test_thanks_url_name(self):
        response = self.client.get(reverse("index:thanks_message"))
        self.assertEquals(response.status_code, 200)

    def test_thanks_correct_template(self):
        response = self.client.get(reverse("index:thanks_message"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "thanks_message.html") 

class LoginTests(TestCase):
    # We test the login process, the user creation, and the login page

    @classmethod
    def setUp(self):
        self.credentials = {
            'username': 'CristoCanyon',
            'password': 'Lastman'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post(reverse("account:login"),self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)


class MessageTests(TestCase):

    # We test all the pages related to the message object:
    # Object creation / List view / Delete view

    @classmethod
    def setUp(self):
        Message.objects.create(mail="test@gmail.com", text="this is a test")
        self.credentials = {
            'username': 'CristoCanyon',
            'password': 'Lastman'}
        User.objects.create_user(**self.credentials)

    def test_message(self):
        message = Message.objects.get(id=1)
        expected_message_text = message.text
        expected_message_email = message.mail
        self.assertEquals(expected_message_text, "this is a test")
        self.assertEquals(expected_message_email, "test@gmail.com")

    def test_message_list_view(self):
        log = self.client.post(reverse("account:login"),self.credentials, follow=True)
        self.assertTrue(log.context['user'].is_active)
        response = self.client.get(reverse("index:my_messages"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "test@gmail.com")   

    #def test_read(self):
        #log = self.client.post(reverse("account:login"),self.credentials, follow=True)
        #self.assertTrue(log.context['user'].is_active)
        #message = Message.objects.get(id=1)
        #response = self.client.get(reverse("index:message_read", args=(message.id,)), follow = True)
        #self.assertTrue(message.read)


    def test_get_delete_message(self):
        message = Message.objects.get(id=1)
        log = self.client.post(reverse("account:login"),self.credentials, follow=True)
        self.assertTrue(log.context['user'].is_active)
        response = self.client.get(reverse("index:message_delete", args=(message.id,)), follow = True)
        self.assertContains(response, "Are you sure you want to delete this message ?")

    def test_post_delete_message(self):    
        message = Message.objects.get(id=1)
        log = self.client.post(reverse("account:login"),self.credentials, follow=True)
        self.assertTrue(log.context['user'].is_active)
        post_response = self.client.post(reverse("index:message_delete", args=(message.id,)), follow = True)
        self.assertRedirects(post_response, reverse('index:my_messages'), status_code=302)


        


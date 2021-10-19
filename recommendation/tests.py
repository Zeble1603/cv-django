from django.contrib.auth.models import User
from django.db.models.query_utils import select_related_descend
from django.http import response
from django.test import TestCase
from django.urls.base import reverse
from .models import Recommendation

# Public recommendation views tests 

class RecoTests(TestCase):

    @classmethod
    def setUp(self):
        Recommendation.objects.create(
            first_name="Cristo", last_name="Canyon",
            job = "Corbeau", relationship="I was his customer",
            comment = "Hola")
        self.credentials = {
            'username': 'CristoCanyon',
            'password': 'Lastman'}
        User.objects.create_user(**self.credentials)    

    def test_reco(self):
        reco = Recommendation.objects.get(id=1)
        expected_first_name = reco.first_name
        expected_last_name = reco.last_name
        expected_job = reco.job
        expected_relationship = reco.relationship
        expected_comment = reco.comment
        self.assertEquals(expected_first_name, "Cristo")
        self.assertEquals(expected_last_name, "Canyon")
        self.assertEquals(expected_job, "Corbeau")
        self.assertEquals(expected_relationship, "I was his customer")
        self.assertEquals(expected_comment, "Hola")


    def test_reco_list_view(self):
        log = self.client.post(reverse("account:login"),self.credentials, follow=True)
        self.assertTrue(log.context['user'].is_active)
        response = self.client.get(reverse("reco:reco_list"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Cristo")


    def test_reco_publish(self):
        reco = Recommendation.objects.get(id=1)
        self.client.post(reverse("account:login"),self.credentials, follow=True)
        self.client.get(reverse("reco:reco_publish", args=(reco.id,)))
        self.assertTrue(hasattr(reco, "publish_date"))


    def test_validreco_list_view(self):
        reco = Recommendation.objects.get(id=1)
        self.client.post(reverse("account:login"),self.credentials, follow=True)
        self.client.get(reverse("reco:reco_publish", args=(reco.id,)))
        response = self.client.get(reverse("reco:validreco_list"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Cristo")


    def test_reco_detail_view(self):
        reco = Recommendation.objects.get(id=1)
        self.client.post(reverse("account:login"),self.credentials, follow=True)
        response = self.client.get(reverse("reco:reco_detail", args=(reco.id,)))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Cristo")

    def test_reco_update_view(self):
        reco = Recommendation.objects.get(id=1)
        self.client.post(reverse("account:login"),self.credentials, follow=True)
        response = self.client.post(reverse("reco:reco_update", kwargs={'pk':reco.id}),
                                   {"first_name":"Richard", "last_name":"Aldana",
                                    "job" : "Boxer", "relationship" : "I was his customer",
                                    "comment" : "Hola"}) 
        self.assertEquals(response.status_code,302)
        reco.refresh_from_db()
        self.assertEquals(reco.first_name, "Richard")


    def test_get_delete_reco(self):
        reco = Recommendation.objects.get(id=1)
        self.client.post(reverse("account:login"),self.credentials, follow=True)
        response = self.client.get(reverse("reco:reco_delete", kwargs={"pk":reco.id}), follow=True)
        self.assertContains(response, "Are you sure you want to delete this recommendation ?")
        self.assertEquals(response.status_code, 200)


    def test_post_delete_reco(self):
        reco = Recommendation.objects.get(id=1)
        self.client.post(reverse("account:login"),self.credentials, follow=True)
        post_response = self.client.post(reverse("reco:reco_delete", kwargs={"pk":reco.id}), follow = True)        
        self.assertRedirects(post_response, reverse('reco:reco_list'), status_code=302)
        reco_list = Recommendation.objects.all().count()
        self.assertEquals(reco_list, 0)